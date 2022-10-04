soda=10
water=10
lemonade=10
potato=10
choc=10
ice=10
profit=0

def payment1(money):
    global soda
    global profit
    
    if(money<2.5):
        print("PAY CORRECTLY!")
    
    elif(money==2.5):
        profit+=2.5
        soda-=1
        print("Successfully payed!")

    else:
        profit+=2.5
        soda-=1
        print("Successfully payed!\n"
        "Returning {}".format(money-2.5))

def payment2(money):
    global water
    global profit

    if(money<1):
        print("PAY CORRECTLY!")
    
    elif(money==1):
        profit+=1
        water-=1
        print("Successfully payed!")

    else:
        profit+=1
        water-=1
        print("Successfully payed!\n"
        "Returning {}".format(money-1))

def payment3(money):
    global lemonade
    global profit

    if(money<1.5):
        print("PAY CORRECTLY!")

    elif(money==1.5):
        profit+=1.5
        lemonade-=1
        print("Successfully payed!")

    else:
        profit+=1.5
        lemonade-=1
        print("Successfully payed!\n"
        "Returning {}".format(money-1.5))

def payment4(money):
    global potato
    global profit

    if(money<4):
        print("PAY CORRECTLY!")

    elif(money==4):
        profit+=4
        potato-=1
        print("Successfully payed!")

    else:
        profit+=4
        potato-=1
        print("Successfully payed!\n"
        "Returning {}".format(money-4))

def payment5(money):
    global choc
    global profit

    if(money<2):
        print("PAY CORRECTLY!")

    elif(money==2):
        profit+=2
        choc-=1
        print("Successfully payed!")

    else:
        profit+=2
        choc-=1
        print("Successfully payed!\n"
        "Returning {}".format(money-2))

def payment6(money):
    global ice
    global profit

    if(money<0.5):
        print("PAY CORRECTLY!")

    elif(money==0.5):
        profit+=0.5
        ice-=1
        print("Successfully payed!")

    else:
        profit+=0.5
        ice-=1
        print("Successfully payed!\n"
        "Returning {}".format(money-0.5))

def buy():
    while True:
        try:
            print("What do you want to buy?")
            code=(int(input("-> ")))
            if(code==1):
                global soda
                if(soda!=0):
                    print("One soda can costs $2,50\n"
                        "Insert the money")
                    money=float(input("-> "))
                    payment1(money)
                    break
                else:
                    print("Product unavailable")
            
            elif(code==2):
                global water
                if(water!=0):
                    print("One bottle of water costs $1\n"
                        "Insert the money")
                    money=float(input("-> "))
                    payment2(money)
                    break
                else:
                    print("Product unavailable")

            elif(code==3):
                global lemonade
                if(lemonade!=0):
                    print("One lemonade costs $1,50\n"
                        "Insert the money")
                    money=float(input("-> "))
                    payment3(money)
                    break
                else:
                    print("Product unavailable")

            elif(code==4):
                global potato
                if(potato!=0):
                    print("One bag of potato chips costs $4\n"
                        "Insert the money")
                    money=float(input("-> "))
                    payment4(money)
                    break
                else:
                    print("Product unavailable")

            elif(code==5):
                global choc
                if(choc!=0):
                    print("One chocolate bar costs $2\n"
                        "Insert the money")
                    money=float(input("-> "))
                    payment5(money)
                    break
                else:
                    print("Product unavailable")

            elif(code==6):
                global ice
                if(ice!=0):
                    print("One ice cream costs $4\n"
                        "Insert the money")
                    money=float(input("-> "))
                    payment6(money)
                    break
                else:
                    print("Product unavailable")

            else:
                print("Invalid value!\n"
                    "Try again...")

        except ValueError:
            print("Invalid value!\n"
                "Try again...")

def storage():
    while True:
        try:
            print("|-----STORAGE-----|\n"
                "|1- Check storage |\n"
                "|2- Add           |\n"
                "|3- Profit        |\n"
                "|4- Exit          |\n"
                "-------------------")
            op=int(input("-> "))
            if(op==1):
                global soda
                global water
                global lemonade
                global potato
                global choc
                global ice
                print("---------STORAGE---------\n"
                      "Items:      |Units:\n"
                      "Soda        |{}    \n"
                      "Water       |{}    \n"
                      "Lemonade    |{}    \n"
                      "Potato chips|{}    \n"
                      "Chocolate   |{}    \n"
                      "Ice cream   |{}".format(soda, water, lemonade, potato, choc, ice))
                print("-"*25)
                continue

            elif(op==2):
                print("What do you want to add?\n"
                    "1- Soda\n"
                    "2- Water\n"
                    "3- Lemonade\n"
                    "4- Potato chips\n"
                    "5- Chocolate\n"
                    "6- Ice cream")
                item=int(input("-> "))
                if(item==1):
                    print("How many units will be added?")
                    add=int(input("-> "))
                    soda+=add
                    print("Units successfully added!")

                elif(item==2):
                    print("How many units will be added?")
                    add=int(input("-> "))
                    water+=add
                    print("Units successfully added!")

                elif(item==3):
                    print("How many units will be added?")
                    add=int(input("-> "))
                    lemonade+=add
                    print("Units successfully added!")

                elif(item==4):
                    print("How many units will be added?")
                    add=int(input("-> "))
                    potato+=add
                    print("Units successfully added!")

                elif(item==5):
                    print("How many units will be added?")
                    add=int(input("-> "))
                    choc+=add
                    print("Units successfully added!")

                elif(item==6):
                    print("How many units will be added?")
                    add=int(input("-> "))
                    ice+=add
                    print("Units successfully added!")

            elif(op==3):
                global profit
                print("The total profit is ${}".format(profit))

            elif(op==4):
                break

            else:
                print("Invalid value!\n"
                    "Try again...")
                continue

        except ValueError:
            print("Invalid value!\n"
                  "Try again...")

def main():
    while True:
        try:
            print("--------Vending Machine--------\n"
                "|Code:         |Items:        |\n"
                "|      1       |Soda          |\n"
                "|      2       |Water         |\n"
                "|      3       |Lemonade      |\n"
                "|      4       |Potato chips  |\n"
                "|      5       |Chocolate     |\n"
                "|      6       |Ice cream     |\n"
                "-------------------------------\n"
                "0- Exit\n"
                "1- Buy")
            op=input("-> ")
            if(op=="1"):
                buy()
                continue
            
            elif(op=="0"):
                print("Finishing...")
                break

            elif(op=="123"):
                storage()
                continue
            
            else:
                print("Invalid value\n"
                      "Try again...")
                continue

        except ValueError:
            print("Invalid value\n"
                  "Try again...")

main()
