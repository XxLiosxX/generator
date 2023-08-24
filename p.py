import random
import string

def generar_correo():
    caracteres = string.ascii_letters + string.digits
    correo = ''.join(random.choice(caracteres) for _ in range(number_email))
    return correo

def generar_contrasena():
    caracteres = string.ascii_letters + string.digits + "!#$%&/()=?"
    contrasena = ''.join(random.choice(caracteres) for _ in range(number_password))
    return contrasena

def run():
    menu = """Bienvenido al generador de correo y contraseña
    1 - @gmail
    2 - @protonmail
    3 - @hotmail.com
    4 - @yahoo.com
    Elije una opción del (1 al 4): """
    opcion = int(input(menu))
    
    email_providers = {
        1: "@gmail.com",
        2: "@protonmail.com",
        3: "@hotmail.com",
        4: "@yahoo.com"
    }
    
    if opcion in email_providers:
        email_provider = email_providers[opcion]
        correo = generar_correo()
        print("Tu nuevo correo es:", correo + email_provider)
        resultado = "Correo: " + correo + email_provider
        contrasena = generar_contrasena()
        print("Tu nueva contraseña es:", contrasena)
        resultado1 = "Contraseña: " + contrasena
        
        file_name = "accounts_" + email_provider[1:].split(".")[0] + ".txt"
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(resultado + "\n")
            f.write(resultado1 + "\n")
    else:
        print("Opción inválida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    number_email = int(input('Ingrese el tamaño del email: '))
    number_password = int(input('Ingrese el tamaño de la contraseña: '))
    run()