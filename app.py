from flask import Flask, render_template, Blueprint, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

app = create_app()


# HTMX endpoint for sending a message
@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.form.get('message', '').strip()
    if not message:
        return '', 204
    return render_template('message.html', message=message)
