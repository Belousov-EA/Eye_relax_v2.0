#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


class FaceDetection:
    def __init__(self, delta):
        self.delta = delta
        self.face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.cap = cv.VideoCapture(0)
        self.prev_center = [0, 0]


    def detection(self):
        ret, frame = self.cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # определяем лица
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            if (abs(self.prev_center[0] - (x + w / 2)) > self.delta) or \
                    (abs(self.prev_center[1] - (y + h / 2)) > self.delta):
                self.prev_center[0] = (x+w/2)
                self.prev_center[1] = (y+h/2)
                return True
            self.prev_center[0] = (x + w / 2)
            self.prev_center[1] = (y + h / 2)
        return False

    def end(self):
        self.cap.release()
        cv.destroyAllWindows()

