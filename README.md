# RealTimeObjectDetection 🎥

Created an application utilising an in-built webcam or external camera to detect humans through facial recognition and other objects, providing an output to the frame contents.


## Features:
- Security Camera with built-in activation timer for human detection.
- Facial Recognition to detect whether the human is recognised or new.
- Saves videos with a timestamp.
- Option for manual photos taken.
- Use of webcam or external webcam.

## Challenges:
- The HOG algorithm would often have difficult in correctly identifying the person if they are too close or too far from the camera.
- Some cameras work better than others, and therefore has varying effects on how well the HOG algorithm performs.
- The HOG algorithm also detects images of people on photos or paintings which can affect the detection of when a real person walks into the frame. This is shown below:

![image](https://user-images.githubusercontent.com/59411811/144748528-d416a506-8887-423b-bef0-c56804086e99.jpg)
- The practibility of this program is limited unless you are using an extendable webcam or a remote webcam.

## Upcoming changes
[] Creating a GUI for option choices.


## Languages and tools used:
Created with Python, OpenCV, and numpy.
