from fakeNumpy import timeMatrix


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["viewMatrix"]

    # Convertir el vértice a una matriz columna 4x1 agregando un valor de 1
    vt = [[vertex[0]], [vertex[1]], [vertex[2]], [1]]
    # Realizar la multiplicación de la matriz del modelo con el vértice
    vt = timeMatrix(vpMatrix, timeMatrix(projectionMatrix, timeMatrix(viewMatrix, timeMatrix(modelMatrix, vt))))
    # Convertir la matriz resultado de nuevo a un vértice (lista)
    vt = [vt[0][0],vt[1][0],vt[2][0]]
    return vt

"""
#toonshader
def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calculate the intensity of the color (brightness)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Define the toon shading levels (adjust as needed)
    levels = 4

    # Calculate the new color value based on toon shading levels
    if intensity > 0.9:
        color = (1, 0, 1)  # High intensity, use white color for cuerpo
    elif intensity > 0.7:
        color = (1, 0.2, 0.8)  # Medium-high intensity, use white color for cuerpo
    elif intensity > 0.5:
        color = (0.3, 0.4, 0.6)  # Medium intensity, use orange color for camisa
    elif intensity > 0.3:
        color = (0.2, 0.6, 0.3)
    else:
        color = (0.1, 0.8, 0.2)

    return color
"""

#gray scale shader
def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calculate the intensity of the color (brightness)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Calculate new color components based on brightness
    new_red = intensity
    new_green = intensity
    new_blue = intensity

    # Return the new color
    return (new_red, new_green, new_blue)

"""
#invertion color shader
def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calculate the intensity of the color (brightness)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Calculate new color components based on brightness
    new_red = 1.0 - color[0]
    new_green = 1.0 - color[1]
    new_blue = 1.0 - color[2]

    # Return the new color
    return (new_red, new_green, new_blue)
"""