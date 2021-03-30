import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name='img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token='https://www.dropbox.com/request/zT5VNb0UIg2go65DP6ZQ'
    file=img_name
    file_from=file
    file_to='users/antho/testfolder'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.file_upload(f.read(),file_to,mod=dropbox.files.WriteMode.overWrite)
        print('file upload')

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()