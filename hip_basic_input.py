r = open('hip_src.tsv', 'r')
src = r.read()
r.close
w = open('hip_basic.dat', 'w+b')
src = src.replace(' ', '')
rows = src.split('\n')
dst = bytearray()
for row in rows:
    d = row.split('|')
    if len(d[0]) > 0 and len(d[1]) > 0 and len(d[2]) > 0 and len(d[3]) > 0 and len(d[4]) > 0 and len(d[5]) > 0 and len(d[6]) > 0 and len(d[7]) > 0 and len(d[8]) > 0 and len(d[9]) > 0 and len(d[10]) > 0:
        ra = float(d[0])
        de = float(d[1])
        des = -1 if de < 0 else 1
        de = abs(de)
        rai = int(ra)
        dei = int(de)
        rad = round((ra - rai) * 4095)
        ded = round((de - dei) * 4095)
        rd = (89 - dei) if des < 0 else (dei + 90)
        rd = rd + rai * 180
        hip = int(d[2])
        mag = int(float(d[8]) + 1.0876)
        b = float(d[9])
        if b < -0.3:
            sp = 0
        elif b >= -0.3 and b < 0.0:
            sp = 1
        elif b >= 0.0 and b < 0.3:
            sp = 2
        elif b >= 0.3 and b < 0.6:
            sp = 3
        elif b >= 0.6 and b < 0.9:
            sp = 4
        elif b >= 0.9 and b < 1.5:
            sp = 5
        elif b >= 1.5 and b < 2.1:
            sp = 6
        else:
            sp = 7
        dst.append(255 & (hip >> 9))
        dst.append(255 & (hip >> 1))
        dst.append(128 & (hip << 7) | 112 & (sp << 4) | 15 & mag)
        dst.append(255 & (rd >> 8))
        dst.append(255 & rd)
        dst.append(255 & (rad >> 4))
        dst.append(240 & (rad << 4) | 15 & (ded >> 8))
        dst.append(255 & ded)
w.write(dst)
w.close