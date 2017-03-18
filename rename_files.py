import os


def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\shawn\Desktop\Secret_Message_mini_project")
    #print (file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\shawn\Desktop\Secret_Message_mini_project")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)    

rename_files() 
