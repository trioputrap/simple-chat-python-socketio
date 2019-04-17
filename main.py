from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('new_user')
def handle_new_user(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('new_user_response', json, callback=messageReceived)

@socketio.on('new_msg')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('new_msg_response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)