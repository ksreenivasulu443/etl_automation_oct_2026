import numpy as np
import random
from datetime import datetime


def generate_customer_data(num_records):

    names = ["Ravi", "Priya", "Rahul", "Anjali",
             "Kiran", "Sneha", "Arjun", "Divya"]

    genders = ["M", "F","UN"]

    customer_data = []

    for customer_id in range(1, num_records + 1):

        name = random.choice(names)

        age = random.randint(1, 80)

        phone_number = random.randint(9000000000, 9999999999)

        gender = random.choice(genders)

        customer_data.append(
            (customer_id, name, age, phone_number, gender)
        )

    return np.array(customer_data, dtype=object)


data = generate_customer_data(10)

print(data)

# Generate dynamic filename
timestamp = datetime.now().strftime("%d%m%Y%H%M%S")

file_name = f"customer_{timestamp}.csv"

# Write NumPy array into CSV file
np.savetxt(
    f"C:\\Users\\Haritha\\PycharmProjects\\etl_automation_oct_2026\\{file_name}.csv",
    data,
    delimiter=",",
    fmt="%s",
    header="CustomerID,Name,Age,PhoneNumber,Gender",
    comments=""
)

print(f"CSV file generated successfully: {file_name}")