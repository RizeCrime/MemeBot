from PIL import Image, ImageDraw, ImageFont
import re 

def textify(word='skills', key='kill'):
    cutText = re.sub(f'{key}', ',', word)
    strList = []
    for subStr in cutText.split(','):
        strList.append(subStr)

    img = Image.open('images/trustNobody.png')
    width, height = img.size

    font = ImageFont.truetype('arial.ttf', 60)
    write = ImageDraw.Draw(img)
    
    write.text((110, 90), strList[0], font=font, fill=(255, 255, 255))
    write.text((425, 100), strList[1], font=font, fill=(255, 255, 255))

    img.save(f'memes/{word}.png')

if __name__ == '__main__':
    textify()
