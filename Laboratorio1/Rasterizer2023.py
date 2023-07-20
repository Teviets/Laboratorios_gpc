from gl import Renderer, V2,V3, color
import shaders

width = 1080

height = 1080

rend = Renderer(width,height)

rend.glClearColor(0, 0, 0)
rend.glClear()


rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel("avion.obj", translate = (width/2, height/2, 0),scale = (300, 300,0))

rend.glRender()

rend.glFinish("output.bmp")