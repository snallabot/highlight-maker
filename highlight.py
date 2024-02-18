from __future__ import print_function
import cv2 as cv
import argparse
from abc import ABC, abstractmethod
capture = cv.VideoCapture(cv.samples.findFileOrKeep("./test-videos/test-gameplay.mp4"))
fps = capture.get(cv.CAP_PROP_FPS)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)


class FrameObject(ABC):
    @abstractmethod
    def startWidth(self):
        pass

    @abstractmethod
    def endWidth(self):
        pass

    @abstractmethod
    def startHeight(self):
        pass

    @abstractmethod
    def endHeight(self):
        pass

    def start(self):
        return (int(self.startWidth() * width), int(self.startHeight() * height))

    def end(self):
        return (int(self.endWidth() * width), int(self.endHeight() * height))

    def debugColor(self):
        return (0, 255, 0)

    def debug(self, image):
        cv.rectangle(image, self.start(), self.end(), self.debugColor(), 1)



class AwayScore(FrameObject):
    def startWidth(self):
        return 805/2000
    def endWidth(self):
        return 890/2000
    def startHeight(self):
        return 56/1090
    def endHeight(self):
        return 118/1090

class HomeScore(FrameObject):
    def startWidth(self):
        return 1110/2000
    def endWidth(self):
        return 1195/2000
    def startHeight(self):
        return 56/1090
    def endHeight(self):
        return 118/1090

class QuarterClock(FrameObject):
    def startWidth(self):
        return 892/2000
    def endWidth(self):
        return 980/2000
    def startHeight(self):
        return 56/1090
    def endHeight(self):
        return 84/1090

class Quarter(FrameObject):
    def startWidth(self):
        return 980/2000
    def endWidth(self):
        return 1045/2000
    def startHeight(self):
        return 56/1090
    def endHeight(self):
        return 84/1090

class PlayClock(FrameObject):
    def startWidth(self):
        return 1045/2000
    def endWidth(self):
        return 1105/2000
    def startHeight(self):
        return 56/1090
    def endHeight(self):
        return 84/1090

class DownSituation(FrameObject):
    def startWidth(self):
        return 920/2000
    def endWidth(self):
        return 1080/2000
    def startHeight(self):
        return 84/1090
    def endHeight(self):
        return 118/1090

class HomePossession(FrameObject):
    def startWidth(self):
        return 1080/2000
    def endWidth(self):
        return 1105/2000
    def startHeight(self):
        return 84/1090
    def endHeight(self):
        return 118/1090

class AwayPossession(FrameObject):
    def startWidth(self):
        return 892/2000
    def endWidth(self):
        return 920/2000
    def startHeight(self):
        return 84/1090
    def endHeight(self):
        return 118/1090

class YardMarker(FrameObject):
    def startWidth(self):
        return 1370/2000
    def endWidth(self):
        return 1410/2000
    def startHeight(self):
        return 75/1090
    def endHeight(self):
        return 95/1090

class FieldPosition(FrameObject):
    def startWidth(self):
        return 1410/2000
    def endWidth(self):
        return 1425/2000
    def startHeight(self):
        return 75/1090
    def endHeight(self):
        return 95/1090

    
class MaddenScoreboard(FrameObject):

    def __init__(self):
        self.children = [AwayScore(), HomeScore(), QuarterClock(), Quarter(), PlayClock(), DownSituation(), HomePossession(), AwayPossession(), YardMarker(), FieldPosition()]

    def startWidth(self):
        return 570/2000
    def endWidth(self):
        return 1434/2000
    def startHeight(self):
        return 56/1090
    def endHeight(self):
        return 118/1090
    
    def debug(self, image):
        for child in self.children:
            child.debug(image)

    
    
        

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
        
        # gray = cv.cvtColor(scoreboard, cv.COLOR_BGR2GRAY)
        # ret, thresh = cv.threshold(gray, 127, 255, 0)
        # cv.bitwise_not(thresh, thresh)
        scoreboard = MaddenScoreboard()
        scoreboard.debug(frame)
        cv.imshow('frame', frame)
        cv.waitKey(1)
    currentFrame += 1
    if currentFrame == fps:
        currentFrame = 0
    
    # cv.imshow('Frame', frame)
    # cv.imshow('FG Mask', fgMask)



capture.release()
# out.release()
cv.destroyAllWindows()
