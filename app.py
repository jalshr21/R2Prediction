from flask import request, Flask
from flask_restplus import Api, Resource
from src.scripts import predict


flask_app = Flask(__name__)
app = Api(app=flask_app)
name_space = app.namespace('main', description='Main APIs')


@name_space.route("/get-prediction")
class MainClass(Resource):
    def get(self):
        language = request.args.get('text')
        ans = predict.predict([language])
        if ans[0] == 0:
            return "Not Relevant"
        elif ans[0] == 1:
            return "Relevant"
        else:
            return "Can't Say"


if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0')
