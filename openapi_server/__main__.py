#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy

from openapi_server.models.usuario import import_db_usuario
from openapi_server.models.perfil import import_db_perfil
from openapi_server.models.contenido import Contenido
from openapi_server.models.temporadas_inner import TemporadasInner
from openapi_server.models.episodios_inner import EpisodiosInner
from openapi_server.models.login_usuario200_response import LoginUsuario200Response
from openapi_server.models.login_usuario_request import LoginUsuarioRequest

from openapi_server.controllers.usuario_controller import import_db_controller

from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./openapi/')
CORS(app.app)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Microservicio de Usuarios de una aplicación de tipo Netflix'},
            pythonic_params=True)

app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/Usuarios'
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#esto es para que no se caiga a las 10 requests
app.app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 30,        # Tamaño máximo de conexiones en el pool
    'pool_timeout': 30,     # Tiempo máximo de espera para obtener una conexión
    'pool_recycle': 180,   # Tiempo máximo de vida de una conexión (en segundos)
    'max_overflow': 5       # Conexiones extra que pueden crearse si se alcanza el pool_size
}

db = SQLAlchemy(app.app)

import_db_controller(db)
import_db_usuario(db)
import_db_perfil(db)

app.run(port=8081)




# def main():
#     app = connexion.App(__name__, specification_dir='./openapi/')
#     app.app.json_encoder = encoder.JSONEncoder
#     app.add_api('openapi.yaml',
#                 arguments={'title': 'Microservicio de Usuarios de una aplicación de tipo Netflix'},
#                 pythonic_params=True)

#     app.run(port=8080)


# if __name__ == '__main__':
#     main()
