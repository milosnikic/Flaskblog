from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
import logging

#
#
#       NEOPHODNA KONFIGURACIJA LOGGERA
#
#

#Kreiranje putanje za cuvanje logga
PATH = '/home/milos/Desktop/python_projects/Flask/flaskblog/logs/posts.log'

#Kreiranje loggera
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#Kreiranje FileHandlera za logger
file_handler = logging.FileHandler(PATH)
#Kreiranje formata za logger
formatter = logging.Formatter("%(asctime)s:%(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
#Podesvanje nivoa logovanja
file_handler.setLevel(logging.INFO)
#Dodavanje hendlera
logger.addHandler(file_handler)


posts = Blueprint('posts',__name__)

@posts.route("/post/new",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,author=current_user) #backref author veza koja nam omogucava da obezbedimo koji autor je pisao post
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        logger.info(f"[{current_user}] has CREATED post successfully")
        return redirect(url_for('main.home'))
    return render_template('create_post.html',title='New Post',form=form,legend='Create Post')

@posts.route("/post/<int:post_id>")#naznacavamo da je int
def post(post_id):
    post = Post.query.get_or_404(post_id) #get the post, if it doesnt exist return 404 (page does not exist)
    return render_template('post.html',title=post.title,post=post)

@posts.route("/post/<int:post_id>/update",methods=['GET','POST'])#naznacavamo da je int
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id) #get the post, if it doesnt exist return 404 (page does not exist)
    if post.author != current_user:
        logger.critical(f"[{current_user}] has tried to UPDATE {post.author}'s post")
        abort(403) #error response 403 forbidden route
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!','success')
        logger.info(f"[{current_user}] has UPDATED post successfully")
        return redirect(url_for('posts.post',post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',title='Update Post',
                            form=form,legend='Update Post')

@posts.route("/post/<int:post_id>/delete",methods=['POST','GET'])#naznacavamo da je int
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id) #get the post, if it doesnt exist return 404 (page does not exist)
    if post.author != current_user:
        logger.critical(f"[{current_user}] has tried to DELETE {post.author}'s post")
        abort(403) #error response 403 forbidden route
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!','success')
    logger.warning(f"[{current_user}] has DELETED post successfully")
    return redirect(url_for('main.home'))
