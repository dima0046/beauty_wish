from webapp import create_app
from webapp.stores.parsers.podrujka_parsing import get_podrujka_make

app = create_app()
with app.app_context(): # функция, чтобы обращаться к бд
    get_podrujka_make()