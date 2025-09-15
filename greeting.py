#Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
#Programm tervitab kasutajat vastavalt soole:

#    Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“

#    Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“

#    Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“



last_name = input("Tere mis on teie perkonnanimi:? "). title()  
gender = input("ja mis sugu te olete:? (m/n) ").lower() 

if gender == "m":
    print(f"Tere, härra {last_name}!") 
elif gender == "n":    
    print(f"Tere, proua {last_name}!") 
else:
    print(f"Tere tulemast, {last_name}! (sugu ei olegi tähtis).")

