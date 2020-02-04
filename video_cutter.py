
import cv2 as cv


#Loading CSV values and video
cap = cv.VideoCapture('/home/jakyx/Desktop/Python scripts/NSA_4_rekr_aceton_subtitled.avi')

#Defining output
output = 'out2.avi'
start_frame = 5000
end_frame = 5200

#Initializing output video
cap.set(cv.CAP_PROP_POS_FRAMES, 0)
fps = cap.get(cv.CAP_PROP_FPS)
maxwidth = cap.get(cv.CAP_PROP_FRAME_WIDTH)
maxheight = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter(output, int(fourcc), int(fps), (int(maxwidth), int(maxheight)))

#Cutting video
i = start_frame
cap.set(cv.CAP_PROP_POS_FRAMES, start_frame)
while(cap.isOpened()):
    print(i, end='\r', flush=True)


    ret, frame = cap.read()
    out.write(frame)

    i += 1
    if ret == False:
        break
    if i > end_frame:
        break

cap.release()
out.release()
cv.destroyAllWindows()
