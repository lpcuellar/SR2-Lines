##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR1: Points
##  LUIS PEDRO CUÉLLAR - 18220
##

##  import gl library for drawing
from gl import Render, color

##  the variables that will be used along the program are declare down below
title = "---    ESCRITOR DE IMÁGENES BMP    ---\n"
intro_msg = "\nPrimero, hay que definir el tamaño de la imagen!"
set_width = "\nIngrese el número de pixeles de largo (width): "
set_height = "Ingrese el número de pixeles de alto (height): "

menu = """\nOpciones:
        1. Modificar el color al fondo de la imagen
        2. Modificar ViewPort
        3. Dibujar un punto en la imagen
        4. Dibujar una línea en la imagen
        5. Guardar imagen
        6. Salir

        Ingrese la opcion que desea realizar: """

draw_point_menu = """\nOpciones para dibujar un punto en la imagen:
        1. Cambiar color (default = blanco)
        2. Escoger coordenadas dentro de la imagen

        Ingrese la opcion que desea realizar: """

draw_line_menu = """\nOpciones para dibujar una línea en la imagen:
        1. Cambiar color (default = blanco)
        2. Escoger coordenadas dentro de la imagen

        Ingrese la opcion que desea realizar: """

wants_to_continue = True
wants_to_change_size = True
is_values_ok = False
width = 0
height = 0
red = 0
green = 0
blue = 0
vp_x = 0
vp_y = 0
vp_width = 0
vp_height = 0
filename = "output.bmp"

##  starts the program showing the title and some instructions
print(title)
input("Apache enter para continuar...")

print(intro_msg)
input("Apache enter para continuar...")

##  starts the loop that will show the possible options that can be made to the image
while(wants_to_continue):
    if(wants_to_change_size):
        is_values_ok = False

        ##  check if the values are ok so it can move on
        while(is_values_ok == False):
            width = input(set_width)
            width = int(width)
            height = input(set_height)
            height = int(height)

            if((width < 0) or (height < 0)) :
                print("\nPor favor escoger valores mayores que 0\n")
            else:
                wants_to_change_size = False
                is_values_ok = True

                ##  create the window for the image
                render = Render(width, height)

    ##    prints the menu with his options
    print(menu)
    option = input()
    option = int(option)

    ##  this options ask the user what color does he wants for his background
    if(option == 1):
        is_values_ok = False

        ## ask the values for the rgb and check that they are valid
        while(is_values_ok == False):
            red = input("Ingrese el valor r del color deseado (de 0 a 1): ")
            red = float(red)
            green = input("Ingrese el valor g del color deseado (de 0 a 1): ")
            green = float(green)
            blue = input("Ingrese el valor b del color deseado (de 0 a 1): ")
            blue = float(blue)

            if((red < 0 or red > 1) or (green < 0 or green > 1) or (blue < 0 or blue > 1)):
                print("\nPor favor escoger valores entre 0 y 1\n")
            else:
                is_values_ok = True

                ##  puts the background color to the image
                render.glClearColor(red, green, blue)

    ## asks the user about the viewport that wants to create
    elif(option == 2):
        is_values_ok = False

        ##  ask the values and check if they´re valid
        while(is_values_ok == False):
            vp_x = input("Ingrese la coordenada en x: ")
            vp_x = int(vp_x)
            vp_y = input("Ingrese la coordenada en y: ")
            vp_y = int(vp_y)

            vp_width = input("Ingrese el ancho del ViewPort (width): ")
            vp_width = int(vp_width)
            vp_height = input("Ingrese el alto del ViewPort (height): ")
            vp_height = int(vp_height)

            if((vp_x < 0) or (vp_y < 0) or (vp_width < 0) or (vp_height < 0)):
                print("\nPor favor escoger valores mayores que 0\n")
            elif((vp_x >= width) or (vp_y >= height)):
                print("\nLos valores escogidos son más grandes que la imagen\n")
            elif((vp_x + vp_width >= width) or (vp_y + vp_height >= height)):
                print("\nLos valores escogidos son más grandes que la imagen\n")
            else:
                is_values_ok = True

                ## create the viewport with the values given above
                render.glViewPort(vp_x, vp_y, vp_width, vp_height)

    ## this option is for drawing a point on the image, it can also change the color of the point
    elif(option == 3):

        ##  asks if the user wants to change the color or draw the point
        print(draw_point_menu)
        point_option = input()
        point_option = int(point_option)

        ## this option will change the color with the given values, also it validates them
        if(point_option == 1):
            is_values_ok = False

            while(is_values_ok == False):
                red = input("Ingrese el valor r del color deseado (de 0 a 1): ")
                red = float(red)
                green = input("Ingrese el valor g del color deseado (de 0 a 1): ")
                green = float(green)
                blue = input("Ingrese el valor b del color deseado (de 0 a 1): ")
                blue = float(blue)

                if((red < 0 or red > 1) or (green < 0 or green > 1) or (blue < 0 or blue > 1)):
                    print("\nPor favor escoger valores entre 0 y 1\n")
                else:
                    is_values_ok = True

                    ##  uses this function to change the default color of the point drawn
                    render.glColor(red, green, blue)

        elif(point_option == 2):
            is_values_ok = False

            ##  asks the coordinates in which the user wants the point to be drawn
            while(is_values_ok == False):
                point_x = input("Ingrese un valor en x relativo al  ViewPort (entre -1 y 1): ")
                point_x = float(point_x)
                point_y = input("Ingrese un valor en y relativo al  ViewPort (entre -1 y 1): ")
                point_y = float(point_y)

                ##  it validates the coordinates given above
                if((point_x < -1 or point_x > 1) or (point_y < -1 or point_y > 1)):
                    print("\nPor favor escoger valores entre -1 y 1\n")
                else:
                    is_values_ok = True

                    ##  this function draws the point into the image
                    render.glVertex(point_x, point_y)

        else:
            print("Por favor escoja una opción válida!")

    ## this option is for drawing a line on the image, it can also change the color of the line
    elif(option == 4):

        ##  asks if the user wants to change the color or draw the line
        print(draw_line_menu)
        line_option = input()
        line_option = int(line_option)

        ## this option will change the color with the given values, also it validates them
        if(line_option == 1):
            is_values_ok = False

            while(is_values_ok == False):
                red = input("Ingrese el valor r del color deseado (de 0 a 1): ")
                red = float(red)
                green = input("Ingrese el valor g del color deseado (de 0 a 1): ")
                green = float(green)
                blue = input("Ingrese el valor b del color deseado (de 0 a 1): ")
                blue = float(blue)

                if((red < 0 or red > 1) or (green < 0 or green > 1) or (blue < 0 or blue > 1)):
                    print("\nPor favor escoger valores entre 0 y 1\n")
                else:
                    is_values_ok = True

                    ##  uses this function to change the default color of the point drawn
                    render.glColor(red, green, blue)

        elif(line_option == 2):
            is_values_ok = False

            ##  asks the coordinates in which the user wants the point to be drawn
            while(is_values_ok == False):
                x0 = input("Ingrese un valor inicial en x relativo al  ViewPort (entre -1 y 1): ")
                x0 = float(x0)
                y0 = input("Ingrese un valor inicial en y relativo al  ViewPort (entre -1 y 1): ")
                y0 = float(y0)

                x1 = input("Ingrese un valor final en x relativo al  ViewPort (entre -1 y 1): ")
                x1 = float(x1)
                y1 = input("Ingrese un valor final en y relativo al  ViewPort (entre -1 y 1): ")
                y1 = float(y1)

                ##  it validates the coordinates given above
                if((x0 < -1 or x0 > 1) or (y0 < -1 or y0 > 1) or (x1 < -1 or x1 > 1) or (y1 < -1 or y1 > 1)):
                    print("\nPor favor escoger valores entre -1 y 1\n")
                else:
                    is_values_ok = True

                    ##  this function draws the line into the image
                    render.glLine(x0, y0, x1, y1)
        else:
            print("Por favor escoja una opción válida!")

    ##      this function saves all the data edited above and writes all the changes into the image
    elif(option == 5):
        render.glFinish(filename)

    ##  this option will let you quit the program, it has a warnin message before quitting
    elif(option == 6):
        print("Si se sale del programa y no ha guardado la imagen no se notará ningún cambio!")
        exit = input("Desea salir del programa? (Si o No): ")

        if(exit.upper() == "SI"):
            wants_to_continue = False
        elif(exit.upper() != "NO"):
            print("Por favor escoja una opción válida!")

    else:
        print("Por favor escoja una opción válida!")

print("BYEEEEE")
