import os
import random

def add_number_to_files():
    #I need to get the files from my folder
    file_list = os.listdir(r"C:\Users\shawn\Desktop\Secret_Message_mini_project")
    #print (file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\shawn\Desktop\Secret_Message_mini_project")
    for file_name in file_list:
        os.rename(file_name, str(random.randrange(0, 101, 2)) + file_name)
    os.chdir(saved_path)

add_number_to_files()
