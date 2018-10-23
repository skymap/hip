r = open('hip.dat', 'rb')
w = open('dst_hip.csv', 'w')
while True:
    row = r.read(17)
    if len(row) == 0:
        break
    dst = []
    v = (row[0] << 9) | (row[1] << 1) | (row[2] >> 7)
    dst.append(v)
    v = ((row[5] << 16) | (row[6] << 8) | row[7]) / 46603.375
    dst.append(round(v, 4))
    s = 1 & (row[2] >> 6)
    v = (((row[2] & 63) << 16) | (row[3] << 8) | row[4]) / 46603.375
    if s == 1:
        v *= -1
    dst.append(round(v, 4))
    s = row[8] >> 7
    v = (((row[8] & 127) << 8) | row[9]) * 0.025
    if s == 1:
        v *= -1
    dst.append(round(v, 2))
    s = row[10] >> 7
    v = (((row[10] & 127) << 12) | (row[11] << 4) | (row[12] >> 4)) * 0.02
    if s == 1:
        v *= -1
    dst.append(round(v, 2))
    s = 1 & (row[12] >> 3)
    v = (((row[12] & 7) << 16) | (row[13] << 8) | row[14]) * 0.02
    if s == 1:
        v *= -1
    dst.append(round(v, 2))
    s = 1 & (row[15] >> 7)
    v = (((row[15] & 127) << 8) | row[16]) / 1000.0
    if s == 1:
        v *= -1
    dst.append(round(v, 3))
    w.write(str(dst[0]) + ',' + str(dst[1]) + ',' + str(dst[2]) + ',' + str(dst[3]) + ',' + str(dst[4]) + ',' + str(dst[5]) + ',' + str(dst[6]) + '\n')
w.close
r.close
