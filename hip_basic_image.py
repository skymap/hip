from PIL import Image, ImageDraw
import math
w = 1080
h = 540
a = -1 / (2 * math.sqrt(math.pi))
im = Image.new('RGB', (w, h), (0, 0, 0))
draw = ImageDraw.Draw(im)
c8 = [[136, 204, 255], [187, 238, 255], [238, 255, 255], [255, 255, 255], [255, 255, 238], [255, 238, 187], [255, 204, 136], [255, 153, 85]]
r = open('hip_basic.csv', 'r')
src = r.read()
r.close
rows = src.split('\n')
for row in rows:
    d = row.split(',')
    if len(d[0]) > 0:
        x = int(w * (360 - float(d[1])) / 360)
        y = int(h * (90 - float(d[2])) / 180)
        m = int(d[3])
        c = c8[int(d[4])]
        if m < 6:
            mm = math.exp((m + 1) * a)
            c0 = int(c[0] * mm)
            c1 = int(c[1] * mm)
            c2 = int(c[2] * mm)
            draw.point((x - 1, y), (c0, c1, c2))
            draw.point((x + 1, y), (c0, c1, c2))
            draw.point((x, y - 1), (c0, c1, c2))
            draw.point((x, y + 1), (c0, c1, c2))
        mm = math.exp(m * a)
        c0 = int(c[0] * mm)
        c1 = int(c[1] * mm)
        c2 = int(c[2] * mm)
        draw.point((x, y), (c0, c1, c2))
im.save('hip_basic.png')