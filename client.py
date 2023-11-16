#Biblioteca para trabalhar com o RPC
import xmlrpc.client

#Cria um proxy para o servidor RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

#Função para exibir menu de opções
def apresentacao():
    print("******************************")
    print("**   Escolha uma operação:  **")
    print("**      1. Somar            **")
    print("**      2. Subtrair         **")
    print("**      3. Multiplicar      **")
    print("**      4. Dividir          **")
    print("**      5. Sair             **")
    print("******************************")

while True:
    apresentacao()
    data = input("Opção: ")

    #Opção pra quebrar o loop
    if data == "5":
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    #Apartir do proxy procura a função 
    if data == "1":
        response = proxy.adicao(num1, num2)
    elif data == "2":
        response = proxy.subtracao(num1, num2)
    elif data == "3":
        response = proxy.multiplicacao(num1, num2)
    elif data == "4":
        response = proxy.divisao(num1, num2)
    else:
        print("Opção inválida!!")
        break

    print("Resultado: ", response)
