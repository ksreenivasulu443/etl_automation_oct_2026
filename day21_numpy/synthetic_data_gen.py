import numpy as np
import random

def generate_customer_data(num_records):

    names = ["Ravi", "Priya", "Rahul", "Anjali",
             "Kiran", "Sneha", "Arjun", "Divya"]

    genders = ["M", "F"]

    customer_data = []

    # customer_ids = np.arange(1, 1 + num_records)

    for customer_id in range(1, num_records + 1):

        name = random.choice(names)

        age = random.randint(18, 80)

        phone_number = random.randint(1000000000, 9999999999)

        gender = random.choice(genders)

        customer_data.append(
            (customer_id, name, age, phone_number, gender)
        )

    return np.array(customer_data, dtype=object)


data = generate_customer_data(10)

print(data)