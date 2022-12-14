
from flask import abort, Blueprint, current_app, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required

from webapp.stores.models import Comment, Products, Stores
from webapp.db import db
from webapp.stores.forms import CommentForm
from webapp.utils import get_redirect_target


blueprint = Blueprint('products', __name__)

@blueprint.route('/')  # декоратор
def index():
    page_title = "Beauty Wish"
    # weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
    # get_podrujka_make()


    product_list = Products.query.all()
    #product_list1 = Products.query.
    return render_template('products/index.html', page_title=page_title, product_list=product_list)

@blueprint.route('/product/<int:product_id>')
def single_item(product_id):
    my_product = Products.query.filter(Products.id == product_id).first()
    store_list = Stores.query.filter(Stores.id == my_product.store_id).all()
    if not my_product:
        abort(404)

    comment_form = CommentForm(product_id=my_product.id)
    return render_template('products/single_product.html', page_title=my_product.brand_full_string,
                           store_list=store_list, product=my_product, comment_form=comment_form)

@blueprint.route('/product/comment', methods=['POST'])
@login_required
def add_comment(user_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text.data, product_id=form.product_id.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен')                        
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в заполнении поля "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(get_redirect_target())