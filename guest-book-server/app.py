from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/messages', methods=['GET'])
def list_messages():
    messages = []
    return jsonify(messages)


if __name__ == '__main__':
    app.run()
