#Yelyzaveta Boiarchuk
# Написати програму, що по заданій колекції текстових файлів будує словник термінів.
#
# Текстові файли подаються на вхід в будь-якому форматі.
# Розмір текстових файлів не менше 150 К.
# Кількість текстових файлів не менше 10.
# Словник термінів зберегти на диск.
# Оцінити розмір колекції, загальну кількість слів в колекції та розмір словника.
# В якості структури даних використати масив.
from lexicon import *
from source import *


if __name__ == '__main__':

    #PATH TO FOLDER WITH FILES (ON DISK/PROJECT)
        #files_dir_path = "/users/lizaboiarchuk/desktop/files"
    files_dir_path = "samples"


    #DOWNLOADING SAMPLE FILES TO THE DIRECTORY
    download(files_dir_path)


    #CREATING NEW DICTIONARY
    dictionary = Lexicon(files_dir_path)


    #SAVE DICT IN THE PROJECT FOLDER
    save_to_path = "file.txt"


    #SAVE DICT TO DISK
    save_to_path2 = "/users/lizaboiarchuk/desktop/file.txt"

    dictionary.write_to_file(save_to_path)
    dictionary.write_to_file(save_to_path2)


    #PRINT DICTIONARY TO THE CONSOLE
    print(dictionary)


    #PRINT SIZE AND MEMORY USAGE ESTIMATIONS
    dictionary.analyze_to_console()










