import os
from shutil import copyfile

data_path = 'modified_augmented_data/'
for file in os.listdir(data_path):
    i = 0
    for image in os.listdir(data_path + file):
        if i < 400:
            copyfile(data_path + file +'/'+image, 'train/'+image )
        else:
            copyfile(data_path + file +'/'+image, 'val/'+image )
        
        i +=1