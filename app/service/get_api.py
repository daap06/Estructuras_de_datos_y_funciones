
import requests

base_url = "https://reqres.in/api/users"

def get_all_users():
    users_data = {}

    # Obtener la primera página de usuarios
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        for usuario in data['data']:
            users_data[usuario['id']] = usuario
            # print(usuario)

    return users_data

# Obtener todos los usuarios
all_users = get_all_users()
# print(get_all_users())
# print(type(all_users[1]))

# Imprimir todos los usuarios
print(f"\n#################### Obtención de datos ########################\n")
for clave, valor in all_users.items():
    print(f"ID : {clave} - {valor}")
