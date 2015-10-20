from flask import Flask,Response
app = Flask(__name__)

@app.route("/")
def html():
	return """
	<html>
	<head>
	<link rel="stylesheet" type="text/css" href="static/estilo.css">
	</head>
	<body>
	<p>Esto es una pagina con estilo css</p>
	<p><img SRC="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Sasso_lungo_da_passo_pordoi.jpg/270px-Sasso_lungo_da_passo_pordoi.jpg"</p>
	</body>
	</html>
	"""
@app.route('/imagen')
def jpeg():
    response = Response()
    response.headers.add('Content-Type', 'image/png')
    archivo = open("./static/tiger.png", "rb") 
    contenido = archivo.read()
    response.set_data(contenido);   # Datos binarios
    return response
if __name__ == "__main__":
    app.run(debug=True)