palavra = input("Digite uma palavra: ") #Palavra a ser digitada pelo usuario

def ProcurarLetra(palavra):
    LetraMaiscula = "A"
    LetraMinuscula = "a"

    quantidade = palavra.count(LetraMinuscula) + palavra.count(LetraMaiscula) #Conta a quantidade de vezes que a letra foi usada

    if LetraMaiscula in palavra or LetraMinuscula in palavra: #Verifica se a palavra tem a letra A
        return(f"A palavra {palavra} tem a letra A, e ela se repete por {quantidade} vezes.")
    else:
        return(f"A palavra {palavra} não tem a letra A")


print(ProcurarLetra(palavra))