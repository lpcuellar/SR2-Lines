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
        self.pixels[round(ver_x)][round(ver_y)] = self.current_color

    ##  this function is like glVertex bit instead it recieves coordinate pixels
    def glVertex_coordinate(self, x, y):
        self.pixels[x][y] = self.current_color

    ##  defines the color that will be used in glVertex
    def glColor(self, r, g, b):
        self.current_color = color(r, g, b)

    ##  draws a straight line from (x0, y0) through (x1, y1)
    def glLine(self, x0, y0, x1, y1):
            x0 = round(( x0 + 1) * (self.vp_width  / 2 ) + self.vp_x)
            x1 = round(( x1 + 1) * (self.vp_width  / 2 ) + self.vp_x)
            y0 = round(( y0 + 1) * (self.vp_height / 2 ) + self.vp_y)
            y1 = round(( y1 + 1) * (self.vp_height / 2 ) + self.vp_y)

            dx = x1 - x0
            dy = y1 - y0

            steep = abs(dy) > abs(dx)

            if steep:
                x0, y0 = y0, x0
                x1, y1 = y1, x1

            if x0 > x1:
                x0, x1 = x1, x0
                y0, y1 = y1, y0

            dx = abs(x1 - x0)
            dy = abs(y1 - y0)

            offset = 0
            limit = 0.5
            
            m = dy/dx
            y = y0

            for x in range(x0, x1 + 1):
                if(steep):
                    self.glVertex_coordinate(y, x)
                else:
                    self.glVertex_coordinate(x, y)

                offset += m
                if offset >= limit:
                    y += 1 if y0 < y1 else -1
                    limit += 1

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
