from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Global list to store To Do items
# Each item will be a dictionary
todo_list = []

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task', '').strip()
    email = request.form.get('email', '').strip()
    priority = request.form.get('priority', '').strip()

    # Validation
    if not task:
        return redirect(url_for('index'))

    if not EMAIL_REGEX.match(email):
        return redirect(url_for('index'))

    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))

    # Add item to list
    todo_item = {
        'task': task,
        'email': email,
        'priority': priority
    }
    todo_list.append(todo_item)

    return redirect(url_for('index'))


@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)