from imutils import paths
import face_recognition
import pickle
import cv2

def recogn(path,name_of_man):
    imagePaths = list(paths.list_images(path))
    knownEncodings = []
    knownNames = []
    for (i,imagePath) in enumerate(imagePaths):
        name = name_of_man 

        image = cv2.imread(imagePath)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb,model='hog')

        encodings = face_recognition.face_encodings(rgb, boxes)
    
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)

    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("face_enc", "wb")
    f.write(pickle.dumps(data))
    f.close()
