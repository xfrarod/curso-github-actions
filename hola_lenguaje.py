import os

def main():
    nombre = os.getenv('USERNAME', 'usuario')
    lenguaje = os.getenv('LANGUAGE', 'lenguaje')

    print(f"Hola {nombre}, se que tu lenguaje favorito es: {lenguaje}")

if __name__ == "__main__":
    main()
