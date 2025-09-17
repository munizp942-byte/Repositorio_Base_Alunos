arquivo=open("números.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()


def le_binario():
    try:
        with open("arquivo.txt", "r") as fs1:
            dados=fs1.read()
        with open("copia.txt", "w") as fs2:
            fs2.write(dados)
    except FileNotFoundError as e:
        print('arquivo nao existe! criando... -_-|||', e)
        arquivo = open("arquivo.txt", "w")
        arquivo.write("algo dentro!")
        arquivo.close()
    except IOError as e:
        print('deu algo errado @_@')
    print("OK! ~_~")
    le_binario()
    