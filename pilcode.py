from PIL import Image, ImageDraw
from myCode import read1, read2

im = Image.new('RGB', (500, 500), color = ('#FAACAC'))

def my_pack()->im:
    for i in read1:
        draw_text = ImageDraw.Draw(im)
        draw_text.text((50,50+read1.index(i)*50), i, fill=('#1c0606'))
    for j in read2:
        draw_text = ImageDraw.Draw(im)
        draw_text.text((150,50+read2.index(j)*50), j, fill=('#1c0606'))
    return im

def line_func(im)->im:
    draw = ImageDraw.Draw(im)
    for i in read1:
        for j in read2:
            if i == j:
                draw.line(
                    xy = ((50, 50+read1.index(i)*50), (150, 50+read2.index(j)*50))
                )
    return im


line_func(my_pack()).show()