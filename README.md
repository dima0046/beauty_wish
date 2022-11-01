# Beauty Wish
Агрегатор косметических продуктов. Поиск наиболее выгодных предложений.

Инструкция запуска.
1. Установить зависимостей
pip install -r requirements.txt
2. Создать базу данных
python3 create_db.py 
Или применить миграцию flask db stamp cc8651750878
3. Создадим пользователя с правами администратора 
python3 create_admin.py
4. Спарсить данные
python3 get_all_products.py
5. Сделать run.sh исполняемым фалйом 
chmod +x run.sh
6. Запустить программу 
./run.sh
7. Или запустить программу
FLASK_APP=webapp.py FLASK_DEBUG=1 TEMPLATES_AUTO_RELOAD=1 flask run
