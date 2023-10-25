from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import json

app = Ursina()

jump_height = 2 # Default: 2
jump_duration = 0.5 # Default: 0.5
jump_fall_after = 0.35 # Default: 0.35
gravity_scale = 1 # Default: 1
mouse_sensitivity = Vec2(40,40) # Default: (40,40)
run_speed = 5 # Default: 5

window.fps_counter.enabled = True
window.exit_button.visible = False

punch = Audio('assets/punch', autoplay=False)

max_platofrme = 15
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
        c = random.randint(0,3)
        if c == 1 :
            voxel = Voxel(position=(x, 1, z),texture=random.choice(blocks_pose))

structure(-1,0,0,"404")
structure(-1,10,0,"404")

player = FirstPersonController()

player.jump_height = jump_height
player.jump_up_duration = jump_duration
player.mouse_sensitivity = mouse_sensitivity
player.speed = run_speed
player.gravity = gravity_scale

app.run()