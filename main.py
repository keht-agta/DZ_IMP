from aplication.db.people import get_employees
from aplication.salary import calculate_salary
from dirty_main import *


if __name__ == '__main__':
    print ("Текущее время: ", datetime.now())
    time_str= input(f"Для перевода даты в Unix время введите дату и время события(год месяц число час минута секунда): ")
    time_to_unixtime(time_str)
    user_id = int(input("Введите ид пользователя от 1 до 3:"))
    user_salary = int(input("А его ЗП:"))
    user_name = get_employees(user_id)
    salary_for_year = calculate_salary(user_salary)
    print(f'{user_name} за год получает ЗП в размере {salary_for_year}')