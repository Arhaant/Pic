import cv2
import dropbox
import time
import random
start = time.time()
def takePic():
    img = cv2.VideoCapture(0)
    active = True
    num = random.randint(0,100)
    while active:
        ret, frame = img.read()
        name = 'img'+str(num)+'.png'
        cv2.imwrite(name,frame)
        start = time.time()
        active = False
    img.release()
    cv2.destroyAllWindows()
    print('picture taken')
    return name

def upload(name):
    dbx = dropbox.Dropbox('sl.BGL6f0RUgVe5s9A4fs_xHHkxIdg9-2rB4jsngegfrniuC6tWmQJF-drQxp-AOCUEPxnYgSHENzQ2ionlvz0KLnOslNHWOvjhRz-9aYBOQAPhIxSssbIUjKtZnuZMXJupkPbsBz0')
    with open(name,'rb') as f:
        dbx.files_upload(f.read(),'/'+name)
        print('Image uploaded')

while True:
    if ((time.time()-start)>5):
        name = takePic()
        upload(name)