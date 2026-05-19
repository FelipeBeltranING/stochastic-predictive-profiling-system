# services/auth_service.py
from database.data_store import usuarios

def authenticate(username: str, password: str) -> dict:
    username = username.lower()
    if username not in usuarios:
        return {"success": False, "message": "Usuario no registrado"}
    
    user_data = usuarios[username]
    if user_data["password"] == password:
        user_info = {
            "nombre": user_data["nombre"],
            "perfil": user_data["perfil"]
        }
        return {"success": True, "message": "Login exitoso", "user": user_info}
    else:
        return {"success": False, "message": "Contraseña incorrecta"}