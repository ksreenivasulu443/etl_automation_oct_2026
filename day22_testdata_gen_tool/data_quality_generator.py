# Data Quality Test Data Generator
# Install: pip install streamlit faker pandas pyarrow
# Run: streamlit run data_quality_generator.py

import random
import json
from datetime import date, datetime, timedelta
from faker import Faker
import pandas as pd
import streamlit as st


# =================================================================
# Domain and dataset configurations
# =================================================================

METHODS = ['Sequential number','Random integer','Random decimal','First name','Last name','Full name','Email','Phone number','Address','City','State','Country','Postal code','Date','Timestamp','Boolean','UUID','List of values','Fixed value']
TYPES = ['Integer','Float','String','Date','Timestamp','Boolean']

def column(name, method='Fixed value', dtype='String', minimum=0, maximum=100, values='Sample'):
    return dict(name=name, type=dtype, method=method, minimum=minimum, maximum=maximum, start_date='2020-01-01', end_date='2026-12-31', values=values)

def identifier(name):
    return column(name,'Sequential number','Integer',1,100)

def integer(name, low=1, high=100):
    return column(name,'Random integer','Integer',low,high)

def money(name):
    return column(name,'Random decimal','Float',100,100000)

def date_column(name):
    return column(name,'Date','Date')

def category(name, values):
    return column(name,'List of values',values=values)

customers = [identifier('customer_id'),column('first_name','First name'),column('last_name','Last name'),category('gender','M,F,Other'),integer('age',18,80),column('email','Email'),column('phone_number','Phone number'),column('address','Address'),column('city','City'),column('state','State'),column('country','Country'),date_column('registration_date')]
DOMAINS = {
 'Retail': {'Customers':customers,'Products':[identifier('product_id'),category('product_name','Laptop,Phone,Chair,Book'),category('category','Electronics,Furniture,Books'),money('price'),integer('stock',0,500)],'Orders':[identifier('order_id'),integer('customer_id'),integer('product_id'),integer('quantity',1,10),money('amount'),date_column('order_date')]},
 'Banking': {'Customers':customers,'Accounts':[identifier('account_id'),integer('customer_id'),category('account_type','Savings,Current'),money('balance'),date_column('opened_date')],'Transactions':[identifier('transaction_id'),integer('account_id'),money('amount'),category('transaction_type','Credit,Debit'),column('transaction_time','Timestamp','Timestamp')]},
 'Insurance': {'Customers':customers,'Policies':[identifier('policy_id'),integer('customer_id'),category('policy_type','Life,Health,Motor'),money('premium'),date_column('start_date')],'Claims':[identifier('claim_id'),integer('policy_id'),money('claim_amount'),date_column('claim_date'),category('status','Pending,Approved,Rejected')]},
 'Healthcare': {'Patients':[identifier('patient_id'),column('patient_name','Full name'),integer('age',1,100),column('phone_number','Phone number')],'Doctors':[identifier('doctor_id'),column('doctor_name','Full name'),category('specialty','General,Cardiology,Orthopedics')],'Appointments':[identifier('appointment_id'),integer('patient_id'),integer('doctor_id'),column('appointment_time','Timestamp','Timestamp')]},
 'HR': {'Employees':[identifier('employee_id'),column('employee_name','Full name'),column('email','Email'),integer('department_id'),date_column('joining_date')],'Departments':[identifier('department_id'),category('department_name','HR,IT,Finance,Sales')],'Salaries':[identifier('salary_id'),integer('employee_id'),money('salary'),date_column('payment_date')]},
 'Custom': {'User-defined dataset':[identifier('id')]}}


# =================================================================
# Positive data generation
# =================================================================

def convert(value, dtype):
    if dtype == 'String': return str(value)
    if dtype == 'Integer':
        if isinstance(value,float) and not value.is_integer(): raise ValueError('Fractional value cannot be an integer')
        return int(value)
    if dtype == 'Float': return float(value)
    if dtype == 'Date': return date.fromisoformat(str(value)[:10])
    if dtype == 'Timestamp': return datetime.fromisoformat(str(value))
    if dtype == 'Boolean':
        if str(value).lower() not in ('true','false','1','0'): raise ValueError('Use true or false')
        return str(value).lower() in ('true','1')
    raise ValueError('Unknown data type')

def generate_data(columns, count, seed=None):
    rng = random.Random(seed)
    fake = Faker('en_US')
    fake.seed_instance(seed)
    names = [c['name'] for c in columns]
    if not names or any(not isinstance(n,str) or not n.strip() for n in names) or len(set(names)) != len(names):
        raise ValueError('Column names must be nonempty and unique.')
    providers = {'First name':fake.first_name,'Last name':fake.last_name,'Full name':fake.name,'Email':fake.email,'Phone number':lambda: fake.numerify('##########'),'Address':fake.address,'City':fake.city,'State':fake.state,'Country':fake.country,'Postal code':fake.postcode,'UUID':fake.uuid4}
    data = {}
    for c in columns:
        name, method, dtype = c['name'], c['method'], c['type']
        try:
            if method not in METHODS or dtype not in TYPES: raise ValueError('Select a method and type')
            values = []
            for i in range(count):
                if method in providers: value = providers[method]()
                elif method == 'Sequential number': value = int(c['minimum']) + i
                elif method == 'Random integer': value = rng.randint(int(c['minimum']),int(c['maximum']))
                elif method == 'Random decimal':
                    if c['minimum'] > c['maximum']: raise ValueError('Minimum exceeds maximum')
                    value = round(rng.uniform(c['minimum'],c['maximum']),2)
                elif method in ('Date','Timestamp'):
                    start,end = date.fromisoformat(c['start_date']),date.fromisoformat(c['end_date'])
                    day = start + timedelta(days=rng.randint(0,(end-start).days))
                    value = day if method == 'Date' else datetime.combine(day,datetime.min.time()) + timedelta(seconds=rng.randrange(86400))
                elif method == 'Boolean': value = rng.choice([True,False])
                elif method == 'List of values': value = rng.choice([v.strip() for v in c['values'].split(',') if v.strip()])
                else: value = c['values']
                value = convert(value,dtype)
                if value == '': raise ValueError('Positive values cannot be empty')
                values.append(value)
            data[name] = pd.Series(values,dtype=object)
        except Exception as exc: raise ValueError(f'{name}: {exc}') from exc
    return pd.DataFrame(data)


# =================================================================
# Negative data generation
# =================================================================

SCENARIOS = ['NULL values','Empty strings','Duplicate values','Duplicate records','Invalid email','Invalid phone number','Invalid date','Negative numbers','Out-of-range values','Special characters','Leading spaces','Trailing spaces','Incorrect data type','Exceed maximum length','Invalid categorical value','Missing column','Additional column']
STRUCTURAL = ['Missing column','Additional column']

def apply_negative(df, columns, rules, mode, percent, seed=None):
    df = df.copy()
    original = df.copy()
    rng = random.Random(seed)
    report = []
    affected = set()
    n = len(df)
    config = {c['name']:c for c in columns}
    if mode == 'Positive': return df, report, affected
    target = n if mode == 'Negative' else round(n*percent/100)
    if not rules and target: raise ValueError('Add negative rules.')
    if any(r['scenario'] in STRUCTURAL for r in rules) and mode == 'Mixed': raise ValueError('Missing/additional columns affect the entire dataset; use Negative mode.')
    pool = rng.sample(range(n),target)
    cursor = 0
    for r in rules:
        col, scenario, pct = r['column'],r['scenario'],float(r['percentage'])
        if not 0 < pct <= 100: raise ValueError('Rule percentage must be above 0 and at most 100.')
        k = round(n*pct/100)
        if k > target: raise ValueError('Rule percentage exceeds the negative record budget.')
        if scenario in STRUCTURAL:
            if pct != 100: raise ValueError('Schema rules require 100%.')
            if scenario == 'Missing column':
                if col not in df or len(df.columns)==1: raise ValueError('Cannot remove this column.')
                df.drop(columns=col,inplace=True)
            else:
                col = r.get('extra_name') or 'unexpected_column'
                if col in df: raise ValueError('Additional column already exists.')
                df[col] = 'unexpected'
            affected.update(range(n))
            report.append(dict(row_number='ALL',column=col,scenario=scenario,original_value='present' if scenario=='Missing column' else 'absent',modified_value='absent' if scenario=='Missing column' else 'present'))
            continue
        if scenario != 'Duplicate records' and col not in df: raise ValueError('Select an existing column.')
        c = config.get(col,{})
        dtype = c.get('type')
        string_rules = ['Empty strings','Invalid email','Invalid phone number','Special characters','Leading spaces','Trailing spaces','Exceed maximum length','Invalid categorical value']
        if scenario in string_rules and dtype != 'String': raise ValueError(f'{scenario} requires a String column.')
        if scenario in ['Negative numbers','Out-of-range values'] and dtype not in ['Integer','Float']: raise ValueError('Numeric scenario requires numeric column.')
        if scenario == 'Invalid date' and dtype not in ['Date','Timestamp','String']: raise ValueError('Invalid date requires date, timestamp or string.')
        if scenario == 'Invalid categorical value' and c.get('method') != 'List of values': raise ValueError('Use a list-generated column.')
        if scenario == 'Out-of-range values' and c.get('method') not in ['Random integer','Random decimal']: raise ValueError('Out-of-range requires random numeric bounds.')
        if not k: continue
        # Cycle through a shuffled pool to maximize distinct affected rows.
        rows = [pool[(cursor+j)%target] for j in range(k)]
        cursor += k
        if scenario in ['Duplicate values','Duplicate records']:
            donors = [i for i in range(n) if i not in rows]
            if not donors: raise ValueError('Duplicate rules need at least one unaffected donor row.')
            donor = donors[0]
        for i in rows:
            old = df.loc[i].to_dict() if scenario=='Duplicate records' else df.at[i,col]
            if scenario=='Duplicate records':
                new = df.loc[donor].to_dict()
                df.loc[i] = df.loc[donor].copy()
            else:
                if scenario=='NULL values': new=None
                elif scenario=='Empty strings': new=''
                elif scenario=='Duplicate values': new=df.at[donor,col]
                elif scenario=='Invalid email': new='invalid-email'
                elif scenario=='Invalid phone number': new='ABC123'
                elif scenario=='Invalid date': new='2026-99-99'
                elif scenario=='Negative numbers': new=-abs(old or 0)-1
                elif scenario=='Out-of-range values': new=c['maximum']+1
                elif scenario=='Special characters': new='@#$%'+str(old)
                elif scenario=='Leading spaces': new='  '+str(old)
                elif scenario=='Trailing spaces': new=str(old)+'  '
                elif scenario=='Incorrect data type': new=12345 if dtype=='String' else 'WRONG_TYPE'
                elif scenario=='Exceed maximum length': new='X'*(int(r.get('max_length',50))+1)
                elif scenario=='Invalid categorical value':
                    new='INVALID_CATEGORY'
                    while new in c['values'].split(','): new+='X'
                else: raise ValueError('Unknown scenario')
                df.at[i,col]=new
            affected.add(i)
            report.append(dict(row_number=i+1,column='ALL' if scenario=='Duplicate records' else col,scenario=scenario,original_value=repr(old),modified_value=repr(new)))
    if len(affected)!=target: raise ValueError(f'Rules cover {len(affected)} rows; expected {target}. Increase rule percentages or reduce negative target.')
    return df,report,affected


# =================================================================
# File exports
# =================================================================

def export_files(df, columns, count, name, formats, delimiter=',', header=True, lines=False):
    files, warnings = [], []
    if not 1 <= count <= len(df): raise ValueError('File count must be between 1 and record count.')
    base, remainder = divmod(len(df),count)
    start = 0
    for i in range(count):
        end = start + base + (i < remainder)
        part = df.iloc[start:end]
        start = end
        for fmt in formats:
            filename = f'{name}_{i+1:03d}.{fmt.lower()}'
            try:
                if fmt == 'CSV': content = part.to_csv(index=False,sep=delimiter,header=header).encode('utf-8')
                elif fmt == 'JSON': content = part.to_json(orient='records',lines=lines,date_format='iso').encode('utf-8')
                else:
                    import pyarrow as pa
                    import pyarrow.parquet as pq
                    types = {'Integer':pa.int64(),'Float':pa.float64(),'String':pa.string(),'Date':pa.date32(),'Timestamp':pa.timestamp('us'),'Boolean':pa.bool_()}
                    config = {c['name']:c['type'] for c in columns}
                    arrays = []
                    for col in part:
                        dtype = config.get(col,'String')
                        vals = part[col].tolist()
                        from datetime import date, datetime
                        expected = {'Integer':int,'Float':(int,float),'String':str,'Date':date,'Timestamp':datetime,'Boolean':bool}[dtype]
                        if any(v is not None and not isinstance(v,expected) for v in vals): raise ValueError(f'{col} contains incompatible values for {dtype}')
                        arrays.append(pa.array(vals,type=types[dtype],safe=True))
                    table = pa.Table.from_arrays(arrays,names=list(part.columns))
                    sink = pa.BufferOutputStream()
                    pq.write_table(table,sink)
                    content = sink.getvalue().to_pybytes()
                files.append((filename,content))
            except Exception as exc: warnings.append(f'{filename}: {exc}. File skipped.')
    return files,warnings


# =================================================================
# Streamlit user interface
# =================================================================

def main():
    st.set_page_config(page_title='Data Quality Test Data Generator',layout='wide')
    st.title('Data Quality Test Data Generator')
    st.caption('Synthetic data for ETL testing • No coding required')
    st.header('1. Select domain and dataset')
    a,b=st.columns(2)
    domain=a.selectbox('Domain',list(DOMAINS))
    dataset=b.selectbox('Dataset',list(DOMAINS[domain]))
    predefined=DOMAINS[domain][dataset]
    key=f'{domain}_{dataset}'
    st.header('2. Select or customize columns')
    all_names=[c['name'] for c in predefined]
    all_selected=st.checkbox('Select all predefined columns',True,key='all_'+key)
    selected=st.multiselect('Include columns',all_names,default=all_names if all_selected else [],key=f'include_{key}_{all_selected}')
    excluded=st.multiselect('Exclude columns',selected,key='exclude_'+key)
    base=[c for c in predefined if c['name'] in selected and c['name'] not in excluded]
    st.caption('Edit names, types and methods. Add rows using +. Dates use YYYY-MM-DD; list values are comma-separated. Minimum is the starting number for sequences.')
    editor=st.data_editor(pd.DataFrame(base,columns=list(column('example'))),num_rows='dynamic',hide_index=True,key=f'editor_{key}_{selected}_{excluded}',column_config={'type':st.column_config.SelectboxColumn('Data type',options=TYPES,required=True),'method':st.column_config.SelectboxColumn('Generation method',options=METHODS,required=True),'name':st.column_config.TextColumn('Column name',required=True)},use_container_width=True)
    columns=editor.to_dict('records')
    st.header('3. Configure records and test data scenarios')
    a,b,c,d=st.columns(4)
    count=a.number_input('Records',1,100000,1000)
    file_count=b.number_input('Files per format',1,100,1)
    name=c.text_input('Output file name','test_data')
    seed_text=d.text_input('Random seed (optional)','42')
    mode=st.radio('Test data type',['Positive','Negative','Mixed'],horizontal=True)
    percent=100 if mode=='Negative' else 0
    rules=[]
    if mode=='Mixed':
        percent=st.slider('Negative records (%)',0,100,20)
        st.caption(f'Positive: {100-percent}% | Negative: {percent}%')
    if mode!='Positive':
        st.info('Rule percentages refer to total records. Rules can overlap. Their combined coverage must match the negative record target. Schema changes require Negative mode and 100%.')
        names=[str(c['name']) for c in columns if c.get('name')]
        rules_table=st.data_editor(pd.DataFrame([{'column':names[0] if names else '', 'scenario':'NULL values','percentage':percent or 1,'max_length':50,'extra_name':'unexpected_column'}]),num_rows='dynamic',hide_index=True,key='rules_'+key+mode,column_config={'column':st.column_config.SelectboxColumn('Column',options=names),'scenario':st.column_config.SelectboxColumn('Scenario',options=SCENARIOS,required=True),'percentage':st.column_config.NumberColumn('Percentage',min_value=0.01,max_value=100,required=True),'max_length':st.column_config.NumberColumn('Maximum length',min_value=1,max_value=10000)},use_container_width=True)
        rules=rules_table.to_dict('records')
    st.header('4. Select output file formats')
    formats=st.multiselect('Formats',['CSV','JSON','Parquet'],default=['CSV'])
    delimiter=','; header=True; lines=False
    if 'CSV' in formats:
        delimiter=st.selectbox('CSV delimiter',['Comma','Pipe','Tab','Semicolon'])
        delimiter={'Comma':',','Pipe':'|','Tab':'\t','Semicolon':';'}[delimiter]
        header=st.checkbox('Include CSV header',True)
    if 'JSON' in formats: lines=st.radio('JSON structure',['JSON array','JSON Lines'])=='JSON Lines'
    st.header('5. Generate, preview and download data')
    if st.button('Generate test data',type='primary'):
        st.session_state.pop('result',None)
        try:
            if not formats: raise ValueError('Select at least one format.')
            if not name.strip() or any(x in name for x in '/\\'): raise ValueError('Enter a simple output filename.')
            seed=int(seed_text) if seed_text.strip() else None
            with st.spinner('Generating synthetic data...'):
                df=generate_data(columns,count,seed)
                df,report,affected=apply_negative(df,columns,rules,mode,percent,seed)
                files,warnings=export_files(df,columns,file_count,name,formats,delimiter,header,lines)
                st.session_state.result=(df,report,affected,files,warnings)
        except Exception as exc: st.error(str(exc))
    if 'result' in st.session_state:
        df,report,affected,files,warnings=st.session_state.result
        st.caption('Showing the last generated dataset. Generate again to apply configuration changes.')
        metrics=st.columns(6)
        for slot,label,value in zip(metrics,['Records','Columns','Positive','Negative','NULL cells','Duplicate records'],[len(df),len(df.columns),len(df)-len(affected),len(affected),int(df.isna().sum().sum()),int(df.duplicated().sum())]): slot.metric(label,value)
        # Mixed-type columns may not be displayable by Arrow; stringify preview only.
        st.dataframe(df.head(100).apply(lambda s:s.map(lambda v:None if v is None else str(v))),use_container_width=True)
        for warning in warnings: st.warning(warning)
        for filename,content in files: st.download_button(filename,content,file_name=filename,key='download_'+filename)
        audit=pd.DataFrame(report,columns=['row_number','column','scenario','original_value','modified_value'])
        st.subheader('Negative test data report')
        st.dataframe(audit.head(100),use_container_width=True)
        st.download_button('Download full negative report',audit.to_csv(index=False).encode(),file_name='negative_report.csv')

if __name__ == "__main__":
    main()
