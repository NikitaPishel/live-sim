from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dev/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK", "message": "Server is running"})

@app.route('/model/data', methods=['GET'])
def get_data():
    data = app.config['dataFunc']()
    return jsonify({"data": data})

@app.route('/client/sign', methods=['GET'])
def get_user():
    pass

def runServer(dataFunc):
    app.config['dataFunc'] = dataFunc
    app.run(debug=True)


if __name__ == '__main__':
    
    app.run(debug=True)