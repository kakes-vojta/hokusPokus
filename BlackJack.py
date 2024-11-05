import random
balance = 100
obnos = int(input(f"Váš zůstatek je: {balance}💲, zde napište za kolik chcete hrát:"))
prohra = - (obnos)
vyhra = + (obnos)
hodnoty = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
counter = 0
counter_sum = 0
eso = False
vzhled = "♠"
pocet_hitu_hrace = 0
pocet_hitu_dealera = 0

def dealeruv_tah():
    global balance, obnos, prohra, vyhra, karty_dealera, karty_hrace, pocet_hitu_hrace, pocet_hitu_dealera, vzhled, eso, karta
    nova_karta_dealer = random.choice(hodnoty)

    karta = hodnota_karty(nova_karta_dealer)
    eso = False
    if karta == 11:
        eso = True

    while karty_dealera < karty_hrace and karty_hrace <= 21 and pocet_hitu_dealera < 6 or karty_dealera == karty_hrace and karty_dealera < 17 and pocet_hitu_dealera < 6: 
        nova_karta_dealer = random.choice(hodnoty)
        nova_karta_dealer1 = (f"{nova_karta_dealer}{vzhled}")
        ruka_dealera.append(nova_karta_dealer1)
        karty_dealera += hodnota_karty(nova_karta_dealer)
        pocet_hitu_dealera += 1
        if karty_dealera > 21 and eso == True:
            karty_dealera -= 10
            eso = False
        continue

    while karty_dealera == karty_hrace and karty_dealera >= 17:
        pocet_hitu()
        pocet_hitu_hrace = 0
        pocet_hitu_dealera = 0
        break
    while karty_dealera > 21 and eso == False:
        pocet_hitu()
        pocet_hitu_hrace = 0
        pocet_hitu_dealera = 0
        break
    while karty_dealera > karty_hrace and karty_dealera <= 21:
        pocet_hitu()
        pocet_hitu_hrace = 0
        pocet_hitu_dealera = 0
        break
        

def pocet_hitu():
    global ruka_hrace, ruka_dealera, karty_hrace, karty_dealera
    print("---------")
    print(f"Dealerova ruka: {ruka_dealera}\nDealerovo skóre:{karty_dealera}")
    print("---------")
    print(f"Tvoje ruka: {ruka_hrace}\nTvoje skóre:{karty_hrace}")
    print("---------")
    porovnaniKaret(karty_hrace, karty_dealera)
    print("------------")
        
def hodnota_karty(karta):
    global eso
    if karta in ["J", "Q", "K"]:
        cisloKarty = 10
    elif karta == "A":
        eso = True
        cisloKarty = 11 
    elif karta in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        cisloKarty = int(karta)
    return(cisloKarty)

def porovnaniKaret(x,y):
    global balance, vyhra, prohra
    if x == y:
        print(f"⏸ Remíza!\nZůstatek: {balance}💲")
    elif x > 21:
        balance += prohra
        print(f"❌ Prohrál jsi: {prohra}\nZůstatek: {balance}💲")
    elif y > 21:
        balance += vyhra
        print(f"✅ Vyhrál jsi: {vyhra}\nZůstatek: {balance}💲")
    elif x > y and x <= 21:
        balance += vyhra
        print(f"✅ Vyhrál jsi: {vyhra}\nZůstatek: {balance}💲")
    elif x < y and y <= 21:
        balance += prohra
        print(f"❌ Prohrál jsi: {prohra}\nZůstatek: {balance}💲")

while balance < 100000000:
    deck1 = random.choice(hodnoty)
    deck2 = random.choice(hodnoty)
    deck3 = random.choice(hodnoty)
    deck4 = random.choice(hodnoty)
    nova_karta = random.choice(hodnoty)
    
    ruka_hrace = [f'{deck3}{vzhled}, {deck4}{vzhled}']
    ruka_dealera = [f'{deck1}{vzhled}, {deck2}{vzhled}']

    karty_dealera = (hodnota_karty(deck1) + hodnota_karty(deck2))
    karty_hrace = (hodnota_karty(deck3) + hodnota_karty(deck4))

    if obnos > balance and balance > 0:
        print("Nedostatek prostředků")
        obnos = int(input(f"Váš zůstatek je {balance}💲 zde napište za kolik chcete hrát:"))
    elif balance <= 0:
            print("Došly vám peníze, nemůžete nadále hrát")
            exit()
    elif balance > 0 and karty_hrace < 21 or balance > 0 and karty_dealera < 21:
        pokracovat = input("Chcete si zahrát? (H):") 

    if pokracovat.upper() == ("H"):
        print(f"---------\nHELP MENU:\nENTER = Hrát\nx = Odejít\nS = Změna vzhledu\nB = Změna částky, se kterou budete hrát\nhráli jste: {counter} krát, za: {counter_sum}💲\nVáš zůstatek je: {balance}💲\n---------") 
    elif pokracovat.upper() == ("B"):
        obnos = int(input(f"Váš zůstatek je {balance}💲, zde napište za kolik chcete hrát:"))
        prohra = - (obnos)
        vyhra = + (obnos) 
    elif pokracovat.upper() == ("S"):
        skin = int(input("1)♠  2)♣  3)♥  4)♦ Jaký chcete vzhled karet:"))
        if skin == 1:
            vzhled = "♠"
        elif skin == 2:
            vzhled = "♣"
        elif skin == 3:
            vzhled = "♥"
        elif skin == 4:
            vzhled = "♦"

    elif pokracovat == (""):
        counter += 1
        counter_sum += (obnos)
        
        if karty_hrace == 22:
            karty_hrace = 12

        if karty_dealera == 22:
            karty_dealera = 12

        while karty_hrace == 21 and karty_hrace == karty_dealera:
            print("---------")
            print(f"💎💎 WOW!!\nOba máte BLACKJACK!\nZůstatek: {balance}💲")
            print("------------")
            pocet_hitu_dealera = 0
            pocet_hitu_hrace = 0
            break
        while karty_hrace == 21:
            balance += vyhra
            print("---------")
            print(f"✨✨BLACKJACK!\nVyhrál jsi: {vyhra}\nZůstatek: {balance}💲")
            print("------------")
            pocet_hitu_dealera = 0
            pocet_hitu_hrace = 0
            break
        while karty_dealera == 21:
            balance += prohra
            print("---------")
            print(f"Dealerova ruka: {ruka_dealera}\nDealerovo skóre:{karty_dealera}")
            print("---------")
            print(f"Tvoje ruka: {ruka_hrace}\nTvoje skóre:{karty_hrace}")
            print("---------")
            print(f"❌❌ Dealer má BLACKJACK!\nProhrál jsi: {prohra}\nZůstatek: {balance}💲")
            print("------------")
            pocet_hitu_dealera = 0
            pocet_hitu_hrace = 0
            break

        if karty_dealera != 21 or karty_hrace != 21:
            print("---------")
            print(f"Dealerova ruka: {deck1}{vzhled}, ?\nDealerovo skóre:{hodnota_karty(deck1)}")
            print("---------")
            print(f"Tvoje ruka: {ruka_hrace}\nTvoje skóre:{karty_hrace}")
        
        while karty_hrace < 21 and karty_dealera != 21 and pocet_hitu_hrace < 6:
            pocet_hitu_dealera = 0
            pocet_hitu_hrace = 0
            volba = input("Chcete [h]it nebo [s]tand? ")
            if volba.lower() == "s":
                dealeruv_tah()
                break 
            if volba.lower() =="h":
                nova_karta = random.choice(hodnoty)
                nova_karta1= (f"{nova_karta}{vzhled}")
                ruka_hrace.append(nova_karta1)
                karty_hrace += hodnota_karty(nova_karta)
                pocet_hitu_hrace += 1
                eso = False
                karta = hodnota_karty(nova_karta)
                if karta == 11:
                    eso = True
                if karty_hrace > 21 and eso == True:
                    karty_hrace -= 10
                    eso = False
                if karty_hrace == 21:
                    dealeruv_tah()
                    pocet_hitu_hrace = 0
                    pocet_hitu_dealera = 0
                    break
                if karty_hrace > 21 and eso == False:
                    pocet_hitu()
                    pocet_hitu_hrace = 0
                    pocet_hitu_dealera = 0
                    break
                print("---------")
                print(f"Dealerova ruka: {deck1}{vzhled}, ?\nDealerovo skóre:{hodnota_karty(deck1)}")
                print("---------")
                print(f"Tvoje ruka: {ruka_hrace}\nTvoje skóre:{karty_hrace}")    
                continue

            elif volba.lower() =="x":
                exit()
            else:
                print("Neznámý příkaz")
                    
    elif pokracovat.lower() == ("x"):
        exit()
    else:
        print("Neznámý příkaz")

