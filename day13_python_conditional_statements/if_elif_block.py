# if conditions:
#     statements
# elif conditions:
#     stataments
# elif conditions:
#     stataments



name = input("Enter your name: ").lower()


if name == "sreeni":
    print("Welcome to Sreeni")
elif name == "pooja": # one elif is True next/subsequent elif checks will be skipped
    print("Welcome to Pooja")
elif name == "sreeni":
    print("Welcome to Ramya")


print("Outside of if-elif block")