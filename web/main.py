from flask import redirect,jsonify,Flask, make_response,render_template,request,send_from_directory,url_for,json
from flask_cors import CORS
import RPi.GPIO as GPIO
from mlx90614 import MLX90614
from os import system
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

thermometer_address = 0x5a
thermometer = MLX90614(thermometer_address)
arttir = 3.7

app = Flask(__name__)
app.config['SECRET_KEY'] = '_2+)q(s^0j6fzdf+=qs$2i3dm5*t7m1yghvk3=hwn(i5c=9a1%'

CORS(app)
cors=CORS(app,ressources={
    r"/*": {
        "origins":"*"
    }
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/durum')
@app.route('/durum/')
def durum():
    for i in range(0,10):
        termoOlcum = thermometer.get_obj_temp()
        sleep(0.1)

    termoOlcum = float(str(termoOlcum))
    giden=0
    limitSwitch = GPIO.input(4)
    if(termoOlcum>32.0):
        giden=1
        arttir=4.1
    elif(termoOlcum>31.0):
        giden=1
        arttir=5.1
    elif(termoOlcum>30.0):
        giden=1
        arttir=6.1
    else:
        giden=0
    insan, sicaklik = str(giden), ("%0.1f"%(termoOlcum+arttir))

    if(insan=="1"):
        data = {"sicaklik":sicaklik}
    else:
        data = {"sicaklik":-1}

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response

# CSS / JS / IMAGE dosyalarına ulaşım için
@app.route('/<path:path>')
def send_dir(path):
    return send_from_directory('static/', path)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=3636, debug=True)
    finally:
        app.do_teardown_appcontext()
        print("SUNUCU KAPATILDI.")
