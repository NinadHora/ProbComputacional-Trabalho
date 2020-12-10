#!/usr/bin/env python
# coding: utf-8

# # Random Texture Generation
# Probabilidade Computacional 2020.2

#     Ana Carolina da Hora - Matrícula
#     Heloisa Matta da Cunha Pessoa - Matrícula 1611868
#     Matheus Moreira - Matrícula

# In[7]:


from PIL import Image
import numpy as np
import math
import random as rand

type_textures = [('chess'),('picnic'), ('noise'),('wood'),('lines'),('marble'),('cloud'),('smooth'),('pixels')]

color = [
('dark skin', [0.4522251474168803, 0.3195169023866588, 0.2640797029583723]),
('light skin',[ 0.7664232707505688, 0.5841431031145494, 0.5047299502518718]),
('blue sky', [0.3653341811826313, 0.481327042486779, 0.6165481324045643]),
('foliage', [0.35287211944234914, 0.4238728463614635, 0.25402943732139904]),
('blue flower', [0.5109284912602754, 0.5043792613433803, 0.6893839226970905]),
('bluish green', [0.3869781874102796, 0.747713653318347, 0.669567100186017]),
('orange', [0.8610217621061337, 0.48320689338088946, 0.17625165953460217]),
('purplish blue', [0.28083051261516145, 0.3591581422277575, 0.6582971549790119]),
('moderate red', [0.762783242481741, 0.33049576940690034, 0.3828090365310446]),
('purple', [0.3548758067268991, 0.23079567149636993, 0.4101201637997396]),
('yellow green', [0.629043785118802, 0.7411994427418241, 0.24280704509270706]),
('orange yellow', [0.8965318085721251, 0.6296778526019191, 0.1600326803764384]),
('blue', [0.16892691578503588, 0.2415747621327311, 0.5762774822654635]),
('green', [0.27908996737667735, 0.5847912061094804, 0.28053792720644494]),
('red', [0.6887484340529423, 0.18907933916840838, 0.2206774636978624]),
('yellow ', [0.933460767413091, 0.7825226060166899, 0.08637123239068975]),
('magenta ', [0.7359229552868234, 0.3287357631191987, 0.5880041004631658]),
('cyan ', [-0.37597313801476506, 0.5341684519550843, 0.6516802862942742]),
('white 9.5 (.05 D) ', [0.9604345851815389, 0.9603051823185978, 0.9402646403560875]),
('neutral 8 (.23 D) ', [0.7848025131996234, 0.7903189700333797, 0.7864960707699661]),
('neutral 6.5 (.44 D) ', [0.6287594851109823, 0.6330021485029693, 0.6319170066986666]),
('neutral 5 (.70 D) ', [0.4695121317846052, 0.47611890396845197, 0.47586812172547405]),
('neutral 3.5 (1.05 D) ', [0.3253482641817533, 0.33054049058799945, 0.3321140690612026]),
('black 2', [0.19459633433851595, 0.19541988810412453, 0.19790519049054628])]


# # Functions

# In[8]:


def generateColor():
    return rand.choice(color)[1]

def generateNoise():
    # Gera 3 valores para o RGB de cada pixel da imagem
    for w in range(textureWidth):
        texture.append([])
        for h in range(textureHeight):
            rValues = generateColor()
            texture[w].append((rValues[0],rValues[1],rValues[2]))
            
def generateSmooth(x,y):
    fractX = x - int(x)
    fractY = y - int(y)
    
    x1 = (int(x) - textureWidth) % textureWidth
    y1 = (int(y) - textureHeight) % textureHeight
    x2 = (x1 + textureWidth - 1) % textureWidth
    y2 = (y1 + textureHeight - 1) % textureHeight
    
    value = 0.0
    value += fractX * fractY * texture[x1][y1][0]
    value += (1 - fractX) * fractY * texture[x2][y1][0]
    value += fractX * (1 - fractY) * texture[x1][y2][0]
    value += (1 - fractX) * (1 - fractY) * texture[x2][y2][0]
    
    return value

def generateCloud(x,y,zoomFactor):
    value = 0.0
    initialZF = zoomFactor
    while(zoomFactor >= 1):
        value += generateSmooth(x/zoomFactor,y/zoomFactor) * zoomFactor
        zoomFactor /= 2.0
    return(128.0*value/initialZF)


# # Drawing

# In[9]:


def drawNoise():
    for w in range(textureWidth):
        for h in range(textureHeight):
            red = int(texture[w][h][0] * 256)
            green = int(texture[w][h][1] * 256)
            blue = int(texture[w][h][2] * 256)
            image.putpixel((w,h),(red, green, blue))
    image.show()
    
    
def drawPixelated():
    color = generateColor()
    zoom = rand.randint(1,6)
    for w in range(textureWidth):
        for h in range(textureHeight):
            red = int(generateSmooth(w/zoom,h/zoom)*color[0]*256)
            green = int(generateSmooth(w/zoom,h/zoom)*color[1]*256)
            blue = int(generateSmooth(w/zoom,h/zoom)*color[2]*256)
            image.putpixel((w,h),(red, green, blue))
    image.show()

def drawSmooth():
    color = generateColor()
    for w in range(textureWidth):
        for h in range(textureHeight):
            zoom = rand.randint(1,200)
            red = int(generateSmooth(w/zoom,h/zoom)*color[0]*256)
            green = int(generateSmooth(w/zoom,h/zoom)*color[1]*256)
            blue = int(generateSmooth(w/zoom,h/zoom)*color[2]*256)
            image.putpixel((w,h),(red, green, blue))
    image.show()
    
    
    
def drawCloud():
    color = generateColor()
    for w in range(textureWidth):
        for h in range(textureHeight):
            red = int(color[0]*256)
            green = int(generateCloud(w,h,64))
            blue = int(color[2]*256)
            image.putpixel((w,h),(red, green, blue))
    image.show()
    
def drawMarble():
#     xPeriod = 10.0 # Quantas linhas teremos no eixo x
#     yPeriod = 10.0 # Quantas linhas teremos no eixo y
#     # xPeriod e yPeriod juntos definem o ângulo das linhas
    
#     lineTwist = 5.0 # Grau de torção das linhas
#     zoomFactor = 32.0
    xPeriod = rand.uniform(7.0, 10.0) # Quantas linhas teremos no eixo x
    yPeriod = rand.uniform(7.0, 10.0) # Quantas linhas teremos no eixo y
    # xPeriod e yPeriod juntos definem o ângulo das linhas
    
    lineTwist = rand.uniform(3.0, 5.0) # Grau de torção das linhas
    zoomFactor = 32.0

    
    for w in range(textureWidth):
        for h in range(textureHeight):
            xyValue = w * xPeriod / textureWidth + h * yPeriod / textureHeight + lineTwist * generateCloud(w,h,zoomFactor) / 256.0
            sineValue = int(226 * abs(math.sin(xyValue * 3.14159)))
            
            red = sineValue
            green = sineValue + 20
            blue = sineValue + 150
            image.putpixel((w,h),(red, green, blue))
    image.show()
    
def drawPicnic():
    color1 = generateColor()
    color2 = generateColor()
    size = rand.randint(8,60)
    side = textureWidth//size
    if(color1 == color2):
        while(color1 == color2):
            color1 = generateColor()
    
    for w in range(textureWidth):
        for h in range(textureHeight):
            if (((w+side)%size and (h+side))%size):
                red = int(color1[0]*256)
                green = int(color1[1]*256)
                blue = int(color1[2]*256)
            else:
                red = int(color2[0]*256)
                green = int(color2[1]*256)
                blue = int(color2[2]*256)
            image.putpixel((w,h),(red, green, blue))
    image.show()

    
def drawChess():
    color1 = generateColor()
    color2 = generateColor()
    side = rand.randint(8,20)
    if(color1 == color2):
        while(color1 == color2):
            color1 = selecionaCor()
    for w in range(textureWidth):
        for h in range(textureHeight):
            if (h%(textureHeight/side) > (textureHeight/side)/2):
                if (w%(textureWidth/side) > (textureWidth/side)/2):
                    red = int(color1[0]*256)
                    green = int(color1[1]*256)
                    blue = int(color1[2]*256)
                else:
                    red = int(color2[0]*256)
                    green = int(color2[1]*256)
                    blue = int(color2[2]*256)
                image.putpixel((w,h),(red, green, blue))
            else:
                if (w%(textureWidth/side) > (textureWidth/side)/2):
                    red = int(color2[0]*256)
                    green = int(color2[1]*256)
                    blue = int(color2[2]*256)
                else:
                    red = int(color1[0]*256)
                    green = int(color1[1]*256)
                    blue = int(color1[2]*256)
                image.putpixel((w,h),(red, green, blue))
    image.show()
    
def drawLines():
    color1 = generateColor()
    color2 = generateColor()
    size = rand.randint(2,60)
    side = textureWidth//size    
    if(color1 == color2):
        while(color1 == color2):
            color1 = selecionaCor()
    
    for w in range(textureWidth):
        for h in range(textureHeight):
            if (((w+h)%side)>(side/2)):
                red = int(color1[0]*256)
                green = int(color1[1]*256)
                blue = int(color1[2]*256)
            else:
                red = int(color2[0]*256)
                green = int(color2[1]*256)
                blue = int(color2[2]*256)
            image.putpixel((w,h),(red, green, blue))
    image.show()
    
    
def drawWood():
    xyPeriod = 12.0
    ringTwist = 0.1
    zoomFactor = 32.0
    for w in range(textureWidth):
        for h in range(textureHeight):
            xValue = (w - textureWidth / 2) / textureWidth
            yValue = (h - textureHeight / 2) / textureHeight
            distance = math.sqrt(xValue**2 + yValue**2) + ringTwist * generateCloud(w, h, zoomFactor) / 256.0
            sineValue = int(128.0 * abs(math.sin(2 * xyPeriod * distance * 3.14159)))
            
            red = sineValue + 80
            green = sineValue + 30
            blue = sineValue
            image.putpixel((w,h),(red, green, blue))
    image.show()
       

def drawTextureOfStyle(style): 
    generateNoise()
    if style == "noise":
        drawNoise()
    elif style == "smooth":
        drawSmooth()
    elif style == "pixels":
        drawPixelated()        
    elif style == "cloud":
        drawCloud()
    elif style == "marble":
        drawMarble()
    elif style == "wood":
        drawWood()
    elif style == "chess":
        drawChess()
    elif style == "lines":
        drawLines()
    elif style == "picnic":
        drawPicnic()   
    else:
        print("Undefined style")


# # Base image

# In[10]:


image = Image.open("square.png")
texture = []
textureWidth, textureHeight = image.size


# # Generate texture

# In[18]:


s = rand.randint(0,8)
style = type_textures[s]
drawTextureOfStyle(style)
# image.save("texture.png")

image = image.convert('RGB')
image.save("C:\\Users\\55219\\Documents\\Facul\\COMP_GRAF\\CG_DONE\\CG-ModernOpenGL\\src\\sphere_texture.jpg")

