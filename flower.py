import turtle as tu
import re
import docx

source = "tulips"  

data = docx.Document("{}.docx".format(source))

# Lists to hold coordinates and colors
coordinates = []
colour = []

# Extract data from the Word document
for i in data.paragraphs:
    try:
        # Find all coordinate tuples in the text
        coord_stg_tup = re.findall(r"\(\-?\d+\.\d+, \-?\d+\.\d+\)", i.text)
        coord_num_tup = []

        # Find color values in the text
        color_val = re.findall(r'\d+\.\d+', coord_stg_tup[0])
        color_val_lst = [float(k) for k in color_val]
        colour.append(tuple(color_val_lst))

        # Convert coordinate strings to float tuples
        for j in coord_stg_tup:
            coord_pos = re.findall(r'\-?\d+\.\d+', j)
            coord_num_lst = [float(k) for k in coord_pos]
            coord_num_tup.append(tuple(coord_num_lst))

        coordinates.append(coord_num_tup)

    except:
        pass

# Initialize the Turtle
pen = tu.Turtle()
screen = tu.Screen()

# Hide the turtle and speed up the drawing
tu.tracer(2)
tu.hideturtle()
pen.speed(0)

# Start drawing the shapes based on the coordinates and colors
for i in range(len(coordinates)):
    draw = 1
    path = coordinates[i]
    col = colour[i]
    pen.color(col)
    pen.begin_fill()

    for order_pair in path:
        x, y = order_pair
        y = -1 * y  
        if draw:
            pen.up()
            pen.goto(x, y)
            pen.down()
            draw = 0
        else:
            pen.goto(x, y)

    pen.end_fill()
    pen.hideturtle()


screen.mainloop()

