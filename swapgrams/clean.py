# -*- coding: utf-8 -*-
def fileToSet(filename,file_encoding="iso-8859-1",encoding="utf-8"):
    words =set()
    with open(filename,"rb") as fp:
        for word in fp:
            word = word.decode(file_encoding)
            words.add(word.strip().lower())
    return words
def setToFile(filename,word_set,encoding="utf-8"):
    with open(filename,"wb") as fp:
        for word in sorted(word_set):
            word = word + "\n"
            fp.write(word.encode(encoding))

if __name__ == "__main__":
    words = fileToSet("wordlist.txt")
    setToFile("cleaned_wordlist.txt",words)
    


