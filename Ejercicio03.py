print("Sistema de autenticación avanzado con penalización")
intentos = 3
accesoConcedido = False
while intentos > 0:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    if usuario == "jose" and password == "70133":
        accesoConcedido = True
        break
    else:
        intentos -= 1
if accesoConcedido:
    print("\nAcceso concedido")
    print("\n1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")
else:
    print("\nACCESO BLOQUEADO")
