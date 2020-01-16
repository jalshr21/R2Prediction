from flask import request, Flask
from src.scripts import predict
from src.scripts import train


app = Flask(__name__)

@app.route('/get-prediction')
def query_example():
    language = request.args.get('text')
    ans = predict.predict([language])
    if ans[0] == 0:
        return "Not Relevant"
    elif ans[0] == 1:
        return "Relevant"
    else:
        return "Can't Say"

@app.route('/train-model')
def query_example_1():
    train.fit()
    return "Model trained"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


