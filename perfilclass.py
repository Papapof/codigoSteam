class perfil:
    # username= ""
    # email= ""
    # password = ""
    def __init__(self,id,username,email,password,status,level=0):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.level = level

    def print(self):
        print("El id es: "+str(self.id))
        print("El username es: "+str(self.username))
        print("El email es: "+str(self.email))
        print("La contraseña es: "+str(self.password))
        print("El estado es: "+str(self.status))
        print("El nivel es: "+str(self.level))
