import os

train_txt=open('2018_train_2.txt', 'w')
val_txt=open('018_val_2.txt', 'w')
num=0
wd=os.getcwd()+'/JPEGImages/'
file_dir='JPEGImages/'
for root,dirs,files in os.walk(file_dir):
    for file in files:
        num+=1
        filename=os.path.splitext(file)[0]
        extension=os.path.splitext(file)[1]
        file_full_name = filename+extension
        if extension == '.jpg':
            if num < 170:
                train_txt.write(wd+file_full_name+'\n')
            else:
                val_txt.write(wd+file_full_name+'\n')

train_txt.close()
val_txt.close()
