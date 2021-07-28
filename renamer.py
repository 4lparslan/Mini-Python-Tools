import os

path = 'C:\\write\\your\\path' # add path here
files = os.listdir(path)
counter = 0 # choose index start number

extension = '.jpg' # specify file extensions
fname = 'file'     # specify file names 

for index, file in enumerate(files):
    if file.endswith(extension):
        os.rename(os.path.join(path, file), os.path.join(path, fname + ''.join([str(counter), extension])))
        counter+=1