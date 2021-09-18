import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return "<h1>Proyecto GitHub V2</h1><p>Prueba de proyecto gestionado con GitHub.</p>"

@app.route('/listar', methods=['GET'])
def listar():
	return "<h1>LISTAR</h1>" \
           "<p>Párrafo de listar.</p>"

if __name__ == '__main__':
	app.run()
