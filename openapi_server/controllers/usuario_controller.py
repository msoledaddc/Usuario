import connexion
from typing import Dict
from typing import Tuple
from typing import Union

import requests

from openapi_server.models.contenido import Contenido  # noqa: E501
from openapi_server.models.login_usuario200_response import LoginUsuario200Response  # noqa: E501
from openapi_server.models.login_usuario_request import LoginUsuarioRequest  # noqa: E501
from openapi_server.models.perfil import Perfiles  # noqa: E501
from openapi_server.models.usuario import Usuarios  # noqa: E501
from openapi_server import util

from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, render_template, make_response

db = SQLAlchemy()

def import_db_controller(database):
    global db
    db = database


def add_favorito(id_usuario, nombre_perfil, body):  # noqa: E501
    """Añadir un nuevo contenido al listado de favoritos de un perfil específico de un usuario por su ID

    Añade un nuevo contenido al conjunto de contenidos multimedia favoritos de un perfil específico perteneciente a un usuario en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario al que se le añadirá un contenido a la lista de favoritos de uno de sus perfiles
    :type id_usuario: int
    :param nombre_perfil: nombre del perfil al que se le añadirá un contenido a su lista de favoritos
    :type nombre_perfil: str
    :param body: 
    :type body: int

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    return 'do some magic!'


def add_perfil(id_usuario, perfil):  # noqa: E501
    """Añadir un nuevo perfil a un usuario por su ID

    Añade un nuevo perfil a un usuario en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario al que se le añadirá un nuevo perfil
    :type id_usuario: int
    :param perfil: 
    :type perfil: dict | bytes

    :rtype: Union[Perfil, Tuple[Perfil, int], Tuple[Perfil, int, Dict[str, str]]
    """
    try:
    # Validar si la solicitud contiene datos JSON válidos
        if not connexion.request.is_json:
            return jsonify({"error": "Los datos enviados no están en formato JSON válido."}), 400

    # Obtener los datos del perfil desde la solicitud JSON
        data = connexion.request.get_json()

    # Verificar si el usuario existe
        usuario = Usuarios.query.get_or_404(id_usuario)
        if not usuario:
            return {"error": "Usuario no encontrado"}

    # Verificar que todos los campos requeridos están presentes
        required_fields = ['nombreperfil', 'favoritos']
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 422  # Código 422: Falta un campo requerido

    # Asignar los valores de los campos
        nombreperfil = data['nombreperfil']
        favoritos = data['favoritos']

    # Verificar si ya existe un perfil con el mismo nombre para este usuario
        if Perfiles.query.filter_by(nombreperfil=nombreperfil, idusuario=usuario.idusuario).first():
            return jsonify({"error": "Ya existe un perfil con este nombre para este usuario."}), 400

    # Crear el nuevo perfil
        nuevo_perfil = Perfiles(
            idusuario=usuario.idusuario,
            nombreperfil=nombreperfil,
            favoritosperfil=favoritos
        )

    # Guardar el perfil en la base de datos
        db.session.add(nuevo_perfil)
        db.session.commit()

    # Devolver la respuesta en formato JSON
        return jsonify(nuevo_perfil.to_dict()), 200  # Código 200: Perfil creado exitosamente
   
    except KeyError as e:
        # Manejar errores si faltan campos en la solicitud JSON
        return jsonify({'error': f'Falta el campo {e} en la solicitud'}), 400
    
    except Exception as e:
        # Manejar otros errores
        db.session.rollback()
        return jsonify({'error': str(e)}), 500




def add_usuario(usuario):  # noqa: E501
    """Añadir un nuevo usuario a la aplicación

    Crea una nueva cuenta en la aplicación que estará asociada a un nuevo usuario # noqa: E501

    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    try:
    # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos
    
    # Verificar que todos los campos requeridos están presentes
        required_fields = ['email', 'password', 'metodopago', 'status']
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 422  # Código 422: Falta un campo requerido

    # Validar los valores de 'metodopago' y 'status' (comprobamos si son válidos)
        valid_pago = ['tarjeta de credito', 'tarjeta virtual', 'tarjeta prepago', 'paypal']
        if data['metodopago'] not in valid_pago:
            return {"error": "Invalido metodo de pago. Metodos de pago validos: tarjeta de credito, tarjeta virtual, tarjeta prepago, paypal"}, 422  # Código 422: Metodo de pago no válido

        valid_status = ['activo', 'en suspension', 'pendiente de pago']
        if data['status'] not in valid_status:
            return {"error": "Invalido status. Status validos: activo, en suspension, pendiente de pago"}, 422  # Código 422: Status no válido

    # Asignar los valores de los campos
        email = data['email']
        password = data['password']
        metodopago = data['metodopago']
        status = data['status']

    # Crear el nuevo usuario
        new_usuario = Usuarios(
            email=email, 
            password=password, 
            metodopago=metodopago, 
            status=status,
            )

    # Guardar el usuario en la base de datos
        db.session.add(new_usuario)
        db.session.commit()

    # Retornar el usuario creado como diccionario
        return new_usuario.to_dict(), 200  # Código 200: Usuario creado exitosamente

    except Exception as e:
    # En caso de error, retornar un mensaje con detalles
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor


def delete_perfil(id_usuario, nombre_perfil):  # noqa: E501
    """Eliminar un perfil específico por su nombre

    Elimina un perfil específico de un usuario registrado en el sistema en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario del que se borrará el perfil
    :type id_usuario: int
    :param nombre_perfil: Nombre del perfil que se borrará
    :type nombre_perfil: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_usuario(id_usuario):  # noqa: E501
    """Eliminar un usuario específico por su ID

    Elimina un contenido multimedia específico de la aplicación en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a borrar
    :type id_usuario: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        # Asegurarse de que el ID proporcionado es un número entero
        id_usuario = int(id_usuario)
        
        # Buscar el usuario en la base de datos
        usuario = db.session.query(Usuarios).get(id_usuario)
        
        if usuario is None:
            # Si el usuario no se encuentra, devolver un error 404
            return jsonify({'error': 'Usuario no encontrado'}), 404

        # Eliminar el usuario de la sesión actual si estaba en otra sesión
        db.session.expunge(usuario)
        
        # Eliminar el usuario de la base de datos
        db.session.delete(usuario)
        db.session.commit()

        # Confirmar que el usuario fue eliminado correctamente
        return jsonify({'message': 'Usuario eliminado correctamente'}), 200


    except ValueError:
        # Devolver un error 400 si el ID proporcionado no es un número entero
        return jsonify({'error': 'ID inválido, debe ser un número entero'}), 400

    except Exception as e:
        # Capturar cualquier otro error y devolver un error 500 con detalles adicionales
        return jsonify({'error': f'Error en el servidor: {str(e)}'}), 500



def get_all_perfiles(id_usuario):  # noqa: E501
    """Obtener la lista de los perfiles asociados a un usuario por su ID

    Retorna el conjunto de perfiles asociados a un usuario específico de la aplicación en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrán sus perfiles
    :type id_usuario: int

    :rtype: Union[List[Perfil], Tuple[List[Perfil], int], Tuple[List[Perfil], int, Dict[str, str]]
    """
    perfiles = Perfiles.query.filter_by(idusuario=id_usuario).all()
    
    perfiles_favoritos = []
    for perfil in perfiles:
        favoritos = []
        for id in perfil.favoritosperfil:
            url = f'http://127.0.0.1:8080/contenido/{id}'
            response = requests.get(url)
            if response.status_code == 200:
                favoritos.append(response.json())
            else:
                print(f"Error al recuperar el contenido con id {id}: {response.status_code}")
        vistas_dict = {
            "idperfil": perfil.idperfil,
            "idusuario": perfil.idusuario,
            "nombreperfil": perfil.nombreperfil,
            "favoritosperfil": perfil.favoritosperfil,
            "favoritos": favoritos
        }
        perfiles_favoritos.append(vistas_dict)

    return perfiles_favoritos 


def get_all_usuarios():  # noqa: E501
    """Obtener la lista de usuarios registrados en la aplicación

    Retorna el conjunto de usuarios registrados en la aplicación # noqa: E501


    :rtype: Union[List[Usuario], Tuple[List[Usuario], int], Tuple[List[Usuario], int, Dict[str, str]]
    """
    usuarios = Usuarios.query.all()
    print(usuarios)
    usuarios_dict = [usuario.to_dict() for usuario in usuarios]

    return usuarios_dict


def get_contenido_favorito(id_usuario, nombre_perfil, contenido_favorito):  # noqa: E501
    """Obtener un contenido multimedia marcado como favorito de un perfil específico de un usuario

    Retorna un contenido multimedia perteneciente al listado de contenidos favoritos de un perfil específico perteneciente a un usuario en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrá el contenido de la lista de favoritos de uno de sus perfiles
    :type id_usuario: int
    :param nombre_perfil: nombre del perfil del que se obtendrá el contenido de su lista de favoritos
    :type nombre_perfil: str
    :param contenido_favorito: ID del contenido marcado como favorito que se obtendrá
    :type contenido_favorito: int

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    perfil = Perfiles.query.filter_by(nombreperfil=nombre_perfil, idusuario=id_usuario).first()
   
    url = f'http://127.0.0.1:8080/contenido/{contenido_favorito}'
    response = requests.get(url)
    if response.status_code == 200:
        contenido = response.json()
    else:
        print(f"Error al recuperar el contenido con id {contenido_favorito}: {response.status_code}")

    return contenido


def get_favoritos(id_usuario, nombre_perfil):  # noqa: E501
    """Obtener el listado de contenidos multimedia favoritos de un perfil específico de un usuario por su ID

    Retorna el conjunto de contenidos multimedia favoritos de un perfil específico perteneciente a un usuario en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrá la lista de favoritos de uno de sus perfiles
    :type id_usuario: int
    :param nombre_perfil: nombre del perfil del que se obtendrá su lista de favoritos
    :type nombre_perfil: str

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    perfil = Perfiles.query.filter_by(nombreperfil=nombre_perfil, idusuario=id_usuario).first()
    contenidos = []
    for id in perfil.favoritosperfil:
        url = f'http://127.0.0.1:8080/contenido/{id}'
        response = requests.get(url)
        if response.status_code == 200:
            contenidos.append(response.json())
        else:
            print(f"Error al recuperar el contenido con id {id}: {response.status_code}")

    return contenidos


def get_perfil(id_usuario, nombre_perfil):  # noqa: E501
    """Obtener un perfil específico por su nombre

    Retorna los datos de un perfil específico en función del identificador proporcionado del usuario # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrá el perfil
    :type id_usuario: int
    :param nombre_perfil: Nombre del perfil que se obtendrá
    :type nombre_perfil: str

    :rtype: Union[Perfil, Tuple[Perfil, int], Tuple[Perfil, int, Dict[str, str]]
    """
    perfil = Perfiles.query.filter_by(nombreperfil=nombre_perfil, idusuario=id_usuario).first()
    perfiles_dict = {
        "idperfil": perfil.idperfil,
        "idusuario": perfil.idusuario,
        "nombreperfil": perfil.nombreperfil,
        "favoritosperfil": perfil.favoritosperfil,
        "favoritos": get_favoritos(id_usuario, nombre_perfil)
    }

    return perfiles_dict


def get_usuario_by_id(id_usuario):  # noqa: E501
    """Obtener un usuario específico por su ID

    Retorna la información de un usuario en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a devolver
    :type id_usuario: int

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    usuario = Usuarios.query.get_or_404(id_usuario)
    print(usuario)
    usuario = usuario.to_dict()

    return usuario


def login_usuario(login_usuario_request):  # noqa: E501
    """Iniciar sesión en el sistema con la cuenta de un usuario

    Iniciar sesión en la aplicación a través de la cuenta de un usuario registrado utilizando su email y su password # noqa: E501

    :param login_usuario_request: 
    :type login_usuario_request: dict | bytes

    :rtype: Union[LoginUsuario200Response, Tuple[LoginUsuario200Response, int], Tuple[LoginUsuario200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        login_usuario_request = LoginUsuarioRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logout_usuario():  # noqa: E501
    """Cerrar sesión en el sistema con la cuenta de un usuario

    Cerrar la sesión de la cuenta de un usuario registrado con su email y su password en la aplicación # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_perfil(id_usuario, nombre_perfil, perfil):  # noqa: E501
    """Actualizar un perfil específico por su nombre

    Actualiza un perfil específico de un usuario registrado en el sistema en función del identificador proporcionado del usuario # noqa: E501

    :param id_usuario: ID del usuario del que se actualizará el perfil
    :type id_usuario: int
    :param nombre_perfil: Nombre del perfil que se actualizará
    :type nombre_perfil: str
    :param perfil: 
    :type perfil: dict | bytes

    :rtype: Union[Perfil, Tuple[Perfil, int], Tuple[Perfil, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        perfil = Perfiles.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_usuario(id_usuario, usuario):  # noqa: E501
    """Actualizar un usuario específico por su ID

    Actualiza la información de un usuario registrado en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a actualizar
    :type id_usuario: int
    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    try:     
        # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos
        
        # Buscar el usuario por su ID
        usuario = db.session.query(Usuarios).get(id_usuario)

        # Actualizar solo los campos que fueron enviados en el cuerpo de la solicitud
        if 'email' in data:
            usuario.email = data['email']
        if 'password' in data:
            usuario.password = data['password']
        if 'metodopago' in data:
            usuario.metodopago = data['metodopago']
        if 'status' in data:
            usuario.status = data['status']

        # Guardar los cambios en la base de datos
        # Eliminar el usuario de la sesión actual si estaba en otra sesión
        db.session.expunge(usuario)
        
        # Guardar el usuario en la base de datos
        db.session.add(usuario)
        db.session.commit()
        # Retornar el usuario actualizado como diccionario
        return usuario.to_dict(), 200  # Código 200: Usuario actualizado exitosamente

    except Exception as e:
        # Otro tipo de error
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor

