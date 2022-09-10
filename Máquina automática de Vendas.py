coca=10
fanta=10
pepsi=10
batata=10
choco=10
gelo=10
lucro=0
while True:
    print('-------Máquina de Vendas-------\n'
          '|Código:       |Produto:      |\n'
          '|       1      |Coca-cola     |\n'
          '|       2      |Fanta         |\n'
          '|       3      |Pepsi         |\n'
          '|       4      |Batatinha     |\n'
          '|       5      |Chocolate     |\n'
          '|       6      |Gelinho       |\n'
          '-------------------------------')
    print('0- Sair')
    print('1- Comprar')
    op= input('-> ')
    if(op=='1234'):
        somac= coca
        somaf= fanta
        somap= pepsi
        somab= batata
        somach= choco
        somag= gelo
        while True:
            print('-------ESTOQUE-------')
            print('Itens:    |Unidades:')
            print('Coca-Cola |{}'.format(coca))
            print('Fanta     |{}'.format(fanta))
            print('Pepsi     |{}'.format(pepsi))
            print('Batatinha |{}'.format(batata))
            print('Chocolate |{}'.format(choco))
            print('Gelinho   |{}'.format(gelo))
            print('-'*21)
            print('0- Sair')
            print('1- Adicionar ao Estoque')
            print('2- Lucro Total')
            estoque= input('-> ')
            if(estoque=='1'):
                print('O que deseja adicionar?')
                print('1- Coca-cola')
                print('2- Fanta')
                print('3- Pepsi')
                print('4- Batatinha')
                print('5- Chocolate')
                print('6- Gelinho')
                item= input('-> ')
                if(item=='1'):
                    unidades1= int(input('Quantas unidades serão adicionadas? '))
                    somac+=unidades1
                    coca+=unidades1
                    print('Unidades de Coca-cola: {} unidades.'.format(somac))
                elif(item=='2'):
                    unidades2= int(input('Quantas unidades serão adicionadas? '))
                    somaf+=unidades2
                    fanta+=unidades2
                    print('Unidades de Fanta: {} unidades.'.format(somaf))
                elif(item=='3'):
                    unidades3= int(input('Quantas unidades serão adicionadas? '))
                    somap+=unidades3
                    pepsi+=unidades3
                    print('Unidades de Pepsi: {} unidades.'.format(somap))
                elif(item=='4'):
                    unidades4= int(input('Quantas unidades serão adicionadas? '))
                    somab+=unidades4
                    batata+=unidades4
                    print('Unidades de Batatinha: {} unidades.'.format(somab))
                elif(item=='5'):
                    unidades5= int(input('Quantas unidades serão adicionadas? '))
                    somach+=unidades5
                    choco+=unidades5
                    print('Unidades de Choholate: {} unidades.'.format(somach))
                elif(item=='6'):
                    unidades6= int(input('Quantas unidades serão adicionadas? '))
                    somag+=unidades6
                    gelo+=unidades6
                    print('Unidades de Gelinho: {} unidades.'.format(somag))
            if(estoque=='2'):
                print('O lucro total é de R${}'.format(lucro))
            if(estoque=='0'):
                break
        print('Encerrando a operação...')
    if(op=='1'):
        nmr= int(input('O que gostaria de comprar? '))
        if(nmr==1):
            if(coca!=0):
                print('Uma Coca-cola vale R$3.50')
                pagamento= float(input('Insira o dinheiro: '))
                if(pagamento<3.5):
                    print('PAGUE CORRETAMENTE!')
                elif(pagamento>=3.5):
                    print ('Compra efetuada com sucesso!')
                    lucro+=3.5
                    coca-=1
                    print('Troco: R${}'.format(pagamento-3.5))
            else:
                print('PRODUTO INDISPONÍVEL!')
        elif(nmr==2):
            if(fanta!=0):
                print('Uma Fanta vale R$2')
                pagamento2= float(input('Insira o dinheiro: '))
                if(pagamento2<2):
                    print('PAGUE CORRETAMENTE!')
                elif(pagamento2>=2):
                    print('Compra efetuada com sucesso!')
                    lucro+=2
                    fanta-=1
                    print('Troco: R${}'.format(pagamento2-2.0))
            else:
                print('PRODUTO INDISPONÍVEL!')
        elif(nmr==3):
            if(pepsi!=0):
                print('Uma Pepsi vale R$1.99')
                pagamento3= float(input('Insira o dinheiro: '))
                if(pagamento3<1.99):
                    print('PAGUE CORRETAMENTE!')
                elif(pagamento3>=1.99):
                    print('Compra efetuada com sucesso!')
                    lucro+=1.99
                    pepsi-=1
                    print('Troco: R${}'.format(pagamento3-1.99))
            else:
                print('PRODUTO INDISPONÍVEL!')
        elif(nmr==4):
            if(batata!=0):
                print('Uma Batatinha vale R$3.50')
                pagamento4= float(input('Insira o dinheiro: '))
                if(pagamento4<3.5):
                    print('PAGUE CORRETAMENTE!')
                elif(pagamento4>=3.5):
                    print('Compra efetuada com sucesso!')
                    lucro+=3.5
                    batata-=1
                    print('Troco: R${}'.format(pagamento4-3.50))
            else:
                print('PRODUTO INDISPONÍVEL!')
        elif(nmr==5):
            if(choco!=0):
                print('Um Chocolate vale R$2')
                pagamento5= float(input('Insira o dinheiro: '))
                if(pagamento5<2):
                    print('PAGUE CORRETAMENTE!')
                elif(pagamento5>=2):
                    print('Compra efetuada com sucesso!')
                    lucro+=2
                    choco-=1
                    print('Troco: R${}'.format(pagamento5-2))
            else:
                print('PRODUTO INDISPONÍVEL!')
        elif(nmr==6):
            if(gelo!=0):
                print('Um Gelinho vale R$0.50')
                pagamento6= float(input('Insira o dinheiro: '))
                if(pagamento6<0.5):
                    print('PAGUE CORRETAMENTE!')
                elif(pagamento6>=0.5):
                    print('Compra efetuada com sucesso!')
                    lucro+=0.5
                    gelo-=1
                    print('Troco: R${}'.format(pagamento6-0.5))
            else:
                print('PRODUTO INDISPONÍVEL!')
    if(op=='0'):
        break
print('Encerrando a operação...')