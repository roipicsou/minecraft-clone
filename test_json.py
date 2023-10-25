import json

with open('data.json', 'r') as fichier :
    data = json.load(fichier)


def structure(name) :
    if name in data :
        structure = data[name]
        if "stone" in structure : 
            stone = structure["stone"]
            print(stone)
            nb = 1
            while True :
                bloc = "bloc_" + str(nb)
                if bloc in stone :
                    nb += 1
                else :
                    nb -= 1
                    break
            print(f"le nombre de bloc est de {nb}")
            for i in range(1, nb + 1) :
                bloc = "bloc_" + str(i)
                if bloc in stone :
                    cord = stone[bloc]
                    print(f'{cord["x"]}/{cord["y"]}/{cord["z"]}')
        if "grass" in structure : 
            stone = structure["grass"]
            print(stone)
            nb = 1
            while True :
                bloc = "bloc_" + str(nb)
                if bloc in stone :
                    nb += 1
                else :
                    nb -= 1
                    break
            print(f"le nombre de bloc est de {nb}")
            for i in range(1, nb + 1) :
                bloc = "bloc_" + str(i)
                if bloc in stone :
                    cord = stone[bloc]
                    print(f'{cord["x"]}/{cord["y"]}/{cord["z"]}')

structure("404")