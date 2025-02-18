from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Folder where data will be stored within the container
DATA_FOLDER = "/data"

# Ensure the folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        name = request.form['name']
        age = request.form['age']
        country = request.form['country']
        
        # Store data in a text file within the container
        with open(os.path.join(DATA_FOLDER, 'user_data.txt'), 'a') as file:
            file.write(f"Name: {name}, Age: {age}, Country: {country}\n")
        
        return "Data saved successfully!"

    # HTML form to collect user data
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>User Info</title>
        </head>
        <body>
            <h1>Enter Your Information</h1>
            <form method="POST">
                <label>Name:</label><br>
                <input type="text" name="name" required><br><br>
                <label>Age:</label><br>
                <input type="number" name="age" required><br><br>
                <label>Country:</label><br>
                <input type="text" name="country" required><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
