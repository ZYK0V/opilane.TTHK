print("Tere! Olen sinu uus sober - Python!")
nimi=input("Mis on sinu nimi? ")
print("{}, oi kui ilus nimi!".format(nimi))
try:
    vastus1=float(input("{}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ".format(nimi)))
except ValueError:
    print("vale vaartus")
if vastus1==1:
    try:
        pikkus=int(input("Sinu pikkus => "))
        mass=float(input("Sinu mass => "))
    except ValueError:
        print("vale vaartus")
    indeks=round(mass/(0.01*pikkus)**2, 1)
    print("{}! Sinu keha indeks on: {}!".format(nimi,indeks))
    if indeks<16:
        indeksvastus="See on Tervisele ohtlik alakaal!"
    elif indeks>=16 and indeks<=19:
        indeksvastus="See on Alakaal!"
    elif indeks>=19 and indeks<25:
        indeksvastus="See on Normaalkaal"
    elif indeks>=25 and indeks<30:
        indeksvastus="See on Ulekaal"
    elif indeks>=30 and indeks<35:
        indeksvastus="See on Rasvumine!"
    elif indeks>=35 and indeks<40:
        indeksvastus="See on Tugev rasvumine!"
    elif indeks>40:
        indeksvastus="See on Tervisele ohtlik rasvumine!"
    else:
        indeksvastus="vale vaartus"
    print(indeksvastus,"\n")
else:
    print("Kahju! See on vaga kasulik info!\n")
print("Kohtumiseni, {}! Igavesti Sinu, Python!".format(nimi))

