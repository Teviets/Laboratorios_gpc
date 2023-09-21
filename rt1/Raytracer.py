import pygame
from pygame.locals import *
from rt import Raytracer
from figures import *
from lights import *
from materials import *

def SnowMan():
    raytracer.scene.append(
        Sphere(position=(0,-1.5,-10), radius=1, material=snow)
    )
    raytracer.scene.append(
        Sphere(position=(0,0,-10), radius=0.75, material=snow)
    )
    raytracer.scene.append(
        Sphere(position=(0,1.1,-10), radius=0.6, material=snow)
    )

    raytracer.scene.append(
        Sphere(position=(0,-1.2,-10), radius=0.2, material=button)
    )
    raytracer.scene.append(
        Sphere(position=(0,-0.5,-10), radius=0.12, material=button)
    )
    raytracer.scene.append(
        Sphere(position=(0,-0.05,-10), radius=0.12, material=button)
    )

    raytracer.scene.append(
        Sphere(position=(-0.07,0.75,-10), radius=0.05, material=button2)
    )
    raytracer.scene.append(
        Sphere(position=(0.07,0.75,-10), radius=0.05, material=button2)
    )

    raytracer.scene.append(
        Sphere(position=(-0.2,0.8,-10), radius=0.05, material=button2)
    )
    raytracer.scene.append(
        Sphere(position=(0.2,0.8,-10), radius=0.05, material=button2)
    )

    raytracer.scene.append(
        Sphere(position=(0,1.02,-10), radius=0.1, material=carrot)
    )

    raytracer.scene.append(
        Sphere(position=(-0.2,1.2,-10), radius=0.1, material=snow)
    )
    raytracer.scene.append(
        Sphere(position=(0.2,1.2,-10), radius=0.1, material=snow)
    )
    raytracer.scene.append(
        Sphere(position=(-0.2,1.2,-10), radius=0.05, material=button2)
    )
    raytracer.scene.append(
        Sphere(position=(0.2,1.2,-10), radius=0.05, material=button)
    )


width = 512
height = 1024/2

pygame.init()

screen = pygame.display.set_mode(
    (width, height), 
    pygame.DOUBLEBUF | 
    pygame.HWACCEL | 
    pygame.HWSURFACE
)
screen.set_alpha(None)


raytracer = Raytracer(screen)
raytracer.rtClearColor(0.4, 0.4, 0.6)

brick = Material(diffuse=[1, 0.4, 0.4], spec = 8)
grass = Material(diffuse=[0.4, 1, 0.4], spec = 32)
water = Material(diffuse=[0.4, 0.4, 1], spec = 256)
snow = Material(diffuse=[1, 1, 1], spec = 5)
button = Material(diffuse=[0, 0, 0], spec = 10)
button2 = Material(diffuse=[0, 0, 0], spec = 5)
carrot = Material(diffuse=[1, 0.5, 0], spec = 1)

SnowMan()

raytracer.lights.append(
    AmbientLight(intensity=0.2)
) 
raytracer.lights.append(
    DirectionalLight(direction=(-1, 0, -1), intensity=0.5)
)

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    raytracer.rtClear()

    raytracer.rtRender()
    
    pygame.display.flip()

pygame.quit()