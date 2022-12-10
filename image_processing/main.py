import cv2

filename = "./image/Lenna.png"

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')


def grayscale():
    #TODO: グレースケール化を行う
    file = cv2.imread(filename)
    cv2.imwrite("./image/Lenna_gray.png", file)
### ここまででグレースケール化 ###


def face_detect():
    #TODO: 顔検出を行う
    file = cv2.imread(filename)

    cv2.imwrite("./image/Lenna_facedetect.png", file)
### ここまでで顔検出 ###


def pixel(file, ratio=0.1):
    # TODO: ピクセル化を行う
    return


def pixel_area(file, x, y, w, h, ratio=0.1):
    #TODO: 顔の部分だけピクセル化を行う
    return


def mosaic():
    #TODO: 顔の部分をモザイク処理を行う
    file = cv2.imread(filename)

    dst = pixel_area(file, x, y, w, h)
    cv2.imwrite("./image/Lenna_mosaic.png", dst)


if __name__ == '__main__':
    grayscale()
    face_detect()
    mosaic()
