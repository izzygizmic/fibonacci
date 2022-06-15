import math
import turtle

unit=5 #tällä muuttujalla säädän piirrettävän kuvion kokoa
a=0
b=1
k=1
s=0
turtle.bgcolor("black")
dmb=turtle.Pen()
dmb.color("green")
#fibonaccin lukusarja tallennetaan tähän
nums = []

#ruudukon nopeus
dmb.speed(1)
dmb.hideturtle()

#kaaren alku
qmp=turtle.Pen()
qmp.hideturtle()
qmp.pensize(2)
qmp.speed(3)
qmp.color("red")
qmp.penup()
qmp.forward(unit)
qmp.right(270)
qmp.pendown()
qmp.circle(b*unit , 180)
qmp.penup()
qmp.left(90)
qmp.forward(2*unit)
qmp.pendown()
#ruudukon alku eli 1x1 laatikot
#1
dmb.forward(b*unit)
dmb.left(90)
#2
dmb.forward(b*unit)
dmb.left(90)
#3
dmb.forward(b*unit)
dmb.left(90)
#4
dmb.forward(b*unit)
dmb.left(180)
a=a+b
#1
dmb.forward(a*unit)
dmb.left(90)
#2
dmb.forward(a*unit)
dmb.left(90)
#3
dmb.forward(a*unit)
dmb.left(90)
#4
dmb.forward(a*unit)
dmb.left(180)
dmb.forward(a*unit)
dmb.left(90)
#nopeutus
dmb.speed(0)

#piirtää ruudukon ja kasaa lukujonon
#fibonaccin lukujono muodostuu muuttujilla a & b. summataan molemmat a ja b vuorotellen a:n arvoksi ja sitten B:n arvoksi ja ne kerätään 
# lukujonoon nums 
while b<100:
    b=a+b
    while k<5: #tämä luuppi piirtää ruudun
        dmb.forward(b*unit)
        dmb.left(90)
        k+=1
    nums.append(b)
    dmb.right(180)
    dmb.forward(a*unit)
    dmb.left(90)
    k=1
    a=a+b
    nums.append(a)
    while k<5: #tämäkin luuppi piirtää ruudun
        dmb.forward(a*unit)
        dmb.left(90)
        k+=1
    k=1
    dmb.right(180)
    dmb.forward(b*unit)
    dmb.left(90)
    print(nums)



#spiraalin toteuttava luuppi
#kaaren säde tulee nums lukujonosta josta seuraava arvo otetaan aina kun kaarta on tehty edellisellä arvolla 90 astetta
qmp.left(90)
while s<14:
    qmp.circle(nums[s]*unit, -90)
    s+=1


#Projektiin liittyy kilpikonnat määrittävät vakiot ja niitä ohjaavat muuttujat.
#Loopilla muodostuu ruudukko ja sen ohessa listaan tulee lukujonon jäsenet.
#Ympyrän piirtosuunta vaihtuu ensimmäisten kahden ruudun jälkeen
#lukujono tulostuu konsoliin










