from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def app_home():
    return render_template('home.html', name='Hien Co Day', age='22')

@app.route('/<string:page_name>')
def home_page(page_name):
    return render_template(page_name)


def write_data(data):
    name = data['Name']
    email = data['Email']
    message = data['Message']
    with open('database.txt', mode='a') as database:
        database.write(f'\n{name},{email},{message}')

def write_data_csv(data):
    name = data['Name']
    email = data['Email']
    message = data['Message']
    with open('database.csv', newline='\n', mode='a') as database2:
        writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([name, email, message])

@app.route('/formsubmit', methods=['POST','GET'])
def form_submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            return redirect('/')
        except:
            return 'we have not save data to database ?'
    else:
        return "something went wrong. try again !"
