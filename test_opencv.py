import cv2 as cv
import os

imgs = []

# read all images in folder and subfolders
folder = "./No_Apply_Grayscale"
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".jpg"):
            imgs.append(cv.imread(os.path.join(root, file)))

img = imgs[5]

# cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.blendLinear(img, gray, 0.5, 0.5, 0.5)
cv.imshow("Image", gray)

k = cv.waitKey(0)  # Wait for a keystroke in the window
# capture = cv.VideoCapture("SampleVideo_LowQuality.mp4")

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)

#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break

# capture.release()
# cv.destroyAllWindows()

# # cv.imshow("Display window", imgs[0])
# # k = cv.waitKey(0)  # Wait for a keystroke in the window
