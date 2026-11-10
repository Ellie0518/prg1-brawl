import random

# Startvärdena väljer du själv.
spelare_hp = 100
fiende_hp = 100

# Ditt första kort börjar här.
name = input("Vad heter laget?")
print(f"Hej {name} välkommen till spelet Volleyboll Masters.")
print ("Erat lag kommer att vara i en turnering, ni kommer att möta fienderna." \
"för varje poäng ni gör eller förlorar kommer ni tappa hp. Det lag som först har 0 hp förlorar!")

print("Rules: Mer hp på serves, spike och block. Tappar hp om andra laget vinner bollen.")

print(f"Matchstart! {name} börjar med serven")
val = input("Vilken serv väljer du?(överarms/underarms)")
if val == "överarms":
    print(" Cool serv! Den sitter och det blir serves. 100 hp kvar")
else: 
    print("Det är synd, serven var för enkel och fienderna gjorde en spike och vann. 90 hp kvar")
