from faker import Faker
import pandas as pd

fake = Faker("en_US")


def generate_customer_data(num_records):

    customer_data = []

    for customer_id in range(1, num_records + 1):

        gender = fake.random_element(elements=["M", "F"])

        if gender == "M":
            name = fake.name_male()
        else:
            name = fake.name_female()

        customer = {
            "customer_id": customer_id,
            "customer_name": name,
            "age": fake.random_int(min=18, max=80),
            "gender": gender,
            "email": fake.unique.safe_email(),
            "phone_number": fake.unique.random_int(
                min=6000000000,
                max=9999999999
            ),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "postal_code": fake.postcode(),
            "country": "US",
            "registration_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),
            "customer_status": fake.random_element(
                elements=["Active", "Inactive"]
            )
        }

        customer_data.append(customer)

    return pd.DataFrame(customer_data)


# Generate 1000 customer records
df = generate_customer_data(1000)

# Write DataFrame into CSV file
df.to_csv("customer_data.csv", index=False)

print(df.head())

print("Total records generated:", len(df))
print("CSV file generated successfully")