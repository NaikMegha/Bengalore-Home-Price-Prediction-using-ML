from flask import Flask, jsonify,request
import my_util as util

app = Flask(__name__)


@app.route("/get_location", methods=["POST", "GET"])
def get_location():
    response = jsonify(
        locations = util.get_location()
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price",methods=["POST","GET"])
def predict_home_price():
    if request.method == "POST":
        total_sqrt = float(request.form["total_sqft"])
        bhk = int(request.form["bhk"])
        bath = int(request.form["bath"])
        location = request.form["location"]
        response = jsonify(
            estimated_price = util.predict_house_price(total_sqrt,bhk,bath,location)
           #"Price of %s" %location.upper() +" is "+ str(util.predict_house_price(total_sqrt,bhk,bath,location))+" Lakhs"
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return  response




if __name__ == '__main__':
    print("Started Python Flask server for Home price prediction")
    app.run()


