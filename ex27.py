def filtrar_paraules():
    for paraula in llista_de_paraules:
        llarg = len(paraula)
        if llarg > num:
            print(paraula)



llista_de_paraules = ["hola", "adéu", "gràcies", "si us plau", "bon dia", "bona tarda", "bona nit", "amics", "família", "alegria", "esperança", "pau", "amor", "llibre", "ciutat", "platja", "muntanya", "escola", "treball", "joc"]

num = int(input("Introduiex un número: "))

filtrar_paraules()
 