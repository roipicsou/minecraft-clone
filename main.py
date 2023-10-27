from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import json

app = Ursina()

jump_height = 1.5 # Default: 2
jump_duration = 0.5 # Default: 0.5
jump_fall_after = 0.35 # Default: 0.35
gravity_scale = 1 # Default: 1
mouse_sensitivity = Vec2(40,40) # Default: (40,40)
run_speed = 5 # Default: 5

window.fps_counter.enabled = True
window.exit_button.visible = False

punch = Audio('assets/punch', autoplay=False)

max_platofrme = 10
min_y_platforme = -2

blocks = [
    load_texture('assets/grass.png'), # 0
    load_texture('assets/grass.png'), # 1
    load_texture('assets/stone.png'), # 2
    load_texture('assets/gold.png'),  # 3
    load_texture('assets/lava.png'),  # 4
]

blocks_pose = [
    load_texture('assets/grass.png'), # 0
    load_texture('assets/grass.png'), # 0
    load_texture('assets/stone.png'), # 2
]

block_id = 1

with open('data.json', 'r') as fichier :
    data = json.load(fichier)

def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]


hand = Entity(
    parent=camera.ui,
    model='assets/block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        punch.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)


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
                positions_bloc = get_postions(str(self.get_position()), "lol")
                print(f"le position du bloc {positions_bloc}")
                positions_player = get_postions(str(player.get_position()), "player")
                print(f"le position du player {positions_player}")
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'right mouse down':
                destroy(self)


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


def structure(x_point, y_point, z_point, name) :
    if name in data :
        print(f"pour le structure {name} il y a :")
        structure = data[name]
        if "stone" in structure : 
            stone = structure["stone"]
            nb = 1
            while True :
                bloc = "bloc_" + str(nb)
                if bloc in stone :
                    nb += 1
                else :
                    nb -= 1
                    break
            print(f"    {nb} bloc de stone")
            for i in range(1, nb + 1) :
                bloc = "bloc_" + str(i)
                if bloc in stone :
                    cord = stone[bloc]
                    x = cord["x"]
                    y = cord["y"]
                    z = cord["z"]
                    voxel = Voxel(position=(x_point - x,z_point + z, y_point - y), texture='assets/stone.png')
        if "grass" in structure : 
            grass = structure["grass"]
            nb = 1
            while True :
                bloc = "bloc_" + str(nb)
                if bloc in stone :
                    nb += 1
                else :
                    nb -= 1
                    break
            print(f"    {nb} bloc de gasse")
            for i in range(1, nb + 1) :
                bloc = "bloc_" + str(i)
                if bloc in grass :
                    cord = grass[bloc]
                    x = cord["x"]
                    y = cord["y"]
                    z = cord["z"]
                    voxel = Voxel(position=(x_point - x,z_point + z, y_point - y), texture='assets/grass.png')


for z in range(max_platofrme):
    for x in range(max_platofrme):
        voxel = Voxel(position=(x, 0, z),texture=random.choice(blocks_pose))

for z in range(max_platofrme) :
    for x in range(max_platofrme) :
        for y in range(min_y_platforme,0) :
            c = random.randint(0,100)
            if c == 78 :
                voxel = Voxel(position=(x,y,z), texture='assets/gold.png')
            else :
                voxel = Voxel(position=(x,y,z), texture='assets/stone.png')

for z in range(max_platofrme):
    for x in range(max_platofrme):
        c = random.randint(0,10)
        if c == 1 :
            voxel = Voxel(position=(x, 1, z),texture=random.choice(blocks_pose))

structure(-1,0,0,"hause")
structure(-1,1,0,"404")

player = FirstPersonController()

player.jump_height = jump_height
player.jump_up_duration = jump_duration
player.mouse_sensitivity = mouse_sensitivity
player.speed = run_speed
player.gravity = gravity_scale


app.run()