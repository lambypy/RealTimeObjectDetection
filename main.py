import numpy as np
import cv2
import datetime
import time


# Initialize the HOG descriptor - for boxes to appear on human
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Detecting faces and bodies for automatic recording
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

cap = cv2.VideoCapture(0)

detection = False
detection_stop_time = None
timer_start = False
RECORD_AFTER_DETECTION = 5

print("Press 'q' to quit.")

"""
For future reference:

def camera_check(source):
    
    # checking the video capture source
    cap = cv2.VideoCapture(source)

    # if no camera available then quit the program or continue
    if cap is None or not cap.isOpened():
        print("Unable to load camera: ", source)
        exit()
    else:
        print("Camera ", source, " is working.")
"""

while True:

    # check to see if capture source available
    # camera_check(source)

    ret, frame = cap.read()

    # frame resized for faster detection
    frame = cv2.resize(frame, (640, 480))

    # greyscale for also faster detection
    grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    bodies = face_cascade.detectMultiScale(grey, 1.3, 5)

    # detect people in image, returns bounding boxes for object
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in color picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                            (0,255,0), 2)
        cv2.putText(frame, "Human", (xA, yA-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (36,255,12), 2)

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_start = False
        else:
            detection = True
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y - %H:%M:%S')
           
            # output written to Human detection .avi with time stamp.
            video_filename = f"Human Detection - {st}.avi"
            output = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*"MJPG"),
                                                    15, (640,480))
            print("Started Recording!")

    elif detection:
        if timer_start:
            if time.time() - detection_stop_time >= RECORD_AFTER_DETECTION:
                detection = False
                timer_start = False
                output.release()
                print('Stop Recording!')
        else:
            timer_start = True
            detection_stop_time = time.time()

    if detection:
        output.write(frame.astype("uint8"))

    cv2.imshow("Camera", frame)


    # To take an image
    if cv2.waitKey(1) & 0xFF == ord("i"):
        print("Taking image...")
        cv2.imwrite("image.jpg", frame)

    # To stop the application.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Closing application...")
        break

# release capture and closing the windows
output.release()
cv2.destroyAllWindows()

# necessary on mac
cv2.waitKey(1)
