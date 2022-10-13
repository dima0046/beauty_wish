# beauty_wish

1) Установить зависимости
pip install -r requirements.txt
2) Создать базу данных
python3 create_db.py 
3) Спарсить данные
python3 get_all_products.py
4) Запустить сайт
FLASK_APP=webapp.py FLASK_DEBUG=1 TEMPLATES_AUTO_RELOAD=1 flask run
