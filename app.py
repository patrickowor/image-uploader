import os 
from flask_wtf.file import FileField 
from flask_wtf import FlaskForm 
from wtforms import SubmitField, StringField 
from flask import Flask,  render_template, request,redirect

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class form(FlaskForm):
    file = FileField('file')
    type = StringField('type')
    submit= SubmitField('submit')
    
    

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LALALALALALALA'

@app.route('/')
def main():
    return render_template('my.html', form=form())
    
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static', 'image')
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        pass
        
    for file in request.files.getlist('file'):
       filename = file.filename
       # here I tried to see if I could add anyone form type
       type = request.form.get('type')
       print(filename)
       print(type)
       destination = '/'.join([target, filename])
       file.save(destination)

    return 'success'
        

if __name__ == '__main__':
    app.run(debug = True)