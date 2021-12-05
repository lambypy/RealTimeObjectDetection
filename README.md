# RealTimeObjectDetection 🎥
Security camera with human detection through the HOG algorithm, created with Python and OpenCV.

Upon stumbling on the OpenCV library, I decided to make a human detection application that functions like a security camera. It was originally designed to just project the box around the human indicating that a detection has been made and recording when the application has started. Yet, it quickly became apparent that there was a lot of boring footage created, in addition to the large cost of memory in storing the videos. 

Therefore, the application was then changed to record only when detection has been made, this includes the option to show the Histogram of gradients (HOG) algorithm in the recording. This recoding lasts until the person has left the frame, starting again when the person enters. Essentially, this program acts as a human detection security camera. 

In efforts to improve the program, I was challenged by the opportunity of adding more features. Such features might include not showing the face of the person being detected for privacy reasons which is an option that the user can choose. Through studying a Big data analytics module, I remembered the importance of privacy & ethics. While the security camera is likely to be on private property facing public property, it is a good idea to have an option allowing the user to choose to blur the faces of people in the frame. 

In light of it being a security camera, I opted for distortion. This was accomplished through Gaussian blur and pixelated blur options. Applying this option will now allow the user to still detect people while retaining privacy. 

## Features:
- Security Camera with built-in activation timer for human detection.
- Creates a box around the human detected, and correctly labels as a human.
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
[] Adding options to detect the person through facial recognition

[] Creating a GUI for option choices.






-----------------------------------------
##### Date project started: 5th July 2021
##### Date project ended:
