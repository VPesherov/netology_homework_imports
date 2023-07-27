import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    calculate_salary()
    get_employees()
    now = datetime.datetime.now()
    print(now.strftime("%d-%m-%Y"))


if __name__ == '__main__':
    main()
