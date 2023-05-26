import cv2
# Reading Video File 
vid = cv2.VideoCapture('E:\\Digital_Image_Processing\\video-processing-workshop\\sampleVideo.mp4')
 
if(vid.isOpened() == False):
     print("Error Opening Video File Errro! ")
     exit(1)

while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:
        cv2.imshow('Sample Video', frame)
        
        # key = cv2.waitKey(2)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
    else:
        break
        
vid.release()
cv2.destroyAllWindows()