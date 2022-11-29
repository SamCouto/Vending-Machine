refri=10
agua=10
limao=10
batata=10
choco=10
picole=10
lucro=0

def pagamento(codigo):
    global refri
    global agua
    global limao
    global batata
    global choco
    global picole
    global lucro
    
    if(codigo==1):
        if(refri!=0):
            print("Uma lata de refrigerante custa R$3,50.")
            dinheiro=float(input("-> "))
            if(dinheiro<3.5):
                print("PAGUE CORRETAMENTE!")

            elif(dinheiro==3.5):
                lucro+=3.5
                refri-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Obrigado por ter comprado conosco!")

            else:
                lucro+=3.5
                refri-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Troco R${}.\n"
                    "Obrigado por ter comprado conosco!\n".format(dinheiro-3.5))

        else:
            print("Acabou o refrigerante!")

    elif(codigo==2):
        if(agua!=0):
            print("Uma garrafa de água custa R$4,50.")
            dinheiro=float(input("-> "))
            if(dinheiro<4.5):
                print("PAGUE CORRETAMENTE!")

            elif(dinheiro==4.5):
                lucro+=4.5
                agua-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Obrigado por ter comprado conosco!")

            else:
                lucro+=4.5
                agua-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Troco R${}.\n"
                    "Obrigado por ter comprado conosco!".format(dinheiro-4.5))

        else:
            print("Acabou a água!")

    elif(codigo==3):
        if(limao!=0):
            print("Uma garrafa de limonada custa R$2,99.")
            dinheiro=float(input("-> "))
            if(dinheiro<2.99):
                print("PAGUE CORRETAMENTE!")
            
            elif(dinheiro==2.99):
                lucro+=2.99
                limao-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Obrigado por ter comprado conosco!")

            else:
                lucro+=2.99
                limao-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Troco R${}.\n"
                    "Obrigado por ter comprado conosco!".format(dinheiro-2.99))

        else:
            print("Acabou a limonada!")

    elif(codigo==4):
        if(batata!=0):
            print("Um pacote de batatinhas custa R$5,00.")
            dinheiro=float(input("-> "))
            if(dinheiro<5):
                print("PAGUE CORRETAMENTE!")

            elif(dinheiro==5):
                lucro+=5
                batata-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Obrigado por ter comprado conosco!")

            else:
                lucro+=5
                batata-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Troco R${}.\n"
                    "Obrigado por ter comprado conosco!".format(dinheiro-5))

        else:
            print("Acabaram as batatinhas!")

    elif(codigo==5):
        if(choco!=0):
            print("Uma barra de chocolate custa R$2,50.")
            dinheiro=float(input("-> "))
            if(dinheiro<2.5):
                print("PAGUE CORRETAMENTE!")

            elif(dinheiro==2.5):
                lucro+=2.5
                choco-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Obrigado por ter comprado conosco!")

            else:
                lucro+=2.5
                choco-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Troco R${}.\n"
                    "Obrigado por ter comprado conosco!".format(dinheiro-2.5))

        else:
            print("Acabou o chocolate!")

    elif(codigo==6):
        if(picole!=0):
            print("Um picolé custa R$1,00.")
            dinheiro=float(input("-> "))
            if(dinheiro<1):
                print("PAGUE CORRETAMENTE!")

            elif(dinheiro==1):
                lucro+=1
                picole-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Obrigado por ter comprado conosco!")

            else:
                lucro+=1
                picole-=1
                print("Pagamento efetuado com sucesso!\n"
                    "Troco R${}.\n"
                    "Obrigado por ter comprado conosco!".format(dinheiro-1))

        else:
            print("Acabaram os picolés!")

def compras():
    while True:
        try:
            print("O que você gostaria de comprar?")
            codigo=int(input("-> "))
            if(codigo==1):
                pagamento(codigo)
                break

            elif(codigo==2):
                pagamento(codigo)
                break

            elif(codigo==3):
                pagamento(codigo)
                break

            elif(codigo==4):
                pagamento(codigo)
                break

            elif(codigo==5):
                pagamento(codigo)
                break

            elif(codigo==6):
                pagamento(codigo)
                break

            else:
                print("Valor inexistente!\n"
                    "Por favor, tente novamente!")

        except ValueError:
            print("Valor inexistente!\n"
                "Por favor, tente novamente!")

def estoque():
    global refri
    global agua
    global limao
    global batata
    global choco
    global picole
    print("-------ESTOQUE--------\n"
        "Items:      |Unidades:\n"
        "Refrigerante|{}\n"
        "Água        |{}\n"
        "Limonada    |{}\n"
        "Batatinha   |{}\n"
        "Chocolate   |{}\n"
        "Picolé      |{}\n"
        "----------------------".format(refri, agua, limao, batata, choco, picole))

def adicao(item):
    global refri
    global agua
    global limao
    global batata
    global choco
    global picole

    
    
    if(item==1):
        print("Quantas unidades serão adicionadas?")
        adicao=int(input("-> "))
        refri+=adicao
        print("Unidades adicionadas com sucesso!")

    elif(item==2):
        print("Quantas unidades serão adicionadas?")
        adicao=int(input("-> "))
        agua+=adicao
        print("Unidades adicionadas com sucesso!")

    elif(item==3):
        print("Quantas unidades serão adicionadas?")
        adicao=int(input("-> "))
        limao+=adicao
        print("Unidades adicionadas com sucesso!")

    elif(item==4):
        print("Quantas unidades serão adicionadas?")
        adicao=int(input("-> "))
        batata+=adicao
        print("Unidades adicionadas com sucesso!")

    elif(item==5):
        print("Quantas unidades serão adicionadas?")
        adicao=int(input("-> "))
        choco+=adicao
        print("Unidades adicionadas com sucesso!")

    elif(item==6):
        print("Quantas unidades serão adicionadas?")
        adicao=int(input("-> "))
        picole+=adicao
        print("Unidades adicionadas com sucesso!")

def painel_de_controle():
    while True:
        try:
            print("---Painel de Controle---\n"
                "|1- Checar o Estoque   |\n"
                "|2- Adicionar Produtos |\n"
                "|3- Lucro Total        |\n"
                "|4- Sair               |\n"
                "------------------------")
            op=int(input("-> "))
            if(op==1):
                estoque()

            elif(op==2):
                while True:
                    try:
                        print("Qual produto você gostaria de adicionar?\n"
                            "1- Refrigerante\n"
                            "2- Água\n"
                            "3- Limonada\n"
                            "4- Batatinha\n"
                            "5- Chocolate\n"
                            "6- Picolé")
                        item=int(input("-> "))
                        adicao(item)
                        break

                    except ValueError:
                        print("Algo saiu errado!\n"
                            "Por favor, tente novamente!")
                        continue

            elif(op==3):
                print("O lucro total é de R${}".format(lucro))
                continue

            elif(op==4):
                break

            else:
                print("Algo saiu errado!\n"
                "Por favor, tente novamente!")

        except ValueError:
            print("Algo saiu errado!\n"
                "Por favor, tente novamente!")

def main():
    while True:
        try:
            print("---Máquina de Vendas---\n"
                "|Produtos:   |Código: |\n"
                "|Refrigerante|    1   |\n"
                "|Água        |    2   |\n"
                "|Limonada    |    3   |\n"
                "|Batatinhas  |    4   |\n"
                "|Chocolate   |    5   |\n"
                "|Picolé      |    6   |\n"
                "-----------------------\n"
                "0- Sair\n"
                "1- Comprar")
            op=input("-> ")
            if(op=="1"):
                compras()
                continue

            elif(op=="0"):
                print("Obrigado por comprar conosco!\n"
                    "Finalizando a Operação...")
                break

            elif(op=="123"):
                painel_de_controle()
                continue

            else:
                print("Algo saiu errado!\n"
                    "Por favor, tente novamente!")
        
        except ValueError:
            print("Algo saiu errado!\n"
                "Por favor, tente novamente!")

main()
