# Turtle kütüphanesi ile resim çiziyoruz
import turtle

ucgen = turtle.Turtle()
# kalem nesnesine renk verdik
ucgen.pencolor("red")
# kalem nesnesinin boyutunu(kalınlıgını )belirleme
ucgen.pensize(2)
# Kalem nesnesine hız verelim
ucgen.speed(7)
# Döngü iel çizgileri uzunluk ve açı ile çizdirelim

for i in range(41):
    ucgen.forward(300)
    ucgen.right(123)
    
turtle.done()


