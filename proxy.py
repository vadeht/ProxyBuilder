from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


ART = './art2.jpg'
FINAL_H=3744
FINAL_W=2688
COLOR_CHOICE = 'B'
COLOR_OFFSET = 0
COLOR = './Templates/New/Box/' + COLOR_CHOICE + '.png'
BACKGROUND = './Templates/New/Backgrounds/' + COLOR_CHOICE + '.png'
BORDER = './Templates/New/Border.png'

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
    colora = './Templates/New/Box/' + choice + '.png'
    backgrounda = './Templates/New/Background/' + choice + '.png'

    art = Image.open('./art.png')


    color = Image.open(colora, 'r')
    #color = makeTrans(color)
    color_w, color_h = color.size

    border = Image.open('./Templates/New/Border/Border.png', 'r')
    #border = makeTrans(border)

    art = art.resize((2300,1680))

    titlebox = Image.open('./Templates/New/Title/' + choice + '.png')


    canvas=Image.new('RGBA', (FINAL_W, FINAL_H  ), (200,200,200,200))

    background = Image.open(backgrounda, 'r')
    background = background.resize((FINAL_W-150, FINAL_H-150), Image.NEAREST)

    w_color = int((FINAL_W-color.size[0])/2)
    h_color = int((FINAL_H-color.size[1] - 100)/2)

    w_background = int((FINAL_W-background.size[0])/2)
    h_background = int((FINAL_H-background.size[1])/2)

    w_art = int((FINAL_W-art.size[0])/2)
    h_art = int((FINAL_H-art.size[1])/2-620)

    w_titlebox = int((FINAL_W-titlebox.size[0])/2)
    h_titlebox = int((FINAL_H - titlebox.size[1]+20) / 2)



    canvas.paste(background, (w_background, h_background), background)
    canvas.paste(border, (0,0), border)
    canvas.paste(art, (w_art,h_art))
    canvas.paste(color, (w_color, h_color), color)
    canvas.paste(titlebox, (w_titlebox, h_titlebox), titlebox)

    draw = ImageDraw.Draw(canvas)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    title_font = ImageFont.truetype("./Templates/Fonts/Beleren2016-Bold.ttf", 160)
    type_font =     ImageFont.truetype("./Templates/Fonts/Beleren2016-Bold.ttf", 140)
    rules_font =    ImageFont.truetype("./Templates/Fonts/MPlantin.ttf", 140)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((220, 225), card['name'], (0, 0, 0), font=title_font)
    draw.text((220, 2160), card['type_line'], (0, 0, 0), font=type_font)
    draw.text((240, 2570), card['oracle_text'], (0, 0, 0), font=rules_font)



    canvas.save('./out/' + card['name'] + '.png')


    #canvas.save('./out/' + card['name'] + '.png')