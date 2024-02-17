from __future__ import print_function
import cv2 as cv
import argparse

capture = cv.VideoCapture(cv.samples.findFileOrKeep("./test-videos/test-gameplay.mp4"))
fps = capture.get(cv.CAP_PROP_FPS)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
startWidth = 570/2000
endWidth = 1434/2000
startHeight = 56/1090
endHeight = 118/1090

start = (int(startWidth * width), int(startHeight * height))
end = (int(endWidth * width), int(endHeight * height))

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
        # reader = easyocr.Reader(['en'])
        # result = reader.readtext(frame, paragraph="false")
        # print(result)
        scoreboard = frame[start[1]:end[1], start[0]:end[0]]
        gray = cv.cvtColor(scoreboard, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray, 127, 255, 0)
        cv.bitwise_not(thresh, thresh)
        cv.imshow('frame', thresh)
        cv.waitKey(1)
    currentFrame += 1
    if currentFrame == fps:
        currentFrame = 0
    
    # cv.imshow('Frame', frame)
    # cv.imshow('FG Mask', fgMask)



capture.release()
# out.release()
cv.destroyAllWindows()
