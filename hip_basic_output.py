print('creating file...')
r = open('hip_basic.dat', 'r+b')
v = r.read()
r.close
n = int(len(v) / 8)
w = open('hip_basic.csv', 'w')
for i in range(n):
    j = i * 8
    hip = 130560 & (v[j] << 9) | 510 & (v[j + 1] << 1) | 1 & (v[j + 2] >> 7)
    sp = 7 & (v[j + 2] >> 4)
    mag = 15 & v[j + 2]
    rd = 65280 & (v[j + 3] << 8) | 255 & v[j + 4]
    rai = int(rd / 180)
    dei = rd - rai * 180
    rad = 4080 & (v[j + 5] << 4) | 15 & (v[j + 6] >> 4)
    ded = 3840 & (v[j + 6] << 8) | 255 & v[j + 7]
    ra = rai + rad / 4095
    ded = ded / 4095
    de = (dei - ded - 89) if dei < 90 else (dei + ded - 90)
    dst = str(hip) + ',' + '{:.3f}'.format(round(ra, 3)) + ',' + '{:.3f}'.format(round(de, 3)) + ',' + str(mag) + ',' + str(sp)
    if i < (n - 1):dst += '\n'
    w.write(dst)
w.close