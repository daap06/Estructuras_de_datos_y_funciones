import requests
from .get_api import get_all_users
base_url = "https://reqres.in/api/users"

all_users = get_all_users()

def crear_usuario(name, job):
    print(f"\n#################### Crear usuario ########################\n")
    payload =  {
        "name": name,
        "job": job,
    }
    # Realizar la solicitud POST con requests
    created_user = requests.post(base_url, json=payload)
    if created_user.status_code // 100 == 2:  # Verificar que la respuesta sea exitosa (código 2xx)
        print(created_user.json())
        return created_user.json()

    else:
        print("Error al crear el usuario.")
        return None

    
if __name__ == "__main__":
    crear_usuario( "Ignacio" ,"Profesor")
    # for clave, valor in create.items():
    #     print(f"ID : {clave} - {valor}")
    