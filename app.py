from flask import Flask, jsonify
import json

with open("api.json", "r") as json_api:
    datos_json = json.load(json_api)


app = Flask(__name__)

# Función requerida por la firma
def find_insert(lista):
    """
    find_n | Gael Flores | 2026-09-21
    Modified:
        2026-09-21 | inicial version | Gael Flores

    Params:
        lista int

    Returns:
        String
    """
    return f"Procesado: {lista}"


# Endpoint HTML principal
@app.route('/')
def inicio():
    print("Cambio")
    return datos_json["3D:RF:09:7F:00:01"]

@app.route('/json/<mac>')
def json_data(mac):
    print(datos_json[mac]["Name"])
    print(datos_json[mac]["Protocolos"])
    print(datos_json[mac]["status"])
    print(datos_json[mac]["VLANs"])
    print(datos_json[mac]["IP"])
    return datos_json[mac]["Name"]

# Función 1: Dispositivo Router Principal
@app.route('/server_1')
def server_1():
    # Se ejecuta la función internamente sin ensuciar la salida JSON
    find_insert(101)
    
    return jsonify({
        "101": {
            "Nombre": "Router Principal",
            "ip": "192.168.1.10",
            "Politica": "ALLOW_ALL",
            "Estado": "Activo"
        }
    })

# Función 2: Dispositivo Router
@app.route('/server_2')
def server_2():
    return jsonify({
        "102": {
            "Nombre": "Router",
            "ip": "192.168.1.20",
            "Politica": "ALLOW_ALL",
            "Estado": "Inactivo"
        }
    })

# Función 3: Dispositivo Switch
@app.route('/server_3')
def server_3():
    return jsonify({
        "103": {
            "Nombre": "Switch",
            "ip": "192.168.1.30",
            "Politica": "ALLOW_ALL",
            "Estado": "Activo"
        }
    })

# Función 4: Dispositivo Servidor principal
@app.route('/server_4')
def server_4():
    return jsonify({
        "104": {
            "Nombre": "Servidor principal",
            "ip": "192.168.1.40",
            "Politica": "ALLOW_ALL",
            "Estado": "Activo"
        }
    })

# Función 5: Impresora
@app.route('/server_5')
def server_5():
    return jsonify({
        "105": {
            "Nombre": "Impresora",
            "ip": "192.168.1.50",
            "Politica": "ALLOW_ALL",
            "Estado": "Inactivo"
        }
    })

# Función 6: Dispositivo (Firewall)
@app.route('/server_6')
def server_6():
    return jsonify({
        "106": {
            "Nombre": "Firewall Perimetral",
            "ip": "192.168.1.1",
            "Politica": "BLOCK_IP",
            "Estado": "Activo"
        }
    })

# Función 7: Dispositivo PC
@app.route('/server_7')
def server_7():
    return jsonify({
        "107": {
            "Nombre": "PC",
            "ip": "192.168.1.60",
            "Politica": "ALLOW_ALL",
            "Estado": "Activo"
        }
    })

# Función 8: Dispositivo TV
@app.route('/server_8')
def server_8():
    return jsonify({
        "108": {
            "Nombre": "TV",
            "ip": "192.168.1.70",
            "Politica": "ALLOW_ALL",
            "Estado": "Inactivo"
        }
    })

# Función 9: Dispositivo Cámara de seguridad
@app.route('/server_9')
def server_9():
    return jsonify({
        "109": {
            "Nombre": "Camara Seguridad IP",
            "ip": "192.168.1.80",
            "Politica": "ALLOW_ALL",
            "Estado": "Activo"
        }
    })

# Función 10: Dispositivo (Servidor Web)
@app.route('/server_10')
def server_10():
    return jsonify({
        "110": {
            "Nombre": "Servidor Web",
            "ip": "192.168.1.90",
            "Politica": "ALLOW_ALL",
            "Estado": "Activo"
        }
    })


if __name__ == '__main__':
    app.run(debug=True)