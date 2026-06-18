import cv2
import cvzone
import os
import pickle
import face_recognition
import numpy as np

#Setting up the camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

#mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
#print(len(imgModeList))

#load the encoded file
print("Loading Encoded File")
file = open("EncodedFile.p", 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
#print(studentIds)
print("Encoded File Was Found")

while True:
    success, img = cap.read()

    #reduce size for computation
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFrame = face_recognition.face_encodings(imgS, faceCurrFrame)


    #overlay
    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44+633, 866:866+414] = imgModeList[4]


    for encoFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encoFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encoFace)
        # print("matches", matches)
        # print("faceDis", faceDis)

        #in the event we have multiple face data 
        matchIndex = np.argmin(faceDis)
        # print(matchIndex)

        if matches[matchIndex]:
            print("Known faces detected")
            print(studentIds[matchIndex])

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
        
            
            # Define the top-left and bottom-right points with your background offsets, if I want to keep everything working with openCV only
            # start_point = (55 + x1, 162 + y1) 
            # end_point = (55 + x2, 162 + y2)   
                
            # # Draw the standard OpenCV rectangle (Image, Start, End, Color(BGR), Thickness)
            # cv2.rectangle(imgBackground, start_point, end_point, (0, 255, 0), 2)

    cv2.imshow("Attendance System", imgBackground)
    cv2.waitKey(1)