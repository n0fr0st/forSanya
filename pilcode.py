from PIL import Image, ImageDraw
from myCode import read1, read2

im = Image.new('RGB', (500, 500), color = ('#FAACAC'))

def my_pack(y=0, x=0):
    for i in read1:
        draw_text = ImageDraw.Draw(im)
        draw_text.text((50,50+y*50), i, fill=('#1c0606'))
        y+=1
    for i in read2:
        draw_text = ImageDraw.Draw(im)
        draw_text.text((150,50+x*50), i, fill=('#1c0606'))
        x+=1
    return im

def line_func(im):
    draw = ImageDraw.Draw(im)
    for i in read1:
        for j in read2:
            if i == j:
                draw.line(
                    xy = ((50, 50+read1.index(i)*50), (150, 50+read2.index(j)*50))
                )
    return im


line_func(my_pack()).show()