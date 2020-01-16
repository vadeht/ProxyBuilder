from PIL import Image

ART = '../art2.jpg'
FINAL_H=3744
FINAL_W=2688
COLOR_CHOICE = 'B'
COLOR_OFFSET = 0
COLOR = '../templates/Colors/' + COLOR_CHOICE + '.png'
BACKGROUND = '../templates/Backgrounds/' + COLOR_CHOICE + '.png'
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

def proxy(art, card):


    choice = card['colors'][0]
    colora = '../templates/Colors/' + choice + '.png'
    backgrounda = '../templates/Backgrounds/' + choice + '.png'

    art = Image.open('./art.png')


    color = Image.open(colora, 'r')
    color = makeTrans(color)
    color_w, color_h = color.size

    border = Image.open('../templates/Border.png', 'r')
    border = makeTrans(border)

    art = art.resize((2300,1680))


    canvas=Image.new('RGBA', (FINAL_W, FINAL_H  ), (200,200,200,200))

    background = Image.open(backgrounda, 'r')
    background = background.resize((FINAL_W-150, FINAL_H-150), Image.NEAREST)

    w_color = int(proper_round((FINAL_W-color.size[0])/2, 0))
    h_color = int(proper_round((FINAL_H-color.size[1])/2, 0))

    w_background = int(proper_round((FINAL_W-background.size[0])/2, 0))
    h_background = int(proper_round((FINAL_H-background.size[1])/2, 0))

    w_art = int(proper_round((FINAL_W-art.size[0])/2, 0))
    h_art = int(proper_round((FINAL_H-art.size[1])/2-568, 0))


    canvas.paste(background, (w_background, h_background), background.convert('RGBA'))
    canvas.paste(border, (0,0), border.convert('RGBA'))
    canvas.paste(art, (w_art,h_art))
    canvas.paste(color, (w_color, h_color), color.convert('RGBA'))


    canvas.save('./out/' + card['name'] + '.png')