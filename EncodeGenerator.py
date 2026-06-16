import cv2
import face_recognition
import pickle
import os

#student images into a list
folderModePath = 'Images'
PathList = os.listdir(folderModePath)
#print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderModePath, path)))
    studentIds.append(os.path.splitext(path)[0])
    #print(os.path.splitext(path)[0])
#print(len(imgList))

def findEncodings(imagesList):
    encodeList = []
    for image in imagesList:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")
#print(encodeListKnown)

#make a binary pickle file
file = open("EncodedFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
