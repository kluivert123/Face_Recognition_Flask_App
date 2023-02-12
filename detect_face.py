import cv2

face_cascade = cv2.CascadeClassifier(r"F:\New folder\Bene\FaceRecognition\Face_Recognition_Flask_App\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()

#img = cv2.imread("fineboy.jpeg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in face:
       cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("img", img)
    k = cv2.waitKey(30) & 0xff
    if  k == 27:
        break

cap.release() 

#function to check your camera position
# def return_camera_indices():
#     index = -2
#     arr = []
#     i = 10
#     while i > 0:
#         cap = cv2.VideoCapture(index)
#         if cap.read()[0]:
#             arr.append(index)
#             cap.release()
#         index += 1
#         i -= 1
#     return arr
# print(return_camera_indices())