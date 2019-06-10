from flask import render_template, flash, redirect, url_for, request
from ..models import User, BlogPost, Comment, Subscriber
from .. import db
from flask_login import login_required,current_user
from .forms import NewPostForm, EditPostForm, CommentForm, SubscribeForm
import markdown2
from . import user
from ..email import mail_message
from ..requests import get_random_quote

@user.route('/')
def homepage():
    title = 'Okasungora'
    recent_posts = BlogPost.query.order_by(BlogPost.postedAt.desc()).limit(5)
    all_posts = BlogPost.query.all()
    quote = get_random_quote()
    
    return render_template('user/user.html', title=title, recent_posts=recent_posts, all_posts=all_posts, quote=quote)



    

@user.route('/create_post', methods=['GET','POST'])
@login_required
def new_post():
    title='New Post'
    form = NewPostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data

        title = markdown2.markdown(title, extras=['code-friendly','fenced-code-blocks'])
        post = markdown2.markdown(post, extras=['code-friendly', 'fenced-code-blocks']) 

        blog_post = BlogPost(title=title, post=post, author=current_user.username)
        db.session.add(blog_post)
        db.session.commit()
        subscribers = Subscriber.query.all()
        for i in subscribers:
            mail_message("New Post", "user/new_blog_alert", i.email)
        return redirect(url_for('.homepage'))

    return render_template('user/new_post.html', form=form, title=title)

@user.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    posts = BlogPost.query.filter_by(author=uname).all()

    
    return render_template("user/profile.html", posts=posts, user=user)

@user.route('/edit/<int:id>', methods = ['GET',"POST"])
@login_required
def edit(id):
    title='edit'
    blog = BlogPost.query.filter_by(id=id).first()
    form = EditPostForm()
    if form.validate_on_submit():
        if form.title.data:
            blog.title = form.title.data
            db.session.add(blog)
            db.session.commit()

        if form.post.data:
            blog.post = form.post.data
            db.session.add(blog)
            db.session.commit()
            
        return redirect(url_for('.edit', id=blog.id))
    return render_template('user/edit.html', form=form, blog=blog)

@user.route('/delete/<int:id>')
@login_required
def delete_post(id):
    title='delete_post'
    blog = BlogPost.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('.profile', uname=current_user.username))

@user.route('/comment/<int:id>',methods=['GET','POST'])
def add_comment(id):
    title='comment'
    form=CommentForm()
    blog = BlogPost.query.filter_by(id=id).first()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        title = markdown2.markdown(title, extras=['code-friendly', 'fenced-code-blocks'])
        comment = markdown2.markdown(comment, extras=['code-friendly', 'fenced-code-blocks'])
        new_comment=Comment(title=title, comment=comment, comment_id=blog.id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.view_post', id=blog.id ))
    return render_template('user/comment.html', title=title, form=form )

@user.route('/view_post/<int:id>', methods=['GET',"POST"])
def view_post(id):
    single_post = BlogPost.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(comment_id=id).all()
    title="post"

    return render_template('user/single_post.html', single_post=single_post, comments=comments)


@user.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    title = "Subscribe"
    form = SubscribeForm()
    if form.validate_on_submit():
        if Subscriber.query.filter_by(email=form.email.data).first():
            flash('You are already subscribed')
        else:
            new_subscriber = Subscriber(email=form.email.data)
            db.session.add(new_subscriber)
            db.session.commit()
            email = form.email.data
            
            mail_message("Thank you for subscribing", "user/welcome", email)
            flash('Successfully subscribed!')
    
    return render_template('user/subscribe.html', form=form)
