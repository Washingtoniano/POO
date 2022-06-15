from Palindromo import Palindromo
def test():
    lista=["Raul","Jamon","Monja","oso","radar","reconocer"]
    i=0
    while i< len (lista):
        print(lista[i])
        unpalindromo=Palindromo(lista[i])
        band=unpalindromo.esPalindromo()
        if band==True:
            print("Es palindromo")
        else:
            print("No es palindromo")
        #unpalindromo.setPalabra(lista[i+1])
        i=i+1
if __name__ == '__main__':
    res=input("Realizar test")
    if(str.lower(res)=='si'):
        test()
