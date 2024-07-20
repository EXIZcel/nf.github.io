import os.path

import flask
from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_migrate import migrate, Migrate
from werkzeug.utils import secure_filename
from flask_admin import Admin
from data.articles import Article
from data.db_session import global_init, create_session
from flask_sqlalchemy import SQLAlchemy
from data.users import User
from flask_admin.contrib.sqla import ModelView
from forms.add_new import Add_NewForm
from forms.edit_profile import EditProfileForm
from forms.login import LoginForm
from forms.register import RegisterForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdsafs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sp2\db\blogs.db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
UPLOAD_FOLDER = os.getcwd() + '\\static\\img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
DEFAULT_IMAGE = '\static\img\default_image.jpg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_HOSTS = ['*']


@app.route('/profile/<int:id>', methods=['GET', 'POST'])
def profile(id):

        sess = create_session()
        user = sess.query(User).filter(User.id == id).first()

        context = {'title': 'Профиль', 'user': user, 'default_user_avatar': DEFAULT_IMAGE}
        return render_template('profile.html', **context)


@app.route('/f')
def index():
    sess = create_session()

    context = {'title': 'Главная', 'users': sess.query(User).all(),
               'default_user_avatar': DEFAULT_IMAGE}
    return render_template('index.html', **context)

@app.route('/obzor')
def obzor():
    return render_template('obzor.html')
@app.route('/')
def ind():
    return render_template('test2.html', title='Главная')


@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    sess = create_session()
    user = sess.query(User).filter(User.id == id).first()
    sess.delete(user)
    sess.commit()
    return redirect('/')

@app.route('/new')
def new():
    return render_template('new.html', title='Новости')

@app.route('/add_new')
def add_new():
    return render_template('add_new.html', title='Добаить')



@app.route('/product')
def product():
    return render_template('product.html', title='Товар')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        sess = create_session()
        user = sess.query(User).filter(email == User.email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect('/')
        else:
            return render_template('login.html', form=form, message='Неверный Логин или Пароль')
    return render_template('login.html', form=form, title='Авторизация')


@app.route('/testik')
def testik():
    return render_template('test_product.html',title='тестик')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/test')
def test():
    return render_template('test.html', title='Товар')


@app.route('/pred')
def pred():
    return render_template('pred.html', title='Предметы')

@app.route('/test2')
def test2():
    return render_template('test2.html', title='fds')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            return render_template('register.html', form=form, message='Пароль не совпадают', title='Регистрация')
        sess = create_session()
        if sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', form=form, message='Такой пользователь уже есть', title='Регистрация')
        user = User(email=form.email.data, name=form.name.data)
        user.set_password(form.password.data)
        sess.add(user)
        sess.commit()
        return redirect('/login')
    return render_template('register.html', form=form, title='Регистрация')


@app.route('/edit_profile', methods=['POST', 'GET'])
@login_required
def edit_profile():
    sess = create_session()
    user = sess.query(User).get(current_user.id)
    form = EditProfileForm()
    form.name.data = user.name
    if form.validate_on_submit():
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(UPLOAD_FOLDER + filename)
            user.image = filename
        user.name = form.name.data
        user.about = form.about.data
        sess.merge(user)
        sess.commit()
        return redirect(f'/profile/{current_user.id}')
    form.name.data = user.name
    form.about.data = user.about
    return render_template('edit_profile.html', form=form, title='Редактирование')



#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  username = db.Column(db.String(100), unique=True, nullable=False)
   # email = db.Column(db.String(120), unique=True, nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    #user = db.relationship('Role', backref=db.backref('users', lazy=True))


    #def __repr__(self):
     #   return f'<User {self.username}>'



#admin = Admin(app, name='MyApp Admin', template_mode='bootstrap4')
#admin.add_view(ModelView(User, db.session))


@login_manager.user_loader
def load_user(user_id):
    return create_session().query(User).get(user_id)





global_init('db/blogs.db')
app.run()