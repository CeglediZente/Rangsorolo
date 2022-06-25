import ast

def koszonto():
    print("Rangsoroló v1.2.0\nKészítő: Ceglédi Zente Holló\n\nEnnek a programnak a segítségével rangsorolásokat készíthetsz, amelyeket utána kiexportálhatsz táblázatként.")
    command = int(input("\n\n1 - Rangsorolás készítése\n2 - Kilépés\n3 - Félbehagyott rangsorolás visszatöltése\nAdd meg a parancs sorszámát: "))
    if command == 2:
        exit()
    return command

def rangsorolo(command):
    if command == 1:
        print("A rendszer a következő módon fogja a rangsort létrehozni:\nHelyezés, ID, Értékelés, Név1, Név2, Kategória, Megjegyzés")
        print("A következőkben szabja személyre a létrehozandó táblázatot!")
        idLegyen = input("Szeretné, hogy tárolja a bevitt tétel azonosítóját a táblázat (i/n)? ")
        kategoriaLegyen = input("Szeretné, hogy tárolja a bevitt tétel kategóriáját a táblázat (i/n)? ")
        megjegyzesLegyen = input("Szeretne megjegyzéseket fűzni a bevitt tételekhez (i/n)? ")
        ertekelesTipus = input("Adja meg az értékelés típusát!\n1 - számos (pl.: 1 és 10 között)\n2 - betűs (S, A+, A, A-, B+, ..., F)\n3 - egyéni\nÉrték: ")

        if ertekelesTipus == "3":
            print("Add meg az értékeket csökkenő sorrendbe! Ha nincs több érték, üss ENTER-t!")
            ertekek = []
            ertek = None
            while ertek != "":
                ertek = input("Érték: ")
                if ertek == "":
                    continue
                ertekek.append(ertek)
        if ertekelesTipus == "2":
            ertekek = ["SS", "S+", "S", "S-", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E+", "E", "E-", "F+", "F", "F-"]
        nevmezoSzam = int(input("Hány névmezőt szeretnél létrehozni (pl.: 2, szerző neve, könyv címe)? "))
        nevmezoLista = []
        felhasznaloAttributumLista = []
        for _ in range(nevmezoSzam):
            nevmezoLista.append(input("Adj meg egy névmezőt: "))

        kod = ["<style>", ".rangsor-tablazat, .rangsor-tablazat tr, .rangsor-tablazat tr td, .rangsor-tablazat tr th {", "border-collapse: collapse;", "border: 2px solid rgb(0, 0, 0);", "padding: 6px;", "font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;", "font-size: large;", "text-align: center;", "}", "</style>", "<table class=\"rangsor-tablazat\">", "<tr>"]
        print("A rangsoroló a következőképpen néz ki:")
        print("Helyezés", end="")
        kod.append("<th>Helyezés</th>")
        if idLegyen == "i":
            print(", ID", end="")
            kod.append("<th>ID</th>")
        print(", Értékelés", end="")
        kod.append("<th>Értékelés</th>")
        for elem in nevmezoLista:
            print(f", {elem}", end="")
            kod.append(f"<th>{elem}</th>")
            felhasznaloAttributumLista.append(elem)
        if kategoriaLegyen == "i":
            print(", Kategória", end="")
            kod.append("<th>Kategória</th>")
            felhasznaloAttributumLista.append("Kategória")
        if megjegyzesLegyen == "i":
            print(", Megjegyzés", end="")
            kod.append("<th>Megjegyzés</th>")
            felhasznaloAttributumLista.append("Megjegyzés")
        print(f"\n következnek az elemek, ezek hozzáadása után, ha készen vagy, a(z) {nevmezoLista[0]} értéknél írj 'kesz'-t.\nHa szeretnéd még később a fájl szerkesztését folytatni, akkor írj 'kesobb'-öt.")
        kod.append("</tr>")

        elemekListaja = []
        sorszam = 0
    elif command == 3:
        print("Fájl visszatöltése!")
        fileName = input("Add meg a mentett fájl nevét (kiterjesztés nélkül): ")
        fileBetoltes = open(f"./saves/mentett/{fileName}.txt", "r", encoding="UTF-8")
        index = 0
        for sor in fileBetoltes:
            index += 1
            sorJo = "".join(sor.split("\n"))
            if index == 1:
                elemekListaja = ast.literal_eval(sorJo)
            elif index == 2:
                idLegyen = sorJo
            elif index == 3:
                kategoriaLegyen = sorJo
            elif index == 4:
                megjegyzesLegyen = sorJo
            elif index == 5:
                ertekelesTipus = sorJo
            elif index == 6:
                kod = ast.literal_eval(sorJo)
            elif index == 7:
                felhasznaloAttributumLista = ast.literal_eval(sorJo)
            elif index == 8:
                sorszam = int(sorJo)
            elif index == 9:
                nevmezoSzam = int(sorJo)
            print("A fájl sikeresen vissza lett töltve!")
    tovabb = True
    while tovabb == True:
        elem = []
        if idLegyen == "i":
            sorszam += 1
            elem.append(int(sorszam))
        # print(elem, elemekListaja)
        for attributum in felhasznaloAttributumLista:
            elemAttr = input(f"{attributum}: ")
            elem.append(elemAttr)
            if elemAttr == "kesz":
                break
            if elemAttr == "kesobb":
                break
        # print(elem, elemekListaja)
        if elemAttr == "kesz":
            break
        if elemAttr == "kesobb":
            kesobb(elemekListaja, idLegyen, kategoriaLegyen, megjegyzesLegyen, ertekelesTipus, kod, felhasznaloAttributumLista, sorszam, nevmezoSzam)
            exit()
        # print(elem, elemekListaja)
        ertekeles = int(input("Értékelés: "))
        if ertekelesTipus == "1":
            elem.insert(0, int(ertekeles))
        else:
            elem.insert(0, ertekeles)
        # print(elem, elemekListaja)
        print("\nElem sikeresen létrehozva!\n\n")
        elemekListaja.append(elem)
    if ertekelesTipus == "1":
        elemekListaja.sort()
        elemekListaja.reverse()
    # print(elemekListaja)
    helyezesIndex = 0
    fileName = input("\nAdd meg milyen néven mentse el a rendszer a fájlt (kiterjesztést ne írj!): ")
    vege = open(f"./saves/kesz/{fileName}.html", "w", encoding="UTF-8")
    for sor in elemekListaja:
        helyezesIndex += 1
        kod.append("<tr>")
        kod.append(f"<td>{helyezesIndex}.</td>")
        index = 0
        if idLegyen == "i":
            kod.append(f"<td>{sor[1]}</td>")
            index = 1
        kod.append(f"<td>{sor[0]}</td>")
        for _ in range(nevmezoSzam):
            index += 1
            kod.append(f"<td>{sor[index]}</td>")
        if megjegyzesLegyen == "i" and kategoriaLegyen == "i":
            kod.append(f"<td>{sor[-2]}</td>")
        if megjegyzesLegyen == "i" or kategoriaLegyen == "i":
            kod.append(f"<td>{sor[-1]}</td>")
        kod.append("</tr>")

    # print(kod)
    kod.append("</table>")
    vege.write("\n".join(kod))
    print("Sikeres kiíratás!\nA saves mappában megtalálod a rangsort!")

def kesobb(elemekListaja, idLegyen, kategoriaLegyen, megjegyzesLegyen, ertekelesTipus, kod, felhasznaloAttributumLista, sorszam, nevmezoSzam):
    fileNev = input("Add meg a fájl nevét, ahova menteni szeretnéd a programot (kiterjesztés nélkül): ")
    mentesHely = open(f"./saves/mentett/{fileNev}.txt", "w", encoding="UTF-8")
    mentesHely.write(f"{elemekListaja}\n{idLegyen}\n{kategoriaLegyen}\n{megjegyzesLegyen}\n{ertekelesTipus}\n{kod}\n{felhasznaloAttributumLista}\n{sorszam-1}\n{nevmezoSzam}")
    print("A fájl sikeresen mentésre került a saves mappába!")

command = koszonto()
if command == 1 or command == 3:
    rangsorolo(command)
