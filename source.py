import urllib.request
from os.path import join

file_urls = ['http://www.gutenberg.org/files/1524/1524-0.txt',
         'http://www.gutenberg.org/cache/epub/1112/pg1112.txt',
         'http://www.gutenberg.org/files/23042/23042-0.txt',
         'http://www.gutenberg.org/files/1531/1531-0.txt',
         'http://www.gutenberg.org/files/1532/1532-0.txt',
         'http://www.gutenberg.org/files/1522/1522-0.txt',
         'http://www.gutenberg.org/cache/epub/1103/pg1103.txt',
         'http://www.gutenberg.org/files/43440/43440-0.txt',
         'http://www.gutenberg.org/files/23046/23046-0.txt',
         'http://www.gutenberg.org/cache/epub/1121/pg1121.txt'
]


def download(dir_path):
    ind = 1
    for url in file_urls:
        file_name = 'text' + str(ind) + '.txt'
        file_path = join(dir_path,file_name)
        urllib.request.urlretrieve(url, file_path)
        ind+=1
