
from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from hangman import hangman_app, db
from hangman.forms import StartGameForm, HangmanCharGuess, LoginForm, RegistrationForm
from hangman.models import User
from games import Hangman

@hangman_app.route('/', methods=['GET','POST'])
@login_required
def hangman_home():
  if not current_user.is_authenticated:
    return redirect(url_for('login'))
  form = StartGameForm()
  print(form.errors)
  if form.submit.data:
    username = current_user.username
    return redirect(url_for('play_hangman'))
  return render_template('hangman_start.html', title='Hangman', form=form)

@hangman_app.route('/play_hangman', methods=['GET', 'POST'])
def play_hangman():
  if not current_user.is_authenticated:
    return redirect(url_for('login'))
  form = HangmanCharGuess()
  if form.validate_on_submit():
    print form.guess
  return render_template('hangman_game.html', title='Playing Hangman', username=current_user.username, form=form)


@hangman_app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('hangman_home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('hangman_home')
      return redirect(next_page)
  return render_template('login.html', title='Sign In', form=form)

@hangman_app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('hangman_home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

@hangman_app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('login'))

@hangman_app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  posts = [
      {'author': user, 'body': 'Test post #1'},
      {'author': user, 'body': 'Test post #2'}
      ]
  return render_template('user.html', user=user, posts=posts)

