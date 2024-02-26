from utils import insert_data_into_tables
from utils import create_tables
from utils import create_database
from classes.db_manager import DBManager

print(" В данный момент создается БД и заполняется данными")

#create_database("course_work_5")
#create_tables("course_work_5")
#insert_data_into_tables("course_work_5")

print("База данных создана, в дальнейшем данные получаем из это БД ")
work_with_db = DBManager('course_work_5')
while True:
    print('Выберите действие')
    print('1  -- Получить список всех компаний и количество вакансий у каждой компании')
    print('2  -- Получить список всех вакансий с указанием названия компании')
    print('      названия вакансии и зарплаты и ссылки на вакансию')
    print('3  -- Получить среднюю зарплату по вакансиям')
    print('4  -- Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям')
    print('5  -- Получить список всех вакансий, в названии которых содержится переданное слово')
    print('6  -- Выход')

    user_sel = input('Ваш выбор ->')

    if user_sel == 1:
        work_with_db.get_companies_and_vacancies_count()



