import xmlrpc.server

#Funções de cálculo
def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Erro: Divisão por zero!!"
    return n1 / n2

#Cria o servidor RPC
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
print("Servidor em operação!! Aguardando conexões...")

#Registra as funções
server.register_function(adicao, "adicao")
server.register_function(subtracao, "subtracao")
server.register_function(multiplicacao, "multiplicacao")
server.register_function(divisao, "divisao")

#Inicia o servidor
server.serve_forever()
