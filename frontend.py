
import requests

app = Flask(__name__)

# URL base de tu API
API_URL = 'http://localhost:5000/profesores'

@app.route('/')
def home():
    return '''
        <h1>Menú de Control Escolar</h1>
        <ul>
            <li><a href="/consultar">Consultar Profesores</a></li>
            <li><a href="/anadir">Añadir Profesor</a></li>
            <li><a href="/modificar">Modificar Profesor</a></li>
            <li><a href="/eliminar">Eliminar Profesor</a></li>
        </ul>
    '''

@app.route('/consultar', methods=['GET'])
def consultar():
    response = requests.get(API_URL)
    profesores = response.json()
    return jsonify(profesores)

@app.route('/anadir', methods=['POST'])
def anadir():
    data = request.json
    response = requests.post(f'{API_URL}/registrar', json=data)
    return jsonify(response.json())

@app.route('/modificar', methods=['PUT'])
def modificar():
    id = request.args.get('id')
    data = request.json
    response = requests.put(f'{API_URL}/modificar/{id}', json=data)
    return jsonify(response.json())

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    id = request.args.get('id')
    response = requests.delete(f'{API_URL}/eliminar/{id}')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=4000)
