from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database2.csv', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message ])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(write_to_csv(data))
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try Again'

# @app.route('/submit_form', methods=['POST','GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Something went wrong. Try Again'
# @app.route('/browse.html')
# def browse():
#     return render_template('browse.html')

# @app.route('/details.html')
# def details():
#     return render_template('details.html')

# @app.route('/profile.html')
# def profile():
#     return render_template('profile.html')

# @app.route('/streams.html')
# def streams():
#     return render_template('streams.html')