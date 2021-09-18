import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>" \
           "<p>Otro párrafo.</p>"

@app.route('/listar', methods=['GET'])
def listar():
	return "<h1>LISTAR</h1>" \
           "<p>Párrafo de listar.</p>"

if __name__ == '__main__':
	app.run()
