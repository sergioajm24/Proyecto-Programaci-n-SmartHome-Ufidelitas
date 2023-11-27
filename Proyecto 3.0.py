class Usuario:
    def __init__(self, correo, contraseña):
        self.correo = correo
        self.contraseña = contraseña

class Dispositivo:
    def __init__(self, nombre, estado_inicial, programacion_automatica=None):
        self.nombre = nombre
        self.estado = estado_inicial
        self.programacion_automatica = programacion_automatica

    def __str__(self):
        return f"Dispositivo: {self.nombre}, Estado: {self.estado}, Programación Automática: {self.programacion_automatica}"
    
class Cerradura:
    def __init__(self, nombre, estado, codigo_apertura):
        self.nombre = nombre
        self.estado = estado
        self.codigo_apertura = codigo_apertura

usuarios_registrados = []
cerraduras_registradas = []
cerraduras=[''] 
nombre=['']
estado=[''] 
codigo_apertura=['']
pin_actual=['']
nuevo_pin=['']


def menu():
    print ("Bienvenido al sistema")
    print("Por favor seleccione una de las siguientes opciones: ")
    opcion=input("1.Registrar usuario, 2.Registrar dispositivo, 3.Registrar cerradura, 4.Actualizar pin o digite 0 para salir, 5. Para iniciar sesion")
    if opcion=='1':
        print("Registro de usuario seleccionado")
        registrar_usuario()

    elif opcion=='2':
        print("Registro de dispositivo seleccionado")
        registrar_dispositivo()

    elif opcion=='3':
        print("Registro de cerradura seleccionado")
        registrar_cerradura(cerraduras, nombre, estado, codigo_apertura)

    elif opcion=='4':
        print("Actualizacion de pin seleccionado")
        actualizar_pin(cerraduras, nombre, pin_actual, nuevo_pin)

    elif opcion=='0':
        print("Saliendo del sistema")

    elif opcion=='5':
        print("Inicie sesion")
        inicio_sesion
        

def registrar_usuario():
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")

    # Verificamos si el usuario ya está registrado
    for correo in usuarios_registrados:
        if correo == correo:
            print("Este correo ya está registrado. Inicie sesión en lugar de registrarse.")
            menu()
            return

    nuevo_usuario = Usuario(correo, contraseña)
    usuarios_registrados.append(nuevo_usuario)
    print("Registro exitoso. Ahora puede iniciar sesión")
    menu()

def registrar_dispositivo():
    nombre = input("Ingrese el nombre del dispositivo: ")
    estado = input("Ingrese el estado inicial (encendido o apagado): ").lower()

    while estado not in ['encendido', 'apagado']:
        print("Por favor, ingrese un estado válido (encendido o apagado).")
        estado = input("Ingrese el estado inicial (encendido o apagado): ").lower()

    programacion_automatica = input("¿Desea configurar la programación automática? (si/no): ").lower()

    if programacion_automatica == 'si':
        programacion_automatica = input("Ingrese los detalles de la programación automática: ")
        print("Los datos deseados para la programacion son los siguientes: ", programacion_automatica)
        print("Datos guardados")

    nuevo_dispositivo = Dispositivo(nombre, estado, programacion_automatica)
    print("Dispositivo registrado:")
    print(nuevo_dispositivo)
    menu()
    return nuevo_dispositivo

def registrar_cerradura(cerraduras, nombre, estado, codigo_apertura):
    cerraduras=input("Digite su cerradura por favor: ")

    for cerraduras in cerraduras_registradas:
        if cerraduras == cerraduras:
            print("Esta cerradura ya es existente")
            menu()

    nueva_cerradura = Cerradura(nombre, estado, codigo_apertura)
    cerraduras_registradas.append(nueva_cerradura)
    print("Registro exitoso")
    menu()

def actualizar_pin(cerraduras, pin_actual, nuevo_pin):
    cerraduras=input("Digite su cerradura: ")
    for cerraduras in cerraduras_registradas:
        if cerraduras == cerraduras:
            pin_actual=input("Digite su pin: ")
            if pin_actual == pin_actual:
                nuevo_pin=input("Digite su nuevo pin: ")
                pin_actual=nuevo_pin
                print("El pin fue actualizado con exito")
                menu()
            else:
                print("PIN actual incorrecto. No se pudo actualizar.")
                menu()
            return
def inicio_sesion():
    correo=input("ingrese correo electronico:")
    contraseña=input("ingrese contraseña:")
    
    for usuario in usuarios_registrados:
        if usuario==usuario:
            print("Bienvenido, ha iniciado sesion")
        elif usuario!=correo:
            print("lo sentimos, el usuario no esta dentro del sistema, favor registrarse")

menu()
