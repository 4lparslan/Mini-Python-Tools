# The code converts annotation format from XML to TXT. Created format is for YOLO

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import os
import cv2

# The path you store XML files
xmlpath = r'/my/path/'
# The path you will store TXT files
pathtosave = r'/my/other/path/'

print(len(os.listdir(xmlpath)))

for filename in os.listdir(xmlpath):
    name= filename.split('.xml')
    # if not filename.endswith('.xml'):
    #     print("damn")
    file = open(pathtosave+name[0]+'.txt','w')
    fullname = os.path.join(xmlpath, filename)

    contents = open(fullname).read()
    soup = BeautifulSoup(contents, "xml")
    coords = set()

    # extract the image dimensions
    w = int(soup.find("width").string)
    h = int(soup.find("height").string)
    # loop over all `object` elements

    for o in soup.find_all("object"):
        # extract the label and bounding box coordinates
        label = o.find("name").string
        xMin = int(o.find("xmin").string)
        yMin = int(o.find("ymin").string)
        xMax = int(o.find("xmax").string)
        yMax = int(o.find("ymax").string)

        # truncate any bounding box coordinates that may fall
        # outside the boundaries of the image
        xMin = max(0, xMin)
        yMin = max(0, yMin)
        xMax = min(w, xMax)
        yMax = min(h, yMax)
        pw= xMax-xMin
        ph=yMax - yMin
#..............................................
        cx = xMin + pw/2
        cy = yMin + ph/2
        NorX = cx / w
        NorY = cy / h


        NorW = pw / w
        NorH = ph / h


        NorX= 1 if NorX> 1 else NorX
        NorY= 1 if NorY> 1 else NorY
        NorW = 1 if NorW> 1 else NorW
        NorH= 1 if NorH> 1 else NorH



        NorX= 0.000001 if NorX< 0 else NorX
        NorY= 0.000001 if NorY< 0 else NorY
        NorW= 0.000001 if NorW< 0 else NorW
        NorH= 0.000001 if NorH< 0 else NorH



        NorX= float("{:.4f}".format(NorX))
        NorY= float("{:.4f}".format(NorY))
        NorW= float("{:.4f}".format(NorW))
        NorH= float("{:.4f}".format(NorH))
        # build a (hashable) tuple from the coordinates


        coord = (NorX, NorY, NorW, NorH)

        # if the coordinates already exist in our `coords` set,
        # ignore the annotation (this is a peculiarity of the
        # logos dataset)
        if coord in coords:
            continue

        # write the image path, bounding box coordinates, and
        # label to the output CSV file

        #row = [label, str(xMin), str(yMin),str(xMax), str(yMax)]
        coords.add(coord)
        #CLASSES.add(label)
        if label =='ball':
            file.write('0')
        else:
            print(label)
            print("ERRROOOOOOORRRR__________")
            print(filename)
            continue
            #cv2.waitKey(0)
            #file.write('0')
        file.write(' ')
        file.write(str(NorX))
        file.write(' ')
        file.write(str(NorY))
        file.write(' ')
        file.write(str(NorW))
        file.write(' ')
        file.write(str(NorH))
        file.write('\n')
    file.close()
print("Done")