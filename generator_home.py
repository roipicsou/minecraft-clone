from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import json

app = Ursina()

window.fps_counter.enabled = True
window.exit_button.visible = False

blocks = [
    load_texture('assets/grass.png'), # 0
    load_texture('assets/grass.png'), # 1
    load_texture('assets/stone.png'), # 2
    load_texture('assets/gold.png'),  # 3
    load_texture('assets/lava.png'),  # 4
]

block_id = 1

with open('data.json', 'r') as fichier :
    data = json.load(fichier)


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'right mouse down':
                destroy(self)

def structure(x_point, z_point, y_point, name) :
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
                    x = cord["x"]
                    y = cord["y"]
                    z = cord["z"]
                    print(f"{x}/{y}/{z}")
                    voxel = Voxel(position=(x_point - x,y_point - y,z_point + z), texture='assets/stone.png')
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
                    x = cord["x"]
                    y = cord["y"]
                    z = cord["z"]
                    print(f"{x}/{y}/{z}")
                    voxel = Voxel(position=(x_point - x,y_point - y,z_point + z), texture='assets/grass.png')

structure(-1,0,0,"404")
voxel = Voxel(position=(0,0,0), texture='assets/stone.png')

player = FirstPersonController()

app.run()