import os
import sys
from os import listdir
from os.path import isfile, join


class Lexicon:
    def __init__(self, files_path):
        self.lexicon = []
        self.wrd_count = []
        self.doc_ids = {}
        self.files_dir_path = files_path
        self.files_list = [f for f in listdir(self.files_dir_path) if isfile(join(self.files_dir_path, f))]
        self.init_docs_ids()
        self.create_dict()


    # creating dictionary with ids and names of files
    def init_docs_ids(self):
        ind = 1
        for file in self.files_list:
            self.doc_ids[file] = ind
            ind+=1



    #function to merge ordered block of terms with lists to a dictionary
    def add_block(self,block_list):
        new_dict = []
        main_list = self.lexicon
        i = 0
        j = 0
        k = 0
        while i < len(main_list) and j < len(block_list):
            if (main_list[i][0][0] < block_list[j][0]):
                new_dict.append(main_list[i])
                i+=1
            elif (main_list[i][0][0] > block_list[j][0]):
                new_dict.append( ((block_list[j][0], 1),[block_list[j][1]]))
                j+=1
            else:
                new_dict.append(((main_list[i][0][0],main_list[i][0][1] + 1), main_list[i][1] + list([block_list[j][1]])))
                i+=1
                j+=1
        while i < len(main_list):
            new_dict.append( main_list[i])
            i+=1
        while j < len(block_list):
            new_dict.append(((block_list[j][0], 1),[block_list[j][1]]))
            j+=1
        self.lexicon = new_dict



    def create_dict(self):
        for file_name in self.files_list:
            word_dict = []
            doc_id = self.doc_ids[file_name]
            file = open(join(self.files_dir_path, file_name), "r")
            for line in file.readlines():
                line = line.replace(',','').replace('.', '').replace(';', '').replace('!', '').replace('?', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('-', '').replace('_', '').replace('*', '').replace('"', '').replace('&', '').replace('#', '').replace("'", '').replace('$', '').replace(':', '').replace('=', '').replace('<', '').replace('/', '')
                terms = line.strip().split()
                for term in terms:
                    if not term.isdigit():
                        term = term.lower()
                        word_dict.append((term, doc_id))
            word_list = list(set(word_dict))
            self.wrd_count.append((doc_id,len(word_list)))
            word_list.sort(key = lambda x: (x[0], x[1]), reverse = False)
            self.add_block(word_list)


    #writes dictionary to file
    def write_to_file(self, file_path):
        file = open(file_path, "w")
        file.write("DICTIONARY\n\n")
        analyze = self.analyze()
        file.write("TOTAL DICTIONARY SIZE: " + str((analyze[2]) / 1000) + " KB\n")
        file.write("WORDS IN DICTIONARY: " + str(analyze[3]))
        file.write("\n\n")
        for term in self.lexicon:
            file.write(str(term[0][0]) + "[" + str(term[0][1]) + "] - ")
            for f in term[1]:
                if f!=term[1][-1]:
                    file.write(str(f) + ", ")
            file.write(str(term[1][-1]))
            file.write("\n")
        file.write("\n\n\n")


    #returns size of collection, number if words in collection, size of dictionary, number of words in dictionary
    def analyze(self):
        col_size = 0
        for file_name in self.files_list:
            size = os.path.getsize(join(self.files_dir_path, file_name))
            col_size+=size
        words_in_col = self.words_in_collection()
        dict_size = sys.getsizeof(self.lexicon)
        words_in_dict = len(self.lexicon)
        return (col_size,words_in_col,dict_size,words_in_dict)



    #prints estimation result to the console
    def analyze_to_console(self):
        print("ESTIMATING: \n")
        res = self.analyze()
        print("TOTAL SIZE OF COLLECTION: " + str(len(self.files_list)) + " files, " + str((res[0])/1000) + " KB" )
        print("WORDS IN COLLECTION: " + str(res[1]))
        print("TOTAL SIZE OF DICTIONARY: " + str((res[2])/1000) + " KB")
        print("WORDS IN DICTIONARY: " + str(res[3]))



    #counts sum of words in all files of collection
    def words_in_collection(self):
        sum = 0
        for val in self.wrd_count:
            sum+= val[1]
        return sum


    def __str__(self):
        res = "DICTIONARY\n\n"
        for term in self.lexicon:
            res+=(str(term[0][0]) + "[" + str(term[0][1]) + "] - ")
            for f in term[1]:
                if f != term[1][-1]:
                    res+=(str(f) + ", ")
            res+=(str(term[1][-1]))
            res+=("\n")
        res+=("\n\n\n")
        return res











