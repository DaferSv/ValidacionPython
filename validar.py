
print("========================================================================")
print(             "Bienvenido al Modulo de validacion de usuarios:"         )
print("========================================================================")
print("========================================================================")

def usuar(user):
    u=user 
    print("========================================================================")
    if len(u) < 6:
        print("El usuario ingresado no es valido debe de contener al menos 6 caracteres")
        print("========================================================================")
    elif len(u) > 12:
         print("El usuario ingresado no es valido, el maximo de caracteres permitidos es 12")
         print("========================================================================")
         
    elif u.isalnum()==False:
         print("El usuario ingresado no es valido, para que el usuario sea valido")
         print("debe de contener caractares alfanumericos tales como 'A-z' '0-9'")
         print("los caracteres especiales #$&/()=! y los espacios en blanco no son permitidos por favor intentelo de nuevo ")
         print("========================================================================")
    else :
        print("el usuario ingreado es valido y ha sido creado con exito")
    return 
