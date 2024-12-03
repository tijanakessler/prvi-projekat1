temperatura = int(input("Unesite temperaturu: "))
test_temperatura = -1
test_temperatura = temperatura
poruka = ""
if temperatura < 0:
   poruka = "Oprez klizavo"

if temperatura > 0:
    poruka = "Temperatura iznad 0"
    if temperatura > 30:
        poruka = "Ukljucite klima uredjaj"


ocekivana_poruka = "Oprez klizavo"
if ocekivana_poruka == ocekivana_poruka:
    print("Case - ispod nule - test prosao")
    