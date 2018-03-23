import os;
def rename_files(path):
    file_list = os.listdir(path); # listdir -- > lists all folders and files from given directory
    saved_path = os.getcwd();
    print("Current working directory is " + saved_path);
    os.chdir(path); # chdir --> changes current dirctory to given dirctory
    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"));
        print("Old name of file "+file_name+" New name of file "+file_name.translate(None, "0123456789")); # Translate --> removes number from date in file_name variable
    os.chdir(path);

rename_files(r"D:\Git\Python\Learn N Practice\Udemy_Progeamming Fundamentals of python\data\prank");
