import easygui as eg

from tensorflow import keras
import numpy as np
import cv2

model_name = 'vgg16.model'
rows = 150
cols = 150
channels = 3
model = keras.models.load_model(model_name)

while(True) :
    file = eg.fileopenbox()
    print('You selected %s' % (file))
    
    try :
        frame = cv2.imread(file,cv2.IMREAD_UNCHANGED)
        frame = cv2.resize(frame, (rows,cols), interpolation = cv2.INTER_AREA)
        frame_bkp = frame
    except :
        print('Unable to read the file')
        break
        
    frame = np.asarray(frame).reshape((1,rows,cols,channels))
    y_pred = model.predict_classes(frame)[0]
    
    if(y_pred == 0) :
        y_pred = 'AK'
    elif(y_pred == 1) :
        y_pred = 'Ala Idris'
    elif(y_pred == 2) :
        y_pred = 'Buzgulu'
    elif(y_pred == 3) :
        y_pred = 'Dimnit'
    else :
        y_pred = 'Nazli'
    
    print("Classified as %s\n" % (y_pred))
    cv2.rectangle(frame_bkp, (0, 0), (300, 40), (0, 0, 0), -1)
    cv2.putText(frame_bkp, str(y_pred), (10, 25), cv2.FONT_HERSHEY_SIMPLEX,0.8, (255, 255, 255), 2)
    cv2.imshow("CNN Application", frame_bkp)
    cv2.waitKey(20000)
    cv2.destroyAllWindows()