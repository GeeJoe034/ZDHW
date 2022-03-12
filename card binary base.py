
    card_number3 = []
    i = 4
    c = 0
    while i < 128:
        card_number3.append(i)
        if c < 3:
            i += 1
            c += 1
        else:
            i += 5
            c = 0
    show(card_number3)
 elif choice == "4":
    print("Card Bainary base 4 ")
    card_number4 = []
    i = 8
    c = 0
    while i < 128:
        card_number4.append(i)
        if c < 7:
            i += 1
            c += 1
        else:
            i += 9
            c = 0
    show(card_number4)
 elif choice == "5":
    print("Card Bainary base 5 ")
    card_number5 = []
    i = 16
    c = 0
    while i < 128:
        card_number5.append(i)
        if c < 15:
            i += 1
            c += 1
        else:
            i += 17
            c = 0
    show(card_number5)
 elif choice == "6":
    print("Card Bainary base 6 ")
    card_number6 = []
    i = 32
    c = 0
    while i < 128:
        card_number6.append(i)
    if c < 30:
        i += 1
        c += 1
    else:
        i += 33
        c = 0
    show(card_number6)
 elif choice == "7":
    print("Card Bainary base 7 ")
    card_number7 = []
    for i in range(64, 128):
        card_number7.append(i)
    show(card_number7)
k+=1
l+=1
