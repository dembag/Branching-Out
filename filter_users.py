import json


def filter_users_by_name(name):
    """
    Filters users database by name.
    Prints the users that match the parameter.
    :param name: str
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """
    Filters users by age.
    Prints the users with the given age.
    :param age: int
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == int(age)]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """
    Filters users by email address.
    Prints the users that match the given email address
    :param email: str
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('name', 'age', 'email'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    if filter_option == "age":
        age_to_search = input("Enter the age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    if filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
