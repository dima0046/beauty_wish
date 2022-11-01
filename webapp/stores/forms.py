from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.stores.models import Products

class CommentForm(FlaskForm):
    product_id = HiddenField('ID новости', validators=[DataRequired()])
    comment_text = StringField('Ваш отзыв', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

    def validate_product_id(self, product_id):
        if not Products.query.get(product_id.data):
            raise ValidationError('Продукт с таким id уже существует')