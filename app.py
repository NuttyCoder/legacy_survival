from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data storage (in-memory)
emergency_contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=emergency_contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        emergency_contacts.append({'name': name, 'phone': phone})
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/medical_instructions')
def medical_instructions():
    return render_template('medical_instructions.html')

@app.route('/survival_tips')
def survival_tips():
    return render_template('survival_tips.html')

@app.route('/offline_map')
def offline_map():
    return render_template('offline_map.html')

if __name__ == '__main__':
    app.run(debug=True)
