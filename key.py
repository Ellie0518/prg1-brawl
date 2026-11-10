gömställe = 4
försök_kvar = 5
gissning = 0

while gissning != gömställe and försök_kvar > 0:
    gissning = int(input("Gissa gömställe (1-5): "))
    försök_kvar -= 1
    if gissning <= gömställe:
        print("Fisk!")
    else:
        print("Fågel!")

if gissning == gömställe:
    print("Du hittade nyckeln!")
else:
    print("Slut på försök!")
    