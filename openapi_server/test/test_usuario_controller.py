import unittest

from flask import json

from openapi_server.models.contenido import Contenido  # noqa: E501
from openapi_server.models.login_usuario200_response import LoginUsuario200Response  # noqa: E501
from openapi_server.models.login_usuario_request import LoginUsuarioRequest  # noqa: E501
from openapi_server.models.perfil import Perfil  # noqa: E501
from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUsuarioController(BaseTestCase):
    """UsuarioController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_favorito(self):
        """Test case for add_favorito

        Añadir un nuevo contenido al listado de favoritos de un perfil específico de un usuario por su ID
        """
        body = 56
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{nombre_perfil}/ListaFavoritos'.format(id_usuario=56, nombre_perfil='nombre_perfil_example'),
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_perfil(self):
        """Test case for add_perfil

        Añadir un nuevo perfil a un usuario por su ID
        """
        perfil = {"favoritosPerfil":[10,10],"nombrePerfil":"Marcos1"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/Perfiles'.format(id_usuario=56),
            method='POST',
            headers=headers,
            data=json.dumps(perfil),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_usuario(self):
        """Test case for add_usuario

        Añadir un nuevo usuario a la aplicación
        """
        usuario = {"metodoPago":"paypal","password":"password1","idUsuario":5,"perfilesUsuario":[{"favoritosPerfil":[10,10],"nombrePerfil":"Marcos1"},{"favoritosPerfil":[10,10],"nombrePerfil":"Marcos1"}],"email":"asee@gmail.com","status":"activo"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario',
            method='POST',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_perfil(self):
        """Test case for delete_perfil

        Eliminar un perfil específico por su nombre
        """
        headers = { 
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{nombre_perfil}'.format(id_usuario=56, nombre_perfil='nombre_perfil_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_usuario(self):
        """Test case for delete_usuario

        Eliminar un usuario específico por su ID
        """
        headers = { 
        }
        response = self.client.open(
            '/usuario/{id_usuario}'.format(id_usuario=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_perfiles(self):
        """Test case for get_all_perfiles

        Obtener la lista de los perfiles asociados a un usuario por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/Perfiles'.format(id_usuario=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_usuarios(self):
        """Test case for get_all_usuarios

        Obtener la lista de usuarios registrados en la aplicación
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contenido_favorito(self):
        """Test case for get_contenido_favorito

        Obtener un contenido multimedia marcado como favorito de un perfil específico de un usuario
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{nombre_perfil}/{contenido_favorito}'.format(id_usuario=56, nombre_perfil='nombre_perfil_example', contenido_favorito=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_favoritos(self):
        """Test case for get_favoritos

        Obtener el listado de contenidos multimedia favoritos de un perfil específico de un usuario por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{nombre_perfil}/ListaFavoritos'.format(id_usuario=56, nombre_perfil='nombre_perfil_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_perfil(self):
        """Test case for get_perfil

        Obtener un perfil específico por su nombre
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{nombre_perfil}'.format(id_usuario=56, nombre_perfil='nombre_perfil_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_usuario_by_id(self):
        """Test case for get_usuario_by_id

        Obtener un usuario específico por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}'.format(id_usuario=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_login_usuario(self):
        """Test case for login_usuario

        Iniciar sesión en el sistema con la cuenta de un usuario
        """
        login_usuario_request = openapi_server.LoginUsuarioRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/login',
            method='POST',
            headers=headers,
            data=json.dumps(login_usuario_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_usuario(self):
        """Test case for logout_usuario

        Cerrar sesión en el sistema con la cuenta de un usuario
        """
        headers = { 
        }
        response = self.client.open(
            '/user/logout',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_perfil(self):
        """Test case for update_perfil

        Actualizar un perfil específico por su nombre
        """
        perfil = {"favoritosPerfil":[10,10],"nombrePerfil":"Marcos1"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}/{nombre_perfil}'.format(id_usuario=56, nombre_perfil='nombre_perfil_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(perfil),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_usuario(self):
        """Test case for update_usuario

        Actualizar un usuario específico por su ID
        """
        usuario = {"metodoPago":"paypal","password":"password1","idUsuario":5,"perfilesUsuario":[{"favoritosPerfil":[10,10],"nombrePerfil":"Marcos1"},{"favoritosPerfil":[10,10],"nombrePerfil":"Marcos1"}],"email":"asee@gmail.com","status":"activo"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/usuario/{id_usuario}'.format(id_usuario=56),
            method='PUT',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
