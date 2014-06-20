from flask import Flask, request, jsonify
from indifferent import app
from .store import Store
from .model import LogEntry

store = Store(app.config)

@app.route('/log/<key>', methods=['GET'])
def get_log(key=None):
    if key:
        # TODO get entire audit log for <key>
        value = store.read(key)
        dct = { key : value }
        return jsonify(dct)
    else:
        return abort(404)

@app.route('/log', methods=['POST'])
def log():
    payload = request.json

    key = payload.pop('key')
    message = payload.pop('message')
    status = payload.pop('http_status')
    # the envelope might or mightn't contain the key/value pair
    value = None
    try:
        _, value = payload.popitem()
    except:
        pass

    entry = LogEntry(message, status, key, value)
    store.log(entry)
    return "OK"
