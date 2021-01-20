import cv2 as cv
import sys

WIDTH = 640
HEIGHT = 480

if __name__ == '__main__':
    faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    video = cv.VideoCapture(0)
    video.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
    video.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    video.set(cv.CAP_PROP_BRIGHTNESS, 170)

    while True:
        success, img = video.read()
        if not success:
            sys.exit("Could not find video.")
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=9,
            minSize=(30, 30),
            flags=cv.CASCADE_SCALE_IMAGE
        )
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
