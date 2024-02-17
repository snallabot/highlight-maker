from __future__ import print_function
import cv2 as cv
import argparse
import easyocr

capture = cv.VideoCapture(cv.samples.findFileOrKeep("./cards2.mp4"))
fps = capture.get(cv.CAP_PROP_FPS)
print(fps)
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
if not capture.isOpened():
    print('Unable to open:')
    exit(0)
currentFrame = 0
seconds = []
frames = []
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    if currentFrame == 0:
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # noise = cv.medianBlur(gray, 3)
        # thresh = cv.threshold(noise, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
        reader = easyocr.Reader(['en'])
        result = reader.readtext(frame, paragraph="false")
        print(result)
    frames.append(frame)
    currentFrame += 1
    if currentFrame == fps:
        seconds.append(frames)
        frames = []
        currentFrame = 0
        print(len(seconds))
    
    # cv.imshow('Frame', frame)
    # cv.imshow('FG Mask', fgMask)



capture.release()
# out.release()
cv.destroyAllWindows()