import random
import time

spelare_hp = 100
fiende_hp = 150

spelare_skada = random.randint(5, 20)
fiende_skada = random.randint(10, 25)

name = input("Vad heter laget?")
print(f"Hej {name} välkommen till spelet Volleyboll Masters.")
print ("Erat lag kommer att vara i en turnering, ni kommer att möta fienderna." \
"För varje poäng ni gör eller förlorar kommer ni tappa eller behålla era hp. Det lag som först har 0 hp förlorar!")

print("Rules: Mer hp på serves, spike och block. Tappar hp om andra laget vinner bollen.")

print(f"Matchstart! {name} börjar med serven")
val = input("Vad vill du serva?(överarms/underarms)")

for i in range(3, 0, -1):
    print(i)
    time.sleep(0.3)
print ("Serven går över...")

if val == "överarms":
    fiende_hp -= random.randint (10, 25)
    print(f"{name} lag vann med serves! Nu har fiende laget {fiende_hp} hp kvar.")

else: 
    if val == "underarms":
        spelare_hp -= random.randint (5, 20)
        print(f"fiende lag gör en spike ner i narken och vinner. Nu har {name} laget {spelare_hp} hp kvar.")

while True:
    print("\n1. Fortsätt spela")
    print("2. Visa status")
    print("3. Avsluta spelet")
    val = input("välj: ")

    if val == "1":
        print("Vi fortsätter spelet.")
        spelare_skada = random.randint(5, 20)
        fiende_skada = random.randint(10, 25)

        
        
    elif val == "2": 
        print(f"Statusen för laget {name} är {spelare_hp}, status för fiende är {fiende_hp}")
    elif val == "3": 
        print("Okej ses nästa gång.")
        break
