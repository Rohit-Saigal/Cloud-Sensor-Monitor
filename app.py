from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

CO2 = 0
SO2 = 0
NO2 = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    co2 = request.args.get('CO2')
    so2 = request.args.get('SO2')
    no2 = request.args.get('NO2')

    global CO2
    global SO2
    global NO2

    CO2 = co2
    SO2 = so2
    NO2 = no2

    print("CO2:{} SO2:{} NO2:{}".format(CO2, SO2, NO2))

    return "CO2:{} SO2:{} NO2:{}".format(CO2, SO2, NO2)


@app.route('/get-data')
def get_data():
    resp = {"CO2": CO2,
            "SO2": SO2,
            "NO2": NO2}

    return jsonify(resp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)
