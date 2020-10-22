
import datetime

import utill


def get_birthday_from_user():
    print('when where you born?: \n')
    year = int(input('Year [YYYY]: \n'))
    month = int(input('Month [MM]: \n'))
    day = int(input('Day [DD]: \n'))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_birthday_info(days):
    if days < 0:
        print(f"\nYou had your birthday {-days} days ago this year.")
    elif days > 0:
        print(f"\nYour birthday is in {days} days!")
    else:
        print("\nHappy Birthday!")


def main():
    utill.print_header(code_name='BIRTHDAY APP')
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)


if __name__ == '__main__':
    main()
