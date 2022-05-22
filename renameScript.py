import os

def renameFiles(old_path, head_tail):
    global REPLACE_FROM, REPLACE_TO
    new_path = os.path.join(head_tail[0],head_tail[1].replace(REPLACE_FROM, REPLACE_TO))
    os.rename(old_path,new_path)


def renameFolder(old_path, head_tail):
    global REPLACE_FROM, REPLACE_TO
    #construct new folder name
    new_path = os.path.join(head_tail[0],head_tail[1].replace(REPLACE_FROM, REPLACE_TO))
    os.rename(old_path, new_path)
    return new_path

def traverseDir(root_path):
    for item in os.listdir(root_path):
        #generate item path
        item_path = os.path.join(root_path, item);
        #seperating the head and tail of the path into a list, index 0 - head, index 1 - tail
        path_head_tail = os.path.split(item_path);
        #checking the provided path is a file or directory
        if os.path.isdir(item_path):
        #replace double backslash with single backslash
            item_path.replace("////","//")
            item_path = renameFolder(item_path, path_head_tail)
            #print(item_path)
            traverseDir(item_path)
        
        if os.path.isfile(item_path):
            renameFiles(item_path, path_head_tail)

REPLACE_FROM = "_"
REPLACE_TO = " "

root_path = "C:\\Users\\jetle\\Documents\\01_April_2022_BoS-20220506T051826Z-001\\01_April_2022_BoS"
traverseDir(root_path)