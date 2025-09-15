""" """ """ # Kirjutame koos programmi mis küsib kasutajalt,mis päev on homme(tööpäev või puhkepäev),ning väljastab vastavalt sellele sobiva sõnumi.
kasutaja sisestab ühe sõna:
"tööpäev"
või "puhkepäev". """
""" kui sisestus on "tööpäev", siis kuvatakse ekranile tekst:
Ma lähen magama, head ööd!
Kui sisestus on "puhkepäev", siis kuvatakse ekranile tekst:
Veel üks osa Netflixi sarjast!
"""
# Alustame programmi.
# Küsime kasutajalt: "Mis päev on homme? (tööpäev/puhkepäev): "
# Salvestame kasutaja sisestuse muutujasse "päev".
# kui päev on võrdne "tööpäev", siis kuvame ekranile tekst: "Ma lähen magama, head ööd!"
# kui päev on võrdne "puhkepäev", siis kuvame ekranile tekst: "Veel üks osa Netflixi sarjast!"
# Muidu ( juhul kui sisestus ei ole kumbki eelnevatest ) siis väljasta ekraanile "Vale väärtus "
# Lõpetame programmi.


""" 
day = input("mis päev on homme? (tööpäev/puhkepäev): ")
if day == "tööpäev":
    print("Ma lähen magama, head ööd!") 
elif day == "puhkepäev":
    print("Veel üks osa Netflixi sarjast!") 
else:
    print("Vale väärtus")
 """

""" # Finantsnõustaja
#sa tahad osta endale uue Iphone 17 pro, aga sa oled otsustanud, et kreditti sa ei võta. Selle asemel oled sa palkanud range ja vastutustundliku
# finantsnõustaja, programmi kujul.
#See programm:
# küsib kui palju sul on raha,
# võrdleb seda iphone 17 pro hinnaga (2500 eurot) 
# ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse.
 """

""" print("Tere tulemast programmi'Finantsnõustaja'!")
print("Sinu isiklikku nõustaja ei tee emotsioon i oste. ")
money =int(input("Kui palju sul on raha sul praegu on? "))
if money< 2500:
    print("Sul pole piisavalt raha. Ole kannatlik ja kogu edasi.")
elif money == 2500:
    print("Palju õnne, sa saad osta uue Iphone 17 Pro aga kas sul on seda ikka vaja.")
else:
    print("Palju õnne, sa saad osta uue Iphone 17 Pro sularahas ja sul jääb veel raha ülegi.")
 """

""" #Sammulugeja
# Sul on eesmärk teha igapäev 10 000 sammu. Programm küsib kasutajalt mitu sammu ta on juba täna teinud, arvutab täitmise protsendi ja annab tagasisidet.
- Kui protsent <50: "Alles poole teel, liigu edasi!"
- Kui protsent on <75: "Tubli, oled peaaegu kohal!"
- Kui protsent on ≥100: "Palju õnne, oled oma eesmärgi täitnud!"
 """


gola = 10000
steps = int(input("Mitu sammu sa oled täna juba teinud?:"))
percent = (steps / gola) * 100

print (f" {percent}%")
       
if percent < 50:
    print("Alles poole teel, liigu edasi!") 
elif percent < 75:
    print("Tubli, oled peaaegu kohal!") 
elif percent < 100:
    print("Suurepärane, väga vähe on jäänud!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!")


