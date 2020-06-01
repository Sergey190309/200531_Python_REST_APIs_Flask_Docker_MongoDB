from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if "x" not in postedData or "y" not in postedData:
        return 301
    elif type(postedData["x"]) != int or type(postedData["y"]) != int:
        return 302

    if functionName == 'div' and postedData["y"] == 0:
        return 303
    else:
        return 200


def processData(postedData, functionName):
    # Verify posted data validity.
    status_code = checkPostedData(postedData, functionName)
    if status_code == 200:
        x = postedData["x"]
        y = postedData["y"]
        # insure they are integers.
        x = int(x)
        y = int(y)
        # Make result
        if functionName == 'add':
            ret = x + y
        elif functionName == 'sub':
            ret = x - y
        elif functionName == 'mul':
            ret = x * y
        elif functionName == 'div':
            ret = x / y
    elif status_code == 301:
        ret = 'Error, argument is missing'
    elif status_code == 302:
        ret = 'Error, arguments are not ints'
    elif status_code == 303:
        ret = 'Error, division by 0, are you idiot?'

    # generate return value
    retJSON = {
        "Message": ret,
        "Status code": status_code
    }
    return retJSON


class Add(Resource):
    def post(self):
        # Step 1 - get posted data.
        postedData = request.get_json()
        retJSON = processData(postedData, 'add')
        return jsonify(retJSON)

    def get(self):
        return "It was get."

    def put(self):
        pass

    def delele(self):
        pass


class Sub(Resource):
    def post(self):
        # Step 1 - get posted data.
        postedData = request.get_json()
        retJSON = processData(postedData, 'sub')
        return jsonify(retJSON)

    def get(self):
        return "It was get."

    def put(self):
        pass

    def delele(self):
        pass


class Mul(Resource):
    def post(self):
        # Step 1 - get posted data.
        postedData = request.get_json()
        retJSON = processData(postedData, 'mul')
        return jsonify(retJSON)

    def get(self):
        return "It was get."

    def put(self):
        pass

    def delele(self):
        pass


class Div(Resource):
    def post(self):
        # Step 1 - get posted data.
        postedData = request.get_json()
        retJSON = processData(postedData, 'div')
        return jsonify(retJSON)

    def get(self):
        return "It was get."

    def put(self):
        pass

    def delele(self):
        pass


api.add_resource(Add, "/add")
api.add_resource(Sub, "/sub")
api.add_resource(Mul, "/mul")
api.add_resource(Div, "/div")


@app.route('/')
def hello_world():
    return 'Hi there!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run(host="127.0.0.1", port=80)
