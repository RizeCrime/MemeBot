from PIL import Image, ImageDraw, ImageFont
import re
import sys
import os
import time
import random


def filterFor(filter):
    with open('words.txt', 'r') as wordsFile:
        words = []
        ## check for key in word
        for word in wordsFile.read().split():
            if filter in word:
                words.append(word)
    return sorted(words)


def getTemplate(template):
    ## add your own template:
    templates = {
        # '<templateName>': {
        #     'image': 'images/<imageName>.png', 
        #     'text1': lambda imgWidth=None, strWidth=None: (imgWidth - strWidth, 100),
        #     'text2': lambda imgWidth=None, strWidth=None: (125 - (strWidth/2), 90),
        #     'font': ImageFont.truetype('<font>', <font size in pixels>)
        # },
        'wildcard': {
            'image': 'images/wildcard.png',
            'text1': lambda imgWidth=None, strWidth=None: (320 - (strWidth/2), 215),
            'text2': lambda imgWidth=None, strWidth=None: (750 - (strWidth/2), 300),
            'font': lambda imgHeight=None: ImageFont.truetype('arial.ttf', int((imgHeight/100 * 12))),
            'color': (255, 255, 255)
        },
        'trustNobody': {
            'image': 'images/trustNobody.png', 
            'text1': lambda imgWidth=None, strWidth=None: ((imgWidth - strWidth), 100),
            'text2': lambda imgWidth=None, strWidth=None: (125 - (strWidth/2), 90),
            'font': lambda imgHeight=None: ImageFont.truetype('arial.ttf', int((imgHeight/100 * 13))),
            'color': (255, 255, 255)
        },
        'stab': {
            'image': 'images/stab.png',
            'text1': lambda imgWidth=None, strWidth=None: (imgWidth - strWidth - 30, 265),
            'text2': lambda imgWidth=None, strWidth=None: (150 - (strWidth/2), 230),
            'font': lambda imgHeight=None: ImageFont.truetype('arial.ttf', int((imgHeight/100 * 12))),
            'color': (255, 255, 255)
        },
        'hug': {
            'image': 'images/hug.png',
            'text1': lambda imgWidth=None, strWidth=None: (390 - (strWidth/2), 175),
            'text2': lambda imgWidth=None, strWidth=None: (260 - (strWidth/2), 300),
            'font': lambda imgHeight=None: ImageFont.truetype('arial.ttf', int((imgHeight/100 * 12))),
            'color': (255, 255, 255)
        },
        'tag': {
            'image': 'images/tag.jpg',
            'text1': lambda imgWidth=None, strWidth=None: (370 - (strWidth/2), 300),
            'text2': lambda imgWidth=None, strWidth=None: (680 - (strWidth/2), 300),
            'font': lambda imgHeight=None: ImageFont.truetype('arial.ttf', int((imgHeight/100 * 12))),
            'color': (0, 0, 0)
        },
    }

    if template in templates:
        return templates[template]
    else:
        # return random.choice(templates)
        return templates['wildcard']


def textify(word='skills', key='kill'):
    ## split string into needed pieces and sort into list/var
    cutText = re.sub(f'{key}', ',', word)
    strList = []
    for subStr in cutText.split(','):
        strList.append(subStr)

    ## get template
    if strList[0] == strList[1]:
        template = getTemplate('trustNobody')
    else:
        template = getTemplate(key)
    

    ## open file 
    img = Image.open(template['image'])
    imgWidth, imgHeight = img.size
    ## set font and prepare image to write on
    font = template['font'](imgHeight)
    write = ImageDraw.Draw(img)

    ## main word as header
    strWidth = font.getsize(word)[0]
    strHeight = font.getsize(word)[1]
    write.text(((imgWidth/2) - (strWidth/2), 0), word, font=font, fill=(template['color']))

    ## first part of subString
    strWidth = font.getsize(strList[1])[0] 
    write.text(template['text1'](imgWidth, strWidth), strList[0], font=font, fill=(template['color']))
    ## second part of subString
    strWidth = font.getsize(strList[1])[0] 
    write.text(template['text2'](imgWidth, strWidth), strList[1], font=font, fill=(template['color']))

    if not os.path.isdir('memes'):
        os.mkdir('memes')
    if not os.path.isdir(f'memes/{key}'):
        os.mkdir(f'memes/{key}')
    img.save(f'memes/{key}/{word}.png')


if __name__ == '__main__':
    sTime = time.time()
    memes = 0
    for arg in sys.argv[1:]:
        filter = arg
        words = filterFor(filter)
        for word in words:
            if word[-len(filter):] != filter and word[:len(filter)] != filter and '-' not in word:
                print(filter, word) 
                textify(word=word, key=filter)
                memes += 1
    eTime = time.time()
    print(f'Generated {memes} memes in {eTime-sTime} seconds.')

