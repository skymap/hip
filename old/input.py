import csv
b = 255
r = open('src_hip.csv', 'r')
w = open('hip.dat', 'wb')
rows = csv.reader(r)
for row in rows:
    dst = bytearray()
    src = int(row[0])
    dst.append(b & (src >> 9))
    dst.append(b & (src >> 1))
    tmp = b & (src << 7)
    src = float(row[2])
    m = 0
    if src < 0:
        src *= -1
        m = 64
    src = round(src * 46603.375)
    dst.append(tmp | m | (b & (src >> 16)))
    dst.append(b & (src >> 8))
    dst.append(b & src)
    src = float(row[1])
    src = round(src * 46603.375)
    dst.append(b & (src >> 16))
    dst.append(b & (src >> 8))
    dst.append(b & src)
    src = float(row[3])
    m = 0
    if src < 0:
        src *= -1
        m = 128
    src = round(src / 0.025)
    dst.append(m | (b & (src >> 8)))
    dst.append(b & src)
    src = float(row[4])
    m = 0
    if src < 0:
        src *= -1
        m = 128
    src = round(src / 0.02)
    dst.append(m | (b & (src >> 12)))
    dst.append(b & (src >> 4))
    tmp = b & (src << 4)
    src = float(row[5])
    m = 0
    if src < 0:
        src *= -1
        m = 8
    src = round(src / 0.02)
    dst.append(tmp | m | (b & (src >> 16)))
    dst.append(b & (src >> 8))
    dst.append(b & src)
    src = float(row[6])
    m = 0
    if src < 0:
        src *= -1
        m = 128
    src = round(src * 1000.0)
    dst.append(m | (b & (src >> 8)))
    dst.append(b & src)
    w.write(dst)
w.close
r.close