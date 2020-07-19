##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR1: Points
##  LUIS PEDRO CUÉLLAR - 18220
##

import struct

##  char --> 1 byte
def char(var):
    return struct.pack('=c', var.encode('ascii'))

##  word --> 2 byte
def word(var):
    return struct.pack('=h', var)

##  dword --> 4 byte
def dword(var):
    return struct.pack('=l', var)

##  returns rgb color in bytes
def color(r, g, b):
    return bytes([int(r * 255), int(g * 255), int(b * 255)])

class Render(object):
    def __init__(self, width, height, background = None):
        self.glInit(width, height, background)

    ##  starts the object so the image can render
    def glInit(self, width, height, background):
        self.width = width
        self.height = height

        if (background == None):
            self.current_color = color(1, 1, 1)
        else:
            self.bg_color = background
            self.glClear(self.bg_color)

    ##  starts framebuffer with a ceratin size(width * height)
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    ##  defines an area in which we can draw
    def glViewPort(self, x, y, width, height):
        self.vp_x = x
        self.vp_y = y
        self.vp_width = width
        self.vp_height = height

    ##  puts a background color to the bitmap
    def glClear(self, background):
        self.bg_color = background
        self.pixels = [[ self.bg_color for x in range(self.width)] for y in range(self.height)]

    ##  changes the background color asigned in glClear
    def glClearColor(self, r, b, g):
        self.r = r
        self.g = g
        self.b = b

        self.bg_color = color(self.r, self.g, self.b)

        self.glClear(self.bg_color)

    ##  changes the color of a point in the area defined in glViewPort
    ##  the color used in this function is defined in glColor
    def glVertex(self, x, y):
        ver_x = int(((x + 1) * (self.vp_width / 2)) + self.vp_x)
        ver_y = int(((y + 1) * (self.vp_height / 2)) + self.vp_y)
        self.pixels[ver_x][ver_y] = self.current_color

    ##  defines the color that will be used in glVertex
    def glColor(self, r, g, b):
        self.current_color = color(r, g, b)

    ##  this function is used to write the image into the file
    def glFinish(self, filename):
        file = open(filename, 'wb')

        ##  file header --> 14 bytes
        file.write(bytes('B'.encode('ascii')))
        file.write(bytes('M'.encode('ascii')))

        file.write(dword(14 + 40 + self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(14 + 40))

        ##  image header --> 40 bytes
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width * self.height * 3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        ##  pixels --> 3 bytes each

        for x in range(self.height):
            for y in range(self.width):
                file.write(self.pixels[x][y])


        file.close()
