import requests
import json
from .get_api import get_all_users


base_url = "https://reqres.in/api/users"

def delete_user(user_id):
    print(f"\n#################### borrar usuario ########################\n")
    delete_url = f"{base_url}/{user_id}"
    # print(delete_url)
    response_new = requests.delete(delete_url)
    
    #print("datos eliminado", response_new)
    if response_new.status_code // 100 == 2:  # Verificar que la respuesta sea exitosa (código 2xx)
        print("Usuario eliminado exitosamente.", response_new)

    else:
        print("Error al eliminar el usuario.")
        
        
if __name__ == "__main__":
    delete_user(12)