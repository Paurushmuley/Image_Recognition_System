import cv2
from os import listdir
from os.path import isfile, join
import MyLibrary as ml

sourceFolder = 'archive/ak/'
outPath = 'augmented/ak/'
onlyfiles = [f for f in listdir(sourceFolder) if isfile(join(sourceFolder, f))]
for count in range(0,len(onlyfiles)):
    print(("Processing:%s\\%s\n" % (sourceFolder, onlyfiles[count])))
    
    origImage = sourceFolder + onlyfiles[count]
    ml.augmentSingle(origImage, outPath)


sourceFolder = 'archive/Ala_Idris/'
outPath = 'augmented/Ala_Idris/'
onlyfiles = [f for f in listdir(sourceFolder) if isfile(join(sourceFolder, f))]
for count in range(0,len(onlyfiles)):
    print(("Processing:%s\\%s\n" % (sourceFolder, onlyfiles[count])))
    
    origImage = sourceFolder + onlyfiles[count]
    ml.augmentSingle(origImage, outPath)

sourceFolder = 'archive/Buzgulu/'
outPath = 'augmented/Buzgulu/'
onlyfiles = [f for f in listdir(sourceFolder) if isfile(join(sourceFolder, f))]
for count in range(0,len(onlyfiles)):
    print(("Processing:%s\\%s\n" % (sourceFolder, onlyfiles[count])))
    
    origImage = sourceFolder + onlyfiles[count]
    ml.augmentSingle(origImage, outPath)

sourceFolder = 'archive/Dimnit/'
outPath = 'augmented/Dimnit/'
onlyfiles = [f for f in listdir(sourceFolder) if isfile(join(sourceFolder, f))]
for count in range(0,len(onlyfiles)):
    print(("Processing:%s\\%s\n" % (sourceFolder, onlyfiles[count])))
    
    origImage = sourceFolder + onlyfiles[count]
    ml.augmentSingle(origImage, outPath)

sourceFolder = 'archive/Nazli/'
outPath = 'augmented/Nazli/'
onlyfiles = [f for f in listdir(sourceFolder) if isfile(join(sourceFolder, f))]
for count in range(0,len(onlyfiles)):
    print(("Processing:%s\\%s\n" % (sourceFolder, onlyfiles[count])))
    
    origImage = sourceFolder + onlyfiles[count]
    ml.augmentSingle(origImage, outPath)
