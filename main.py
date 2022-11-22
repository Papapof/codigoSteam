from perfilclass import perfil

id = input("ingresa tu username: ")
email = input("ingresa tu email: ")
password = input("ingresa tu contraseña: ")

profile1 = perfil(1,id,email,password,"online","10")

profile1.print()

yn= input ("deseas cambiar la contraseña? (Y/N)")
if (yn == "y"):
        newpassword = input("Ingresa una nueva contraseña: ")
        newpassretry = input("Ingresa la contraseña de nuevo: ")
        if (newpassword == newpassretry):
            if (newpassword == password):
                print("incorrecto, contraseña es igual a la anterior")
            else:
                print("correcto")
                profile1newpass = perfil(1,id,email,newpassword,"online","10")
                profile1newpass.print()
        else:
            print("incorrecto, las contraseñas deben ser iguales")
