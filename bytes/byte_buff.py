class bytesBuffer:
    buf = bytearray
    readpos = int
    def __init__(self, num, pos):
        self.buf = bytearray(num)
        self.readpos = pos

    def writeInt(self, x):
        self.buf[self.readpos] = (x >> 8)
        self.buf[self.readpos + 1] = (x >> 16)
        self.buf[self.readpos + 2] = (x >> 24)
        self.buf[self.readpos + 3] = (x >> 32)
        self.readpos+=4
    def readInt(self):
        ret = 0
        for i in range(0, 4):
            print(self.buf[i])
            ret |= (self.buf[self.readpos + i] << ((i + 1) * 8))
        return ret
