def main():
    import time
    import random
    print("Jack and Poy")
    a = int(input("1. Bato, 2. Gunting, 3. Papel: "))
    if a == 1:
        print("Bato ang pinili mo")
    if a == 2:
        print("Gunting ang pinili mo")
    if a == 3:
        print("Papel ang pinili mo")

    print("Jack")
    time.sleep(1)
    print("and")
    time.sleep(1)
    print("Poy!")
    time.sleep(1)

    b = random.randint (1,3)
    
    if b == 1:
        print("Bato ang pinili ko")
    if b == 2:
        print("Gunting ang pinili ko")
    if b == 3:
        print("Papel ang pinili ko")
    
    if a == 1:
        if b == 1:
            print("Mukha kayong mga bato, walang nanalo!")
        if b == 2:
            print("Durog ang gunting sa bato mo!")
        if b == 3:
            print("Tinakpan ng papel ko ang bato mo!")
    
    if a == 2:
        if b == 1:
            print("Durog ang gunting mo sa bato ko!")
        if b == 2:
            print("Mag scissors na lang kayong dalawa!")
        if b == 3:
            print("Punit ang pagka papel ko sa gunting mo!")
    
    if a == 3:
        if b == 1:
            print("Tinakpan ng papel mo ang bato ko!")
        if b == 2:
            print("Punit ang pagka papel mo sa gunting ko!")
        if b == 3:
            print("Pareho tayong mapapel!")
    
    ulit=input("Ano, rematch tayo? Oo o Hindi? ").lower()
    
    if ulit == "oo":
        print(main())
    else:
        exit()

print(main())