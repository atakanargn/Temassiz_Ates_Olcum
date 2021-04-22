from flask import redirect,jsonify,Flask, make_response,render_template,request,send_from_directory,url_for,json
from flask_cors import CORS
import RPi.GPIO as GPIO
from mlx90614 import MLX90614

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

thermometer_address = 0x5a
thermometer = MLX90614(thermometer_address)
arttir = 3

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
    insan, sicaklik = str(GPIO.input(channel)), thermometer.get_obj_temp()+arttir
    
    if(insan=="1"):
        data = {"sicaklik":float(sicaklik)}
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
