import random

try:
    # game variable
    w = int(input("Enter first Number\n"))
    d = int(input("Enter Second Number\n"))

    s = 6
    p = []

    #game loop
    for a in range(1,3):
        m = random.randint(w, d)
        print(f"\nPLAYER{a} turm")
        for i in range(30):
            print("*",end="")
        for i in range(1,s):
            print(i)
            try:
                n = int(input("\nEnter your number\n"))
                if n>=w and n<=d:
                    if n==m:
                        print("\nYou win")
                        print(f"PLAYER{a} take {i} turns to win ")
                        p.append(i)
                        break
                    elif n>m:
                        print("\nYour number is grater")
                        if i==s-1:
                            p.append(0)
                            print(f"Player{a} not win")
                    elif n<m:
                        print("\nYour number is smaller")
                        if i==s-1:
                            p.append(0)
                            print(f"Player{a} not win")
                else:
                    print(f"\nEnter number only between {w} and {d}\n\n")
                    continue

            except:
                print("\nEnter only numbers")

except:
    print("\nInvaled value")
l = p[0]
f = p[1]
if l > f:
    print("\nPlayer1 win")
elif l == f:
    print("\nGame Draw")