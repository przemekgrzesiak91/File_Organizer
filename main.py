import os
import re

# Add option to choose path
path = os.path.abspath(os.getcwd())
print("Current path for sorting files: ", path)
print("Do you want to change it? (Y/N)")

if input() =='Y':
    print("Paste new path for sorting: ")
    path = input().replace('\\',"/")
    print("New path: ", path)

# Store file names
files = [file for file in os.listdir(path) if os.path.isfile(path+'/'+file)]

# Current types
types = set([file_type.split('.')[1]  for file_type  in files])
print(types)

# Regular expressions for file types
# doc/pdf
doc_re = re.compile(r'\.(doc(x)?|pdf|ppt(x)?|xlsx|csv|json|txt|dat|odt)$',re.I)
# img
img_re = re.compile(r'\.(jp(e)?g|png|svg|ico|xcf)$', re.I)
# mp3
mp3_re = re.compile(r'\.(mp3|mp4|m4a|flac|wav)$', re.I)
# compressed
zip_re = re.compile(r'\.(zip|rar|tar\.(gz|bz2))$', re.I)

if not os.path.exists(path+'/Documents'):
    os.makedirs(path+'/Documents')
if not os.path.exists(path+'/Images'):
    os.makedirs(path+'/Images')
if not os.path.exists(path+'/Zip'):
    os.makedirs(path+'/Zip')
if not os.path.exists(path+'/Music'):
    os.makedirs(path+'/Music')
if not os.path.exists(path+'/Other'):
    os.makedirs(path+'/Other')

for file in files:
    if img_re.search(file):
        os.rename(path+'/'+file, path+'/Images/'+file)
    elif zip_re.search(file):
        os.rename(path+'/'+file, path+'/Zip/'+file)
    elif doc_re.search(file):
        os.rename(path+'/'+file, path+'/Documents/'+file)
    elif mp3_re.search(file):
        os.rename(path+'/'+file, path+'/Music/'+file)
    else:
        os.rename(path+'/'+file, path+'/Other/'+file)
