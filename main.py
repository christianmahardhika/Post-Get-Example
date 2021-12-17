from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/',methods=["GET"])
def default():
  return '[GET] /listSkincareRutinku \n\n [POST] /skinCareRutin'

@app.route('/listSkincareRutinku',methods=["GET"])
def list():
    products = [{
      "nama": "Daily Facial Cleanser",
      "merk": "CETAPHIL",
      "jenis": "Face Wash"
    },{
      "nama": "Snail Truecica Miracle Repair Serum",
      "merk": "Some By Me",
      "jenis": "Serum"
    },{
      "nama": "Mugwort Pore Clarifying Wash Off Pack",
      "merk": "Axis - Y",
      "jenis": "Masker Wajah"
    },]
    return jsonify(products)

@app.route('/skinCareRutin',methods=["POST"])
def create():
  request_data = request.json

  nama = request_data["nama"]
  merk = request_data["merk"]
  jenis = request_data["jenis"]
  
  response = '''nama skincare: {} \n
  merk skincare: {} \n
  jenis skincare: {} \n'''.format(nama,merk,jenis)
  return response


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)