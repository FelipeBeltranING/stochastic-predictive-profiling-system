# services/auth_service.py
from database.data_store import usuarios

def authenticate(username: str, password: str) -> dict:
    """
    Args:
        username (str): Nombre de usuario (clave en el diccionario 'usuarios')
        password (str): Contraseña en texto plano

    Returns:
        dict: {
            "success": bool,
            "message": str,
            "user": dict (información del usuario sin contraseña) si éxito
        }
    """
    username = username.lower()
    if username not in usuarios:
        return {"success": False, "message": "Usuario no registrado"}
    
    user_data = usuarios[username]
    if user_data["password"] == password:
        # Devolver datos del usuario sin la contraseña
        user_info = {
            "nombre": user_data["nombre"],
            "perfil": user_data["perfil"]
        }
        return {"success": True, "message": "Login exitoso", "user": user_info}
    else:
        return {"success": False, "message": "Contraseña incorrecta"}