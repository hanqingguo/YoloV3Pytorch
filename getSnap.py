import urllib.request
from PIL import Image
import io
import numpy as np
import cv2

cameraIp = "192.168.0.105"
username = "admin"
password = ""


snapUrl = "http://"+cameraIp+"/snapshot.cgi?user=%s&pwd=%s&"%(username,password)

# res = url.request.urlopen('http://192.168.1.32/snapshot.cgi?user=admin&pwd=&')
res = urllib.request.urlopen(snapUrl)
buf = res.read()
pic = io.BytesIO(buf) #from bytes read to stream
pic = Image.open(pic)
arrPic = np.array(pic)
cv2.imshow("snap",arrPic)
cv2.waitKey(0)