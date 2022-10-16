# beauty_wish

1) Установить зависимостей
pip install -r requirements.txt
2) Создать базу данных
python3 create_db.py 
3) Создадим пользователя с правами администратора 
python3 create_admin.py
4) Спарсить данные
python3 get_all_products.py
5) Запустить сайт
FLASK_APP=webapp.py FLASK_DEBUG=1 TEMPLATES_AUTO_RELOAD=1 flask run
