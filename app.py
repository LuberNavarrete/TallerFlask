from flask import Flask
import logging
app = Flask(__name__)

logging.basicConfig(filename = "taller.log", format = '%(asctime)s %(message)s', filemode = 'w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route("/")
def inicio():
	logger.info ("App Home")
	return "<h1>Diplomado Cyberseguridad</h1><p>Bienvenido al modulo de desarrollo Seguro</p>"

@app.route("/cal/sum/<int:val1>/<int:val2>")
def val_suma(val1, val2):
	resul = val1 + val2
	resp =  "<p>El resultado es: {}</p>".format(resul)
	logger.info("Val1: {} + Val2: {} = {}".format(val1, val2, resp))
	return resp

@app.route("/cal/sus/<int:val1>/<int:val2>")
def val_sus(val1, val2):
	resul = val1 - val2
	resp =  "<p>El resultado es: {}</p>".format(resul)
	logger.info("Val1: {} - Val2: {} = {}".format(val1, val2, resp))
	return resp

@app.route("/cal/pro/<int:val1>/<int:val2>")
def val_pro(val1, val2):
	resul = val1 * val2
	resp =  "<p>El resultado es: {}</p>".format(resul)
	logger.info("Val1: {} x Val2: {} = {}".format(val1, val2, resp))
	return resp

@app.route("/cal/div/<int:val1>/<int:val2>")
def val_div(val1, val2):
	try:
		resul = val1 / val2
		resp =  "<p>El resultado es: {}</p>".format(resul)
		logger.info("Val1: {} / Val2: {} = {}".format(val1, val2, resp))
		return resp
	except:
		logger.info("Ha ocurrido un error")
		return "<p>Ha ocurrido un error</p>"		
