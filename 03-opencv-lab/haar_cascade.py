import cv2 as cv
import sys

WIDTH = 640
HEIGHT = 480

if __name__ == '__main__':
    classifier = cv.CascadeClassifier('models/haarcascade_frontalface2.xml')

    video = cv.VideoCapture(0)
    video.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
    video.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    video.set(cv.CAP_PROP_BRIGHTNESS, 170)

    while True:
        success, img = video.read()
        if not success:
            sys.exit("Could not find video.")
        faces = classifier.detectMultiScale(img)
        for result in faces:
            x,y,w,h = result
            x1, y1 = x+w, y+w
            cv.rectangle(img, (x,y), (x1,y1), (0, 0, 255), 2)

        cv.imshow("Video", img)
        if cv.waitKey(30) & 0xFF == 27:
            break;

    video.release()
    cv.destroyAllWindows()
    sys.exit(0)
