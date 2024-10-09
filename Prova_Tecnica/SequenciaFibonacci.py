numero = input("Digite um número maior que 0: ") #Declarando o numero a ser considerado.

def pertenceFibonacci(numero):  #Criando a função
     numero = int(numero)   #Transformando a String em um número
     a = 0
     b = 1

     if numero == a or numero == b:
        return f'O número {numero} pertence à sequência de Fibonacci.' #Retorno caso o numero fizer parte.

     proximo = a + b  #Soma os números

     while proximo <= numero: #Define o limite para que a sequencia vá
        if proximo == numero:
            return f'O número {numero} pertence à sequência de Fibonacci.'

        a = b
        b = proximo

        proximo = a + b

        return f'O número {numero} não pertence à sequência de Fibonacci.'

# Testando a função
print(pertenceFibonacci(numero))
