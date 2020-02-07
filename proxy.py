from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import constants as co



def write_oracle_text(text, draw):

    #No differentiation between new lines for paragrahs irl and new lines that i put in for the wrap formatting. ie snapcaster should have
    #flash distinct from the second paragraph



    real_oracle_text=text.split('(')[0]
    print(real_oracle_text)
    reminder_text = '(' + text.split('(')[1]
    print('UMMM     '  + reminder_text)


    print()
    print()
    print()
    print()

    rules_font = ImageFont.truetype("./Templates/Fonts/MPlantin.ttf", co.RULES_FONT_SIZE)
    reminder_font = ImageFont.truetype("./Templates/Fonts/MPlantin-Italic.ttf", co.RULES_FONT_SIZE)

    # Breaks apart actual new paragraphs i.e. things that actually contained a new line first.
    # Then breaks apart each paragraph based on how many words can fit on an actual drawn line.
    current_line = 0
    current_paragraph = 0
    current_x = 0
    current_y_sum = 0
    final_y_sum = 0
    for count,line in enumerate(real_oracle_text.splitlines()):
        if line.strip() != '':
            print('LINE' + str(count))
            print(line)


        for count2, line2 in enumerate(textwrap.wrap(line, 42, break_long_words = False, replace_whitespace = False)):

            final_y_sum = current_y_sum

            line_size = draw.textsize(line2, font=rules_font)

            x_draw = co.RULES_TEXT_X_OFFSET
            y_draw = co.RULES_TEXT_Y_OFFSET + current_y_sum + current_paragraph * co.RULES_TEXT_PARAGRAPH_SPACE + co.RULES_TEXT_ADDITIONAL_SPACE*current_line


            draw.text((x_draw, y_draw), line2, (0, 0, 0), font=rules_font)
            current_y_sum += line_size[1]
            current_line += 1
            current_x = line_size[0]

            '''
            WORKING WAY:
            
            print('BREAK' + str(count2))
            print(line2)

            print(draw.textsize(line2, font=rules_font))
            #do we maybe add less rules text line width and more
            draw.text((co.RULES_TEXT_X_OFFSET, co.RULES_TEXT_Y_OFFSET + current_line * co.RULES_TEXT_LINE_WIDTH + current_paragraph*co.RULES_TEXT_PARAGRAPH_SPACE), line2, (0, 0, 0), font=rules_font)
            current_line += 1
            '''




        current_paragraph += 1

    draw.text((x_draw + line_size[0],y_draw),'(Reminder text.)', (0, 0, 0), font=reminder_font)





    '''
    #join everything that we find with a new line, which means everything we find should be an actual line on
    real_oracle_text = '\n'.join(['\n'.join(textwrap.wrap(line, 35, break_long_words=False, replace_whitespace=False)) for line in real_oracle_text.splitlines() if line.strip() != ''])

    nlines = real_oracle_text.count('\n')
    print(nlines)
    print(real_oracle_text)
    draw.text((margin, offset-nlines*32), real_oracle_text, (0, 0, 0), font=oracle_font, spacing=40)
    '''


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

def tricky_text(text):


    print()

def convert_cost(mana_cost):
    #https://www.pydanny.com/why-doesnt-python-have-switch-case.html#dispatch-methods-for-classes
    return_cost = ''
    for symbol in mana_cost:
        if symbol == '{' or symbol == '}':
            return_cost = return_cost
        elif symbol == 'W':
            return_cost += co.W_SYMBOL
        elif symbol == 'U':
            return_cost += co.U_SYMBOL
        elif symbol == 'B':
            return_cost += co.B_SYMBOL
        elif symbol == 'R':
            return_cost += co.R_SYMBOL
        elif symbol == 'G':
            return_cost += co.G_SYMBOL
        elif symbol == '1':
            return_cost += co.NUMBER_1_SYMBOL
        elif symbol == '2':
            return_cost += co.NUMBER_2_SYMBOL


    return return_cost



def proxy(art, card):



    try :
        choice = card['colors'][0]
    except:
        choice = 'Artifact'

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


    canvas=Image.new('RGBA', (co.FINAL_W, co.FINAL_H  ), (200,200,200,200))

    background = Image.open(backgrounda, 'r')
    background = background.resize((co.FINAL_W-150, co.FINAL_H-150), Image.NEAREST)

    w_color = int((co.FINAL_W-color.size[0])/2)
    h_color = int((co.FINAL_H-color.size[1] - 100)/2)

    w_background = int((co.FINAL_W-background.size[0])/2)
    h_background = int((co.FINAL_H-background.size[1])/2)

    w_art = int((co.FINAL_W-art.size[0])/2)
    h_art = int((co.FINAL_H-art.size[1])/2-620)

    w_titlebox = int((co.FINAL_W-titlebox.size[0])/2)
    h_titlebox = int((co.FINAL_H - titlebox.size[1]+20) / 2)



    canvas.paste(background, (w_background, h_background), background)
    canvas.paste(border, (0,0), border)
    canvas.paste(art, (w_art,h_art))
    canvas.paste(color, (w_color, h_color), color)
    canvas.paste(titlebox, (w_titlebox, h_titlebox), titlebox)

    draw = ImageDraw.Draw(canvas)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    title_font = ImageFont.truetype("./Templates/Fonts/Beleren2016-Bold.ttf", co.TITLE_FONT_SIZE)
    type_font = ImageFont.truetype("./Templates/Fonts/Beleren2016-Bold.ttf", co.TYPE_FONT_SIZE)
    rules_font = ImageFont.truetype("./Templates/Fonts/MPlantin.ttf", co.RULES_FONT_SIZE)
    mana_font = ImageFont.truetype("./Templates/Fonts/mana.ttf", co.MANA_FONT_SIZE)
    mana_cost = convert_cost(card['mana_cost'])
    mana_offset = (draw.textsize(mana_cost, font=mana_font))

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((co.TITLE_X, co.TITLE_Y), card['name'], (0, 0, 0), font=title_font)
    draw.text((co.TYPE_X, co.TYPE_Y), card['type_line'], (0, 0, 0), font=type_font)
    draw.text((co.MANA_X - mana_offset[0], co.MANA_Y), mana_cost, (0,0,0), font=mana_font)

    write_oracle_text(card['oracle_text'], draw)




    canvas.save('./out/' + card['name'] + '.png')


    #canvas.save('./out/' + card['name'] + '.png')