import os
import shutil

source = "C:/Users/bilal/Downloads"
destination = "C:/Users/bilal/Desktop/Coding Files/Classes/102/Example"

file_list = os.listdir(source)
# print(file_list)

for i in file_list:
    name, ext = os.path.splitext(i)
    # print(name, ext)
    if ext == "":
        continue
    if ext in [".png", ".jpg", ".jpeg", ".gif", ".jfif"]:
        path1 = source + '/' + i
        path2 = destination + '/' + "f1/"
        path3 = destination + '/' + "f1/" + i
        # print(path1, path3)

        if os.path.exists(path2):
            print("moving", i)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving", i)
            shutil.move(path1, path3)