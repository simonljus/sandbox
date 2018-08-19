# -*- coding: utf-8 -*-
import sys
from clean import fileToSet,setToFile

def iterDict(dict_obj):
    ''' dict_obj.items() support for Python 2 and 3
    '''
    if sys.version < "3":
        return dict_obj.iteritems()
    else:
        return dict_obj.items()
def dictToFile(filename,swap_gram_dict,encoding="utf-8"):      
    with open(filename,"wb") as fp:
        for word,swap_grams in iterDict(swap_gram_dict): 
            fp.write((word + "," + ",".join(sorted(swap_grams)) + "\n").encode(encoding))
def swapgramsInList(words,word_min=3):
    swapgram_dict = {}
    n_words = len(words)
    percent = int(n_words/100)
    percent_count =0
    for i,word in enumerate(words):
        if percent > 0 and i % percent ==0:
            print("{} percent done".format(percent_count))
            percent_count+=1
        swapgrams=findSwapgrams(word,words,word_min)
        if len(swapgrams) >0:
            if word in swapgram_dict:
                swapgram_dict[word] = swap_gram_dict[word] | swap_grams
            else:
                swapgram_dict[word] = swapgrams
    return swapgram_dict
                
def findSwapgrams(word,words,word_min=3):
        swapgrams = set()
        swap_index = word_min 
        max_index = len(word) - word_min
        while(swap_index <= max_index):
            word_a,word_b = word[swap_index:],word[:swap_index]
            swapgram = word_a + word_b
            if swapgram in words and word_a in words and word_b in words:
                swapgrams.add(swapgram)
            swap_index+=1
        return swapgrams

if __name__ == "__main__":
    words = fileToSet("cleaned_wordlist.txt",file_encoding="utf-8")
    swapgram_dict = swapgramsInList(words)
    dictToFile("swapgrams.txt",swapgram_dict)


