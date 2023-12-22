# app.py (Flask backend)
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(_name_)

# Configure Flask Mail
app.config['MAIL_SERVER'] = 'your_mail_server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

# Dummy data for services and bookings
services = [
    {'id': 1, 'name': 'General Service Check-up'},
    {'id': 2, 'name': 'Oil Change'},
    {'id': 3, 'name': 'Water Wash'}
]

bookings = []

# Routes for bike station owner
@app.route('/owner/services', methods=['GET', 'POST'])
def manage_services():
    if request.method == 'POST':
        # Handle service creation/editing/deletion
        # ...

    return render_template('owner_services.html', services=services)

@app.route('/owner/bookings')
def view_bookings():
    return render_template('owner_bookings.html', bookings=bookings)

@app.route('/owner/bookings/<int:booking_id>')
def view_booking(booking_id):
    # View details of a specific booking
    # ...

@app.route('/owner/bookings/ready-for-delivery/<int:booking_id>')
def mark_ready_for_delivery(booking_id):
    # Mark booking as ready for delivery
    # Send email notification to customer
    # ...

@app.route('/owner/bookings/completed/<int:booking_id>')
def mark_completed(booking_id):
    # Mark booking as completed
    # ...

# Routes for customers
@app.route('/customer/register', methods=['GET', 'POST'])
def customer_register():
    if request.method == 'POST':
        # Handle customer registration
        # ...

    return render_template('customer_register.html')

@app.route('/customer/bookings', methods=['GET', 'POST'])
def customer_bookings():
    if request.method == 'POST':
        # Handle booking creation
        # ...

    return render_template('customer_bookings.html', services=services)

@app.route('/customer/bookings/<int:booking_id>')
def customer_view_booking(booking_id):
    # View details of a specific booking
    # ...

# Function to send email
def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)

if _name_ == '_main_':
    app.run(debug=True)







