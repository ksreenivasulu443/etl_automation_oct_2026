import numpy as np
from faker import Faker

fake = Faker("en_IN")


def generate_customer_data(num_records):

    customer_data = []

    for customer_id in range(1, num_records + 1):

        name = fake.name()

        age = fake.random_int(min=18, max=80)

        phone_number = fake.random_int(
            min=6000000000,
            max=9999999999
        )

        gender = fake.random_element(elements=["M", "F"])

        customer_data.append(
            (customer_id, name, age, phone_number, gender)
        )

    return np.array(customer_data, dtype=object)


data = generate_customer_data(10)

print(data)