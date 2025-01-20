from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK", "message": "Server is running"})

@app.route('/model/data', methods=['GET'])
def get_data():
    data = app.config['dataFunc']()
    return jsonify({"status": "OK", "Data": data})

def runServer(dataFunc):
    app.config['dataFunc'] = dataFunc
    app.run(debug=True)


if __name__ == '__main__':
    
    app.run(debug=True)