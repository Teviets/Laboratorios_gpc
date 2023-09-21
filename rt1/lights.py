#import numpy as np
import fakeNumpy as fnp

def reflectVector(normal, direction):
    reflect = 2* fnp.dot_product(normal, direction)
    reflect =[reflect * normal[0], reflect * normal[1], reflect * normal[2]]
#    reflect = fnp.elementwise_multiply(reflect, normal)
    reflect = fnp.elementwise_subtract(reflect, direction)
    reflect = fnp.normalize(reflect)
    return reflect

class Light(object):
    def __init__(self, intensity = 1, color = (1,1,1), lightType = "None"):
        self.intensity = intensity
        self.color = color
        self.lightType = lightType

    def getLightColor(self):
        return [self.color[0] * self.intensity,
                self.color[1] * self.intensity,
                self.color[2] * self.intensity]
    
    def getDiffuseColor(self, intercept):
        return None
    
    def getSpecularColor(self, intercept, viewPos):
        return None

class AmbientLight(Light):
    def __init__(self, intensity = 1, color = (1,1,1)):
        super().__init__(intensity, color, "AmbientLight")

class DirectionalLight(Light):
    def __init__(self, direction = (0,-1,0), intensity = 1, color = (1,1,1)):
        super().__init__(intensity, color, "DirectionalLight")
        self.direction = fnp.normalize(direction)

    def getDiffuseColor(self, intercept):

        dir = [(i *-1) for i in self.direction]
        intensity = fnp.dot_product(intercept.normal, dir) * self.intensity
        intensity = max(0, min(1, intensity))

        diffuseColor = [(i * intensity) for i in self.color]

        return diffuseColor

    def getSpecularColor(self, intercept, viewPos):
        dir = [(i *-1) for i in self.direction]

        reflect = reflectVector(intercept.normal, dir)

        viewDir = fnp.elementwise_subtract(viewPos, intercept.point)
        viewDir = fnp.normalize(viewDir)

        specIntensity = max(0, fnp.dot_product(viewDir, reflect)) ** intercept.obj.material.spec
        specIntensity *= self.intensity

        specColor = [(i * specIntensity) for i in self.color]

        return specColor