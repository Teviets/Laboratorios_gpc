import fakeNumpy as fnp
import numpy as np
import fakeNumpy as fnp


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    vt = [vertex[0],vertex[1],vertex[2],1]
    
    vt = fnp.timeMatrixSingle(modelMatrix,vt)
    
    vt = [vt[0]/vt[3],vt[1]/vt[3],vt[2]/vt[3]]
    return vt

def fragmentShader(**kwargs):
    color = [1,1,0]
    return color