# A good website for free HTML templates --> https://html5up.net/ and  http://www.mashup-template.com/templates.html
# I have downloaded and put that template in a desired folder and in that folder, I have created a template,
# and static folder and in template, I have put all the HTML files, and all css, JacaScript and assets,
# in static folder. Now, we just need to change all HTML paths according to our need.


from flask import Flask, render_template, request, redirect
import csv  # to store data

app = Flask(__name__)

@app.route("/")  # This / means we are on homepage.
def my_home():
    return render_template('index.html')

# @app.route("/index.html")
# def home():
#     return render_template('index.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

@app.route("/<string:page_name>")  # Short-cut for upper code.
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):  # Like this we can store our data after submission in a text file.
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

# But it is always better to store a database in form of a CSV file or an excel file.

def write_to_csv(data):  # Like this we can store our data after submission in a csv file.
    with open('database.csv', newline="", mode='a') as database2:  # newline to give new line after every entry.
        email = data['email']
        subject = data['subject']
        message = data['message']
        # This is just a writing convention, REMEMBER it.
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])  # Now, we gotta modilfy form in contact page, acc to this.
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # This will get our data in form of a dictionary.
            print(data)  # Just for me
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')  # To redirect to a different HTML, after submission.
        except:
            return "Did not saved to database."
    else:
        return 'Something went wrong, Please Try again!'

# Upper code copied from Flask (accessing request data) documentation.

# REMEMBER to give name attribute to each email, text and text-area. eg in email tag name='email'
# This is necessary to grab the information whatever user submits.

# Now, we have server and our browser on the same machine, only we can access this website (localhost)
# as we have server on this computer, to get it online, and make it available for everyone, we need to
# host it. And for that we are gonna use pythonanywhere website.
# Now we need to run a command (pip freeze > requirements.txt) this will create a requirement.txt folder
# in our folder (portfolio_website). Which will contain all the information of our virtual environment,
# and now we are gonna upload our portfolio_website on git-hub but not these virtual-environment
# files, instead we will simply upload requirements.txt in that place, then we will upload this 
# on pythonanywhere and the python anywhere will see requirements.txt and itself create those
# files of virtual environment.
