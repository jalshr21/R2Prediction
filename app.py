from flask import request, Flask
from R2Prediction.src.scripts import predict

app = Flask(__name__)

@app.route('/get-prediction')
def query_example():
    language = request.args.get('text')
    return predict.predict([language])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


