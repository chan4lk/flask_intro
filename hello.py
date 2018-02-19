from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'index Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return 'do the login'

def show_the_login_form():
    return 'show the login form'

@app.route('/profiles/<username>')
def profile(username):  pass

@app.route('/hello', methods=['GET'])
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# with app.test_request_context('/login', method='POST'):
#    assert request.path == '/login'
#    assert request.method == 'POST'