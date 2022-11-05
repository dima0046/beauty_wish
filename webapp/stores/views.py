
from flask import abort, Blueprint, current_app, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required

from webapp.stores.models import Category, Comment, Products, Stores, Favorites
from webapp.db import db
from webapp.stores.forms import CommentForm
from webapp.utils import get_redirect_target


blueprint = Blueprint('products', __name__)

@blueprint.route('/', methods = ['GET', 'POST'])  # декоратор
@blueprint.route('/index', methods = ['GET', 'POST'])
@blueprint.route('/index/<int:page_num>', methods = ['GET', 'POST'])
def index(page_num=1):
    page_title = "Beauty Wish"
    hide_title = "main"
    hide_title2 = "main"
    product_list1 = Products.query.all()
    product_list = Products.query.paginate(per_page=12, page=page_num, error_out=False)
    category_list = Category.query.all()
    return render_template('products/index.html', page_title=page_title, product_list=product_list.items, 
    pages=product_list.iter_pages(left_edge=5), category_list=category_list, hide_title=hide_title, hide_title2=hide_title2)


@blueprint.route('/product/<int:product_id>')
def single_item(product_id):
    my_product = Products.query.filter(Products.id == product_id).first()
    similar_products = Products.query.filter(Products.brand_product.contains(my_product.brand_product)).all()
    common_list = []
    for prod in similar_products:
        store_list = Stores.query.filter(Stores.id == prod.store_id).first()
        row = {'store_id': store_list.id, 'store_name':store_list.name, 'price': prod.price, 'url': prod.url}
        common_list.append(row)
    if not my_product:
        abort(404)

    comment_form = CommentForm(product_id=my_product.id)
    return render_template('products/single_product.html', page_title=my_product.brand_full_string,
                           store_list=store_list, product=my_product, comment_form=comment_form, similar_products=similar_products, common_list=common_list)



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


@blueprint.route('/button/')  # декоратор
def add_to_favorite(product_id):
    product = Products.query.filter(Products.id == product_id).first()
    favorite_item = Favorites(product_id=product.id, user_id=current_user.id)
    db.session.add(favorite_item)
    db.session.commit()
    product_list = Products.query.all()
    page_title = "Beauty Wish"
    return render_template('products/index.html', page_title=page_title, product_list=product_list)


@blueprint.route('/category/<category_id>', methods = ['GET', 'POST'])
@blueprint.route('/category/<category_id>/<int:page_num>', methods = ['GET', 'POST'])
def get_category(category_id, page_num=1):
    page_title = "Beauty Wish"
    hide_title = "main"
    hide_title2 = "cat"
    product_list = Products.query.filter(Products.category == category_id).paginate(per_page=12, page=page_num, error_out=False)
    category_list = Category.query.all()
    current_category = Category.query.filter(Category.id == category_id).first()
    return render_template('products/index.html', page_title=page_title, product_list=product_list.items, 
    pages=product_list.iter_pages(left_edge=5), category_list=category_list, category=current_category.id, 
    category_name=current_category.name, hide_title=hide_title, hide_title2 = hide_title2)


