from cv2 import *

camera = VideoCapture(0)
m, pic = camera.read()
if m:
    imwrite("Camerapic.jpg", pic)
    imshow("Camerapic", pic)
    waitKey(0)

    picGray = cvtColor(pic, COLOR_BGR2GRAY)
    picGray = cvtColor(picGray, COLOR_GRAY2BGR)
    imshow("Camerapic", picGray)
    waitKey(0)

    line(picGray, (10, 10), (picGray.shape[1] - 10, picGray.shape[0] - 10), (0, 0, 156), 5)
    imshow("Camerapic", picGray)
    waitKey(0)

    rectangle(picGray, (100, 100), (picGray.shape[1] - 100, picGray.shape[0] - 100), (0, 156, 0))
    imshow("Camerapic", picGray)
    waitKey(0)

    destroyWindow("Camerapic")