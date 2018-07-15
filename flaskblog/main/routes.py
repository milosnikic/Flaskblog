from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    #posts = Post.query.paginate(),Post.query.paginate(per_page=5,page=2) items , to see attributes dir(posts)
    #posts = Post.query.all() #na ovaj nacin dobijamo sve postove
    page = request.args.get('page',1,type=int)#type int will raise ValueError if sb enters not int
    #Post.query.order_by(Post.date_posted.desc()) sortira po odredjenom argumentu desc() descending
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5) #proveru u browseru vrsimo unosom npr: localhost:5000/?page=3 
    return render_template('home.html',posts=posts,title='Home')


@main.route("/about")
def about():
    return render_template('about.html',title='About')
