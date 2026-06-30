usuarios = []

def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    while True:
        sexo = input("Ingrese sexo(F/M):  ").upper()
        if sexo == "M" or sexo == "F":
            return 
        print("Debe ingresar M o F solamente. Intente de nuevo.")

        contraseña = input("ingrese contraseña: ")

        if " " in contraseña:

            print("tiene espacios. no puede tener espacios")
        else:
            print("no tiene espacios")
        break

    usuarioos = {
        
        'nombre' = nombre
        'sexo' = sexo
        'contraseña' = contraseña
            
    }
    usuarioos.append(usuarios)






def  buscar_usuario():

  usuario = input("Ingrese usuario a buscar: ").strip().upper()
  if usuario in usuarios:
    sexo = usuarios[sexo]
    contraseña = usuarios[contraseña]

    print("El sexo del usuario es:", sexo,"y la contraseña es:",contraseña)

  else:

    print("Usuario no encontrado.")

def eliminar_usuario():
    print







def main():

    while True:
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        op = input("ingrese una opcion: ")
    
        if op == 1:
            ingresar_usuario()

        elif op == 2:
            buscar_usuario()

        elif op == 3:
            eliminar_usuario()

        elif op == 4:
            print("Programa terminado... ")
            break
        else:
            print("Debe ingresar una opción válida!!")