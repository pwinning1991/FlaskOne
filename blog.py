from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '0c38bfec65e63d30f16f21e391a4aabd'

posts = [
        {
            'author': 'Phil W',
            'title': 'Blog post 1',
            'content': 'First post content',
            'date_posted': 'APril 20, 2018',
            },
            {
            'author': 'Phil e',
            'title': 'Blog post 2',
            'content': 'Second post content',
            'date_posted': 'April 21, 2018',
            }
        ]

@app.route("/")
@app.route("/home")
def home():
    return  render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return  render_template('about.html', title="About")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
