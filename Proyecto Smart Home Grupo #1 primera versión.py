#SMARTHOME

usuariosRegistrados = 0 #Indica que existen 0 usuarios al indicio del programa
habitacionRegistrada= 0 #Indica que existen 0 habitaciones

menu= 1

while menu ==1:
    menu = int(input("1.Ingrese usuario\ n2.ingrese habitacion\ n3.Salir"))
    if menu ==1:
        correo = input("Ingrese su correo electronico:") #Nos pide que ingresemos el correo para registrarnos
        for usuario in range (1,usuariosRegistrados+1):
            if usuario [ "correo"] == correo:
                print("El correo ya esta en uso")
                break #si el usuario ingresa un correo ya registrador nos indicara que ya existe que debemos de ingresar uno nuevo

        pin = input("Ingrese su pin:") #Nos pide ingresar el pin
        usuariosRegistrados=("correo:",correo,"pin:",pin) #registra el correo y el pin establecido por el usuario en la base de datos
        print("Usuario registrado con exito")

        
        habitacion = input("agrega una nueva habitacion") #Nos pide que ingresemos la habitacion
        for habitacion2 in range (1,habitacionRegistrada+1):
            if habitacion2  ["habitacion"] == habitacion: #registra la habitacion establecida 
                print("La habitacion ya existe")
                break
        
        habitacionRegistrada=("habitacion:",habitacion) #registra la habitacion 
        print("habitacion registrada con existo")




