def vocal():
    if lletra in vocals:
        return (f"{lletra} és una vocal")
    else:
        return (f"{lletra} no és una vocal")


lletra = input("Introduiex una lletra: ").lower()
vocals = "aeiou"

print(vocal())