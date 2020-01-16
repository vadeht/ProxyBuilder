from PIL import Image

ART = '../art.jpg'
COLOR_CHOICE = 'U'
COLOR_OFFSET = 0
COLOR = '../templates/Colors/' + COLOR_CHOICE + '.png'
BACKGROUND = '../templates/Backgrounds' + COLOR_CHOICE + '.png'
BORDER = '../templates/Border.png'

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

def makeTrans(img):
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    return img

art = Image.open(ART)

color = Image.open(COLOR, 'r')
color = makeTrans(color)
color_w, color_h = color.size

border = Image.open('../templates/Border.png', 'r')
borderr = border.resize((color_w+250,color_h+400), Image.NEAREST)
art=art.resize(borderr.size)
borderr=makeTrans(borderr)
border_w, border_h = borderr.size
background = Image.open('../templates/Backgrounds/Gold.png', 'r')
background = background.resize((border_w, border_h), Image.NEAREST)
background.paste(borderr, (0,0), borderr.convert('RGBA'))
w = int(proper_round((border_w-img_w)/2, 0))
h = int(proper_round((border_h-img_h)/2, 0))
background.paste(img, (w, h), img.convert('RGBA'))

background.save('hope.png')