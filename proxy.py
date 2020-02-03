from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap


ART = '../art2.jpg'
FINAL_H=3744
FINAL_W=2688
COLOR_CHOICE = 'B'
COLOR_OFFSET = 0
COLOR = '../Templates/Colors/' + COLOR_CHOICE + '.png'
BACKGROUND = '../Templates/Backgrounds/' + COLOR_CHOICE + '.png'
BORDER = '../Templates/Border.png'

def write_oracle_text(text, draw):

    #No differentiation between new lines for paragrahs irl and new lines that i put in for the wrap formatting. ie snapcaster should have
    #flash distinct from the second paragraph
    margin = 240 
    offset = 2570

    oracle_font = ImageFont.truetype(r"C:\Users\teved\AppData\Local\Microsoft\Windows\Fonts\MPlantin.ttf", 130)

    real_oracle_text=text.split('(')[0]
    

    real_oracle_text = '\n'.join(['\n'.join(textwrap.wrap(line, 35,
                break_long_words=False, replace_whitespace=False))
                for line in real_oracle_text.splitlines() if line.strip() != ''])

    nlines = real_oracle_text.count('\n')
    print(nlines)
    print(real_oracle_text)
    draw.text((margin, offset-nlines*32), real_oracle_text, (0, 0, 0), font=oracle_font, spacing=40)


'''
    try:


        reminder_oracle_text=text.split('(')[1]
        
        reminder_oracle_text = '\n'.join(['\n'.join(textwrap.wrap(line, 35,
                    break_long_words=False, replace_whitespace=False))
                    for line in reminder_oracle_text.splitlines() if line.strip() != ''])

        
        draw.text((margin, offset-nlines*40), reminder_oracle_text, (100, 100, 100), font=oracle_font, spacing=40)
    
    except:
        print('skip')



    
    
    margin = 240 
    offset = 2570
    for line in textwrap.wrap(text, width=35,break_long_words=False,replace_whitespace=False):
        draw.text((margin, offset), line, (0, 0, 0), font=oracle_font)
        offset += oracle_font.getsize(line)[1]
    '''


def proxy(art, card):


    choice = card['colors'][0]
    colora = '../Templates/Colors/' + choice + '.png'
    backgrounda = '../Templates/Backgrounds/' + choice + '.png'

    art = Image.open('./art.png')


    color = Image.open(colora, 'r')
    #color = makeTrans(color)
    color_w, color_h = color.size

    border = Image.open('../Templates/Border.png', 'r')
    #border = makeTrans(border)

    art = art.resize((2300,1680))

    titlebox = Image.open('../Templates/TitleBox/' + choice + '.png')


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
    #title_font = ImageFont.truetype("Beleren2016-Bold.ttf", 160)
    #type_font =     ImageFont.truetype("Beleren2016-Bold.ttf", 140)
    #rules_font =    ImageFont.truetype("MPlantin.ttf", 140)

    title_font = ImageFont.truetype(r"C:\Users\teved\AppData\Local\Microsoft\Windows\Fonts\Beleren2016-Bold.ttf", 160)
    type_font =     ImageFont.truetype(r"C:\Users\teved\AppData\Local\Microsoft\Windows\Fonts\Beleren2016-Bold.ttf", 140)
    

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((220, 225), card['name'], (0, 0, 0), font=title_font)
    draw.text((220, 2160), card['type_line'], (0, 0, 0), font=type_font)

    write_oracle_text(card['oracle_text'], draw)
    



    canvas.save('./out/' + card['name'] + '.png')


    #canvas.save('./out/' + card['name'] + '.png')