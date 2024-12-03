temperatura = int(input("Unesite temperaturu"))
test_temperatura = -1
temperatura = test_temperatura
poruka = ""
if temperatura < 0 :
    print ("Oprez klizavo")
if temperatura >0:
    poruka = "Temperatura iznad 0"
    if temperatura >30:
        print("ukljucite klima uredjaj")


test_temperatura = -1
ocekivana_poruka = "Oprez klizavo"
if poruka == ocekivana_poruka:
    print("Case - ispod nule - Test prosao")


