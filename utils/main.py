from utils import insert_data_into_tables
from utils import create_tables
from utils import create_database

print(" В данный момент создается БД и заполняется данными")

create_database("course_work_5")
create_tables("course_work_5")
insert_data_into_tables("course_work_5")

print("База данных создана, в дальнейшем данные получаем из это БД ")
print("Перейдите и запустите файл db_manager.py")
