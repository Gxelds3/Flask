

network_config_2 = {
    "0001": {
        "ip": "192.168.0.2",
        "device": "Switch",
        "Policy": "Allow All",
        "status": False
    },  
    "0002": {
            "ip": "192.168.0.1",
            "device": "Router",
            "Policy": "Allow All",
            "status": True
        },
    "0003": {
            "ip": "192.168.0.3",
            "device": "Switch",
            "Policy": "Allow All",
            "status": False
        },
    "0004": {
            "ip": "192.168.0.4",
            "device": "Router",
            "Policy": "Allow All",
            "status": False
        },
    "0005": {
            "ip": "192.168.0.5",
            "device": "Switch",
            "Policy": "Allow All",
            "status": False,
            "lista": [1,4,6,0,8]
        },

}

#contenido = network_config_2.get("0005")
#listaA = contenido.get('lista')
#num = listaA[2]
#print(num)

print(network_config_2.get("0005").get("lista")[2])