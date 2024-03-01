import requests
from .get_api import get_all_users
base_url = "https://reqres.in/api/users"

def update_user(user_id, **updated_fields):


    print(f"\n#################### Actualizar usuario ########################\n")

    update_url = f"{base_url}/{user_id}"
    response = requests.put(update_url, json=updated_fields)

    if response.status_code // 100 == 2:
        updated_user = get_all_users()
        if user_id in updated_user.keys():
            dicc = updated_user[user_id].update({**updated_fields})
        else:
            print("No se accede al")

        print(f"Usuario actualizado: {updated_user[user_id]}")
        return updated_user
    else:
        print(f"Error al actualizar el usuario: {response.status_code}")
        return None


if __name__ == "__main__":
    update = update_user(2, first_name = "Morpheus", residense = "zion")
    for clave, valor in update.items():
        print(f"ID : {clave} - {valor}")