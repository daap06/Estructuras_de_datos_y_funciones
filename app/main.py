from service.get_api import get_all_users
from service.create import crear_usuario
from service.update import update_user
from service.delete import delete_user


def main():
    mi_post = {
    "id": 1,
    "email":"",
    "first_name": "",
    "last_name": "",
    "avatar": ""
}
        
    usuarios = get_all_users()
    
    crear_usuario( "Ignacio" ,"Profesor")

    update_user(2, first_name = "Morpheus", residense = "zion")
    
    delete_user(6)

if __name__ == "__main__":
    main()