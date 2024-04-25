def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def calculatrice():
    print("Bienvenue dans la meilleur calculatrice de votre vie !")
    while True:
        print("\nOptions disponibles:")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division (Work in progress)")
        print("5. Quitter")

        choix = input("Choisissez une opération (1/2/3/4/5) : ")

        if choix == '5':
            print("Revenez !!!")
            break

        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        if choix == '1':
            print("Résultat : ", addition(nombre1, nombre2))
        elif choix == '2':
            print("Résultat : ", soustraction(nombre1, nombre2))
        elif choix == '3':
            print("Résultat : ", multiplication(nombre1, nombre2))
        elif choix == '4':
            print("Résultat : ", division(nombre1, nombre2))
        else:
            print("Choix invalide. Veuillez choisir une option valide.")

calculatrice()