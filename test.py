#lol = ["é", "lol", "lollll;l"]
data = ['2', '.', '0', '5', '7', '1', '7', ' ', '0', '.', '2', '5', ' ', '2', '.', '1', '7', '3', '8', '9']

for i in data :
    if i == "." :
        id = data.index(i)
        x = data[id - 1]
        data.remove(i)
        break
for i in data :
    if i == "." :
        id = data.index(i)
        y = data[id - 1]
        data.remove(i)
        break
for i in data :
    if i == "." :
        id = data.index(i)
        z = data[id - 1]
        data.remove(i)
        break

print(f"{x}/{y}/{z}")
data = ['2', '.', '0', '5', '7', '1', '7', ' ', '0', '.', '2', '5', ' ', '2', '.', '1', '7', '3', '8', '9']

#i = "é"
#id = lol.index(i)
#print(lol[id + 1])


def get_postions(donée, demande) :
    positions = donée
    positions = positions.replace("LPoint3f(", "")
    positions = positions.replace(")","")
    x = 0
    y = 0
    z = 0
    print(positions)
    list_postions = []
    for i in positions :
        if i == "," or "" :
            pass
        else :
            list_postions.append(i)
    if demande == "player" :
        print("demande player")
        for i in list_postions :
            if i == "." :
                id = list_postions.index(i)
                print(list_postions[id - 1])
                x = list_postions[id - 1]
                list_postions.remove(i)
                break
        for i in list_postions :
            if i == "." :
                id = list_postions.index(i)
                y = list_postions[id - 1]
                print(list_postions[id - 1])
                list_postions.remove(i)
                break
        for i in list_postions :
            if i == "." :
                id = list_postions.index(i)
                z = list_postions[id - 1]
                print(list_postions[id - 1])
                list_postions.remove(i)
                break
    else :
        print(list_postions)
        x = list_postions[0]
        y =list_postions[2]
        z = list_postions[4]
    return [x,y,z]

print(get_postions(data, "player"))