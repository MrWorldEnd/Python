import socket

class device:
    #add p2p list
    def __init__(self):
        self.h_name = socket.gethostname()
        self.IP_addres = socket.gethostbyname(socket.gethostname())
    def myfunc(self):
        return [self.h_name,self.IP_addres]
    def getmydeviceinfo(self):
        out = '' + self.h_name + ',' + self.IP_addres
        return out

    def printtxt(self):
        f = open("testfile.txt", "x")
        f.write(self.getmydeviceinfo())
        f.close()

#open and read the file after the appending:
device().printtxt()
f = open("testfile.txt", "r")
print(f.read())