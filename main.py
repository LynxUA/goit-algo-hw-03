'''
Homework 1
Please pay attention that the names of the function parameters were renamed 
in order to prevent conflicts with the outer scope
'''

from datetime import datetime
from datetime import date
from datetime import timedelta
import random
import re

print("############## Task 1 start ##############")
def get_days_from_today(incoming_date: str) -> int:
    '''
    Returns days from today to date
    '''
    try:
        provided_datetime = datetime.strptime(incoming_date, "%Y-%m-%d")
    except ValueError:
        print("Please provide a valid date")
        return 0
    now = datetime.today()
    return (provided_datetime - now).days

print(get_days_from_today("2024-05-21"))
print(get_days_from_today("2024-0421"))
print("############## Task 1 end ##############")

print("############## Task 2 start ##############")
def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list[int]:
    '''
    Generates numbers for a lottery
    '''
    random_nums = []
    for _ in range(1, quantity):
        random_nums.append(random.randint(min_number, max_number))
    return random_nums

print(get_numbers_ticket(1, 10, 10))
print(get_numbers_ticket(1, 10, -10))
print(get_numbers_ticket(-1, 10, 10))
print("############## Task 2 end ##############")

print("############## Task 3 start ##############")
def normalize_phone(phone_number: str) -> str:
    '''
    Returns a normalized number
    '''
    pattern = r"\D"
    replacement = r""
    phone_nums = re.sub(pattern, replacement, phone_number)
    if len(phone_nums) == 10:
        return f"+38{phone_nums}"
    if len(phone_nums) == 12:
        return f"+{phone_nums}"
    return "Invalid number"

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
print("############## Task 3 end ##############")

print("############## Task 4 start ##############")
def get_upcoming_birthdays(users_birthdays: list[dict]) -> list[dict]:
    '''
    Returns dictionaries that specify upcoming birthdays for this week 
    (or next monday, if the birthdays occur during the weekends)
    '''
    current_date = datetime.today().date()
    next_birthdays = []
    for user in users_birthdays:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = date(current_date.year, birthday.month, birthday.day)
        start_of_the_year = date(current_date.year, 1, 1)
        current_week = int((current_date - start_of_the_year).days / 7)
        birthday_week = int((birthday_this_year - start_of_the_year).days / 7)
        if current_week == birthday_week:
            birthday_weekdate = birthday_this_year.isoweekday()
            if birthday_weekdate == 6:
                congr_date = birthday_this_year + timedelta(days=2)
            elif birthday_weekdate == 7:
                congr_date = birthday_this_year + timedelta(days=1)
            else:
                congr_date = birthday_this_year
            next_birthdays.append({
                "name": user["name"],
                "congratulation_date": congr_date.strftime("%Y.%m.%d")
                })
    return next_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.20"},
    {"name": "Jane Smith", "birthday": "1990.04.17"},
    {"name": "Jack Black", "birthday": "1992.04.21"},
    {"name": "Volodymyr Zelenskyy", "birthday": "1978.01.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
print("############## Task 4 end ##############")
