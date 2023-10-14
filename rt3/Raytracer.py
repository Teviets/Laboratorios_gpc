import pygame as pg
from pygame.locals import *
from rt import Raytracer
from figures import *
from materials import *
from lights import *

width = 720
height = 720

pg.init()

screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.HWACCEL | pg.HWSURFACE)
screen.set_alpha(None)

raytracer = Raytracer(screen=screen)

white = Material(diffuse=(1, 1, 1))
tex2 = pg.image.load("tex1.jpg")
tex2 = Material(texture=tex2)
tex3 = pg.image.load("tex2.jpg")
tex3 = Material(texture=tex3)
back = Material(diffuse=(0.9, 0.9, 0.9), specular=32, ks=0.2, ior=3, matType=OPAQUE)

raytracer.scene.append(Plane(position=(0,1.5,0), normal=(0,1,0), material=white))
raytracer.scene.append(Plane(position=(0,-1.5,0), normal=(0,1,0), material=white))
raytracer.scene.append(Plane(position=(0,0,-5), normal=(0,0,1), material=white))
raytracer.scene.append(Plane(position=(-1.5,0,0), normal=(1,0,0), material=white))
raytracer.scene.append(Plane(position=(1.5,0,0), normal=(1,0,0), material=white))

sizeDim = 0.5
raytracer.scene.append(AABB(position=(0.5,-0.6,-2.7), size=(sizeDim,sizeDim,sizeDim), material=tex2))
raytracer.scene.append(AABB(position=(-0.5,-0.6,-2.7), size=(sizeDim,sizeDim,sizeDim), material=tex3))
raytracer.scene.append(Disk(position=(0.5,-1.2,-2.5), normal=(0,1,0), radius=0.5, material=back))
raytracer.scene.append(Disk(position=(-0.5,-1.2,-2.5), normal=(0,1,0), radius=0.5, material=back))
raytracer.lights.append(AmbientLight(0.2))
isRunning = True
while(isRunning):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isRunning = False
            elif event.key == pg.K_s:
                pg.image.save(screen, "image.bmp")
    raytracer.rtClear()
    raytracer.rtRender()
    pg.display.flip()



pg.quit()
