import pygame as pg
from pygame.locals import *
from rt import Raytracer
from figures import *
from materials import *
from lights import *

width = 720
height = 460

pg.init()

screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.HWACCEL | pg.HWSURFACE)
screen.set_alpha(None)

background_image = pg.image.load('./img/prueba_fondo.jpg')  # Cambia 'ruta_de_tu_imagen_de_fondo.jpg' a la ruta correcta de tu imagen
background_image = pg.transform.scale(background_image, (width, height))  # Escala la imagen al tamaño de la ventana

raytracer = Raytracer(screen=screen)

white = Material(diffuse=(1, 0, 1),specular=32, ks=0.2, ior=3, matType=OPAQUE)
grass = Material(diffuse=(0, 1, 0), specular=32, ks=0.2, ior=3, matType=OPAQUE)
water = Material(diffuse=(0, 0, 0.9), specular=32, ks=0.2, ior=3, matType=TRANSPARENT)
back = Material(diffuse=(0.9, 0.9, 0.9), specular=32, ks=0.2, ior=3, matType=OPAQUE)
cristal = Material(diffuse=(1, 1, 1), specular=64, ks=0.2, ior=1.1, matType=TRANSPARENT)
mirror = Material(diffuse=(1, 1, 1), specular=64, ks=0.2, ior=1.1, matType=REFLECTIVE)
tex1 = pg.image.load("./img/fondo.jpg")
tex1 = Material(texture=tex1)
raytracer.envMap = background_image

raytracer.scene.append(OvalSphere((-3, 0, -5), 1, 2, grass))
raytracer.scene.append(OvalSphere((0, 0, -50), 1, 2, water))
raytracer.scene.append(OvalSphere((0, 0, -10), 1, 2, cristal))
raytracer.scene.append(OvalSphere((3, 0, -10), 1, 2, mirror))

raytracer.lights.append(AmbientLight(0.3))
raytracer.lights.append(DirectionalLight(direction=(-1, -1, -1)))


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
