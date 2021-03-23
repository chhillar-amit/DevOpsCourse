from flask import Flask
from flask import render_template

from todo_app.flask_config import Config
import todo_app.data.session_items as session_items
from flask import request, redirect
import cgi

app = Flask(__name__)
app.config.from_object(Config)

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

@app.route('/')
def index():
    #return 'Hello World!'   
    items = session_items.get_items()
    return render_template('index.html',items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    NewItem = request.form['title'] 
    print(NewItem)
    session_items.add_item(NewItem)

    return redirect("/")

@app.route('/form', methods=['GET'])
def show_form():
    return render_template('form.html')

@app.route('/update', methods=['GET'])
def update_form():
    return render_template('update.html')

@app.route('/update_item', methods=['POST'])
def update_item():
    ID = request.form['ID'] 
    print(ID)
    session_items.save_item(ID)

    return redirect("/")

@app.route('/save_item/<id>', methods=['GET'])
def save_item(id):
    item = session_items.get_item(id)
    item['status']='Completed'
    session_items.save_item(item)

    return redirect("/")

if __name__ == '__main__':
    app.run()
