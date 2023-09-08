import turtle

pen=turtle.Turtle()

def persegiPanjang(panjang, lebar, xpp, ypp):
    panjang=120
    lebar=80
    xpp=-550
    ypp=100
    pen.fillcolor("red")
    pen.begin_fill()
    pen.penup()
    pen.goto(xpp,ypp)
    pen.pendown()
    pen.forward(panjang)
    pen.right(90)
    pen.forward(lebar)
    pen.right(90)
    pen.forward(panjang)
    pen.right(90)
    pen.forward(lebar)
    pen.right(90)
    pen.end_fill()

def segitiga(sisit,sisim,xst,yst):
    sisit=75
    sisim=107
    xst=-550
    yst=-100
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.penup()
    pen.goto(xst,yst)
    pen.pendown()
    pen.forward(sisit)
    pen.right(90)
    pen.forward(sisit)
    pen.right(135)
    pen.forward(sisim)
    pen.right(135)
    pen.end_fill()

def trapesium(sisi1, sisi2, tinggi,xtp,ytp):
    sisi1=100
    sisi2=168
    tinggi=80
    xtp=-350
    ytp=100
    pen.fillcolor("green")
    pen.begin_fill()
    pen.penup()
    pen.goto(xtp,ytp)
    pen.pendown()
    pen.forward(sisi1)
    pen.right(65)
    pen.forward(tinggi)
    pen.right(115)
    pen.forward(sisi2)
    pen.right(115)
    pen.forward(tinggi)
    pen.right(65)
    pen.end_fill()

def jajargenjang(sisi, tinggi,xjg,yjg):
    sisi=120
    tinggi=100
    xjg=-350
    yjg=-100
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.penup()
    pen.goto(xjg,yjg)
    pen.pendown()
    pen.forward(sisi)
    pen.right(135)
    pen.forward(tinggi)
    pen.right(45)
    pen.forward(sisi)
    pen.right(135)
    pen.forward(tinggi)
    pen.right(45)
    pen.end_fill()

def segilima(sisi,xsl,ysl):
    sisi=60
    xsl=-150
    ysl=100
    pen.fillcolor("purple")
    pen.begin_fill()
    pen.penup()
    pen.goto(xsl,ysl)
    pen.pendown()
    pen.forward(sisi)
    pen.right(75)
    pen.forward(sisi)
    pen.right(71)
    pen.forward(sisi)
    pen.right(71)
    pen.forward(sisi)
    pen.right(75)
    pen.forward(sisi)
    pen.end_fill()


persegiPanjang(120, 80, -250, 200)
segitiga(75, 107, 0, 200)
trapesium(100, 125, 100, 250, 200)
jajargenjang(120, 100, 200, 0)
segilima(65, 65, 65)

turtle.done()