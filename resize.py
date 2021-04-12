import glob
import cv2

files = glob.glob('./your_data/*jpg')

for f in files:
    
    dirs = f.split('/')

    img = cv2.imread(f)
    img = cv2.resize(img, ( int( img.shape[1]/4 ) , int( img.shape[0]/4) ))
    cv2.imwrite('./resize_data/' + dirs[-1], img)
