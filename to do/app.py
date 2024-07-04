import webbrowser
from datetime import datetime
from flask import redirect, request, url_for, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import TextAreaField, Form


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)




class ToDoForm(Form):
    name = TextAreaField('', name='main_form', render_kw={
        'placeholder': 'write the thing you wanna do here',

    })



# webview.create_window('REDD AXE TO DO APP', app, width=1500, height=1000)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime,
                             default=datetime.fromisoformat(
                                 datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def __repr__(self):
        return f'{self.task}'

@app.route('/', methods=['POST', 'GET'])
def index():

    to_dos = ToDo.query.order_by(ToDo.date_created).all()
    if request.method == 'POST':
        info = request.form['main_form']
        new_to_do = ToDo(task=info)

        try:
            db.session.add(new_to_do)
            db.session.commit()

            return redirect(url_for('index'))

        except Exception as e:
            print(f'there was an error\n{e}')

    return render_template('index.html', to_dos=to_dos)


@app.route('/settings')
def settings():
    to_do_form = ToDoForm()
    return render_template(
        'settings.html', to_do_form=to_do_form
    )


@app.route('/information')
def information():
    to_dos = ToDo.query.order_by(ToDo.date_created)
    return render_template('information.html', to_dos=to_dos)


@app.route('/delete/<int:to_do_id>', methods=["POST", "GET"])
def delete(to_do_id):
    try:
        to_be_deleted = ToDo.query.get_or_404(to_do_id)
        db.session.delete(to_be_deleted)
        db.session.commit()

        return redirect(url_for('index'))

    except Exception as e:
        return f'there  was an error\n{e}'


@app.route('/edit/<int:to_do_id>', methods=["POST", "GET"])
def edit(to_do_id):
    to_be_edited = ToDo.query.get_or_404(to_do_id)
    to_do_form = ToDoForm()

    if request.method == 'POST':
        to_be_edited.task = request.form['main_form']

        try:
            db.session.commit()
            return redirect(url_for('index'))

        except Exception as e:
            return f'there  was an error\n{e}'

    return render_template('edit.html', to_be_edited=to_be_edited, to_do_form=to_do_form)


if __name__ == '__main__':
    # webview.start()
    default_browser = webbrowser.WindowsDefault()
    default_browser.open('http://127.0.0.1:5000')
    app.run(debug=True)
