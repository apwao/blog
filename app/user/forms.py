from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import Required

class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[Required()],render_kw={"placeholder":"title"})
    post = TextAreaField('Your Article',render_kw={"placeholder":"Write Post"})
    
    submit = SubmitField('Post')
class EditPostForm(FlaskForm):
    title= StringField('New title')
    post= TextAreaField('Write new post')
    submit= SubmitField('Save Changes')
class CommentForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    comment = TextAreaField('Comment')
    submit =SubmitField('Add Comment')

class SubscribeForm(FlaskForm):
    email = StringField('Your email address', validators=[Required()])
    submit = SubmitField('Subscribe')
