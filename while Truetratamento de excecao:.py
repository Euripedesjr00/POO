while True:
    try:
        num = int (input("Digite um numero intero: "))
        resultado = 10/ num
        print (f"resultado da divisao: {resultado}")
        break
    except ZeroDivisionError:
        print ("Erro: Não é possivel dividir por zero.")
    except ValueError:
        print("Erro: DIgite um numero inteiro válido.")


#2-Leitura de arquivo que pode não existir#        
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
except FileNotFoundError:
    print("Arquivo não encontrado.")