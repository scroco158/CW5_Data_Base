import psycopg2
from utils.config import config


class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query):
        conn = psycopg2.connect(dbname=self.db_name, **config())
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        conn.close()

        return result

    def get_companies_and_vacancies_count(self):
        """ Получает список всех компаний и количество вакансий у каждой компании """

        query = ('SELECT employers.name, COUNT(*) AS vac_count '
                 'FROM employers JOIN vacancies ON employers.id = vacancies. employer '
                 'GROUP BY employers.id')

        result = self.execute_query(query)

        for item in result:
            print(item)

        return result

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
           названия вакансии и зарплаты и ссылки на вакансию. """

        query = ('SELECT employers.name, vacancies.name, vacancies.salary_from, vacancies.salary_to, vacancies.url '
                 'FROM employers JOIN vacancies ON employers.id = vacancies. employer '
                 'ORDER BY employers.name, vacancies.salary_from')

        result = self.execute_query(query)

        for item in result:
            print(item)

        return result

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям.
           Отображает только те вакансии, где есть данные по ЗП """

        query = ("""
        SELECT vacancies.name AS VACANCY, round(AVG(vacancies.salary_from)) AS AVERAGE_SALARY_FROM, 
                                          round(AVG(vacancies.salary_to)) AS AVERAGE_SALARY_TO
        FROM employers
        JOIN vacancies ON employers.id = vacancies. employer
        WHERE vacancies.salary_from <> 0 and vacancies.salary_to <> 0
        GROUP BY vacancies.name
        ORDER BY AVG(vacancies.salary_from)
        """)

        result = self.execute_query(query)

        for num, item in enumerate(result, 1):
            print(num, item)

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
           Отображает только те вакансии, где есть данные по ЗП """

        print('Средняя ЗП по всем вакансиям где есть информация:')

        query = ("""
                 SELECT round(avg(salary_from))
                 FROM vacancies
                 WHERE salary_from > (SELECT AVG(salary_from) from vacancies where salary_from <> 0)
        """)
        result = self.execute_query(query)
        print(result)

        query = ("""
                 SELECT DISTINCT name, salary_from
                 FROM vacancies
                 WHERE salary_from > (SELECT AVG(salary_from) from vacancies where salary_from <> 0)
                 ORDER BY salary_from
                """)
        result = self.execute_query(query)

        print('Список вакансий с ЗП выше средней:')

        for num, item in enumerate(result, 1):
            print(num, item)

    def get_vacancies_with_keyword(self, text: str):
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""

        str1 = "'%" + text.lower() + "%'"
        str2 = "'%" + text.capitalize() + "%'"

        query = f"SELECT name FROM vacancies WHERE name LIKE {str1} OR name LIKE {str2}"

        result = self.execute_query(query)

        print(f'Список вакансий по таким выборкам : {str1} and {str2}')

        for num, item in enumerate(result, 1):
            print(num, item)


#work_with_db = DBManager('course_work_5')
#work_with_db.get_companies_and_vacancies_count()