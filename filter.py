from PIL import Image, ImageDraw, ImageFont
import re
import sys
import os

def filterFor(filter):
    with open('words.txt', 'r') as wordsFile:
        words = []
        ## check for key in word
        for word in wordsFile.read().split():
            if filter in word:
                words.append(word)
    return sorted(words)


def textify(word='skills', key='kill'):
    ## split string into needed pieces and sort into list/var
    cutText = re.sub(f'{key}', ',', word)
    strList = []
    for subStr in cutText.split(','):
        strList.append(subStr)
    ## open file 
    img = Image.open('images/trustNobody.png')
    imgWidth, imgHeight = img.size
    ## set font and prepare image to write on
    font = ImageFont.truetype('arial.ttf', 40)
    write = ImageDraw.Draw(img)
    ## main word as header
    strWidth = font.getsize(word)[0]
    strHeight = font.getsize(word)[1]
    write.text(((imgWidth/2) - (strWidth/2), 0), word, font=font, fill=(255, 255, 255))
    ## first part of subString
    strWidth = font.getsize(strList[0])[0]  
    write.text((imgWidth - strWidth, 100), strList[0], font=font, fill=(255, 255, 255))
    ## second part of subString
    strWidth = font.getsize(strList[1])[0]
    write.text((125 - (strWidth/2), 90), strList[1], font=font, fill=(255, 255, 255))

    if not os.path.isdir(f'memes/{key}'):
        os.mkdir(f'memes/{key}')
    img.save(f'memes/{key}/{word}.png')


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        filter = arg
        words = filterFor(filter)
        for word in words:
            if word[-len(filter):] != filter and word[:len(filter)] != filter and '-' not in word:
                print(word) 
                textify(word=word, key=filter)
