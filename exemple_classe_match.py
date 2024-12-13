def suma():
        num1 = float(input("Introdueix el pirmer nombre: "))
        num2 = float(input("Introdueix el segon nombre: "))
        resultat = num1 + num2
        return resultat
    

def resta():
        num1 = float(input("Introdueix el pirmer nombre: "))
        num2 = float(input("Introdueix el segon nombre: "))
        resultat = num1 - num2
        return resultat
   

def multiplicacio():
        num1 = float(input("Introdueix el pirmer nombre: "))
        num2 = float(input("Introdueix el segon nombre: "))
        resultat = num1 * num2
        return resultat
    

def divisio():
        num1 = float(input("Introdueix el pirmer nombre: "))
        num2 = float(input("Introdueix el segon nombre: "))
        resultat = num1 / num2
        return resultat


def binari():
        num = input("Introdueix un nombre binari: ")
        decimal = int(num, 2)  
        print(f"El resultat de la conversió de {num} a decimal és: {decimal}")
        octal = oct(decimal)[2:]
        print(f"El resultat de la conversió de {num} a decimal és: {octal}")
        hexadecimal = hex(decimal)[2:]
        print(f"El resultat de la conversió de {num} a decimal és: {hexadecimal}")

        return decimal, octal, hexadecimal
        

def octal():
        num = input("Introdueix un nombre octal: ")
        decimal = int(num, 8)
        print(f"El resultat de la conversió de {num} a decimal és: {decimal}")
        binari = bin(decimal)[2:]
        print(f"El resultat de la conversió de {num} a binari és: {binari}")
        hexadecimal = hex(decimal)[2:]
        print(f"El resultat de la conversió de {num} a hexadecimal és: {hexadecimal}")

        return decimal, binari, hexadecimal


def decimal():
        num = int(input("Introdueix un nombre decimal: "))
        binari = bin(num)[2:]
        print(f"El resultat de la conversió de {num} a binari és: {binari}")
        octal = oct(num)[2:]
        print(f"El resultat de la conversió de {num} a octal és: {octal}")
        hexadecimal = hex(num)[2:]
        print(f"El resultat de la conversió de {num} a hexadecimal és: {hexadecimal}")

        return binari, octal, hexadecimal



def hexadecimal():
        num = input("Introdueix un nombre hexadecimal: ")
        decimal = int(num, 16)
        print(f"El resultat de la conversió de {num} a hexadecimal és: {decimal}")
        binari = bin(decimal)[2:]
        print(f"El resultat de la conversió de {num} a binari és: {binari}")
        octal = oct(decimal)[2:]
        print(f"El resultat de la conversió de {num} a octal és: {octal}")

        return decimal



while True:

        print("--------------------------------------------------")
        print("                      MENÚ")
        print("--------------------------------------------------")
        print("1. Operacions aritmètiques")
        print("2. Canvis de base")
        opcio = int(input("Introdueix quina operació vols fer: "))



                                
                                        
        match (opcio):
            case 1:
                print("--------------------------------------------------")
                print("                      MENÚ")
                print("--------------------------------------------------")
                print("1. Suma")
                print("2. Resta")
                print("3. Multipliacació")
                print("4. Divisió")
                opcio = int(input("Introdueix quina operació vols fer: "))
                match (opcio):
                    case 1:
                        print(f"El resultat de la suma és {suma()}")
                    case 2:
                        print(f"El resultat de la resta és {resta()}")
                    case 3:
                        print(f"El resultat de la multiplicació és {multiplicacio()}")
                    case 4:
                        print(f"El resultat de la divisió és {divisio()}")
                
            case 2:
                print("--------------------------------------------------")
                print("                      MENÚ")
                print("--------------------------------------------------")
                print("1. Binari")
                print("2. Octal")
                print("3. Decimal")
                print("4. Hexadecimal")
                opcio = int(input("Introdueix quina operació vols fer: "))
                match (opcio):
                    case 1:
                        binari()
                    case 2:
                        octal()
                    case 3:
                        decimal()
                    case 4:
                        hexadecimal()



