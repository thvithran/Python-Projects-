import turtle as t

def spiral(sides,trun,color,width):
    pen = t.Turtle()
    pen.color(color)
    pen.width(width)
    pen.speed(5)
    for n in range(sides):
        pen.forward(n)
        pen.right(trun)
spiral(200,45,"red",5)