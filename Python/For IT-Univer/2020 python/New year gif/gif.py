from PIL import Image, ImageDraw#, ImageFilter, ImageOps, ImageFont

list_image = []
fon = Image.open('room.jpg')
fon.thumbnail((800,800))

list_image.append(fon)

fon = fon.copy()

elka = Image.open('elka1.png')
elka.thumbnail((400,400))


#fon.show()
#elka.show()
pos = (270, 70)
fon.paste(elka, pos, elka)

list_image.append(fon)

fon = fon.copy()


mish = Image.open('mishura2.png')
mish = mish.resize(elka.size)# podognaty pod rasmer elka

fon.paste(mish, pos, mish)
list_image.append(fon)

fon = fon.copy()

pix = mish.load()

draw = ImageDraw.Draw(mish)

for k in range(20):
    for i in range(mish.width):
        for j in range(mish.height):
            r,g,b,a = pix[i, j]
            r = (r + 3 * k) % 255
            g = (g + 7 * k) % 255
            b = (b + 8 * k) % 255 
            
            draw.point((i,j),(r,g,b,a))
            #list_image.append(mish)
            #fon = fon.copy()
    fon.paste(mish, pos, mish)
    list_image.append(fon)
    fon = fon.copy()
#deer = Image.open("deer.png")
#deer.thumbnail((300,300))


#posdeer = (260, 50)
#fon.paste(deer, posdeer, deer)
#list_image.append(deer)
fon = fon.copy()
fon.save('Gifka.gif', 'GIF',\
         save_all = True, \
         append_images = list_image,\
         duration = [0,1000,1000,1000] + [150]* 20 + [1000], loop = 0 )





































































































































