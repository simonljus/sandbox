import sys
import time
useFirst=True
useLast=True
useAll=True
def iterdict(dictionary):
    return dictionary.items() if sys.version >= "3" else dictionary.iteritems()
def removeAt(string,index):
    return string[:index] + string[index+1:]
def getCuts(word):
    cuts = set()
    length =len(word)
    positions = []
    if useAll: 
        for pos in range(length):
            cut=removeAt(word,pos)
            if len(cut) >0:
                cuts.add(cut)
        return cuts
    elif useFirst:
        positions =[0]
        if useLast and length >1:
            positions.append(length-1)
    elif useLast:
        positions =[length-1]
    for pos in positions:
        cut=removeAt(word,pos)
        if len(cut) >0:
            cuts.add(cut)
    return cuts


def readFile(filename,bans=[],encoding="latin-1"):
    words = {}
    try:
        with open(filename,"rb") as fp:
            lines = fp.readlines()
            for word in lines:
                w =word.decode(encoding).strip().lower()
                if w not in bans:
                    words[w] = []
    except IOError:
        print("file",filename,"not found")
    return words
        
def findCombos(allwords,combos):
    for word in allwords:
        findChains(word,word,combos,0) 
    return combos
def createKey(key,index,separator="_"):
    return  key if index == 0 else key + separator + str(index)
def findChains(key,word,combos,variant_i):
    if(len(word) > 0):
        cuts =getCuts(word)
        found =False
        key_i = createKey(key,variant_i)
        sequence = list(combos[key_i])
        for cut in cuts:
            if cut in combos:
                if found:
                    variant_i +=1
                    key_i = createKey(key,variant_i)
                    combos[key_i] = list(sequence)
                found =True
                key_i = createKey(key,variant_i)
                combos[key_i].append(cut)
                variant_i = findChains(key,cut,combos,variant_i)  
    return variant_i
def main(resultfile="results.txt",wordlist="wordlist.txt",excluded="excluded.txt"):
    bans = readFile(excluded,[],"utf-8")
    words = readFile(wordlist,bans.keys())
    findCombos(list(words.keys()),words)
    best_word =""
    best_combo= []
    for word,combos in iterdict(words):
        if len(combos) >= len(best_combo):
            best_word = word
            best_combo = combos
    print("BEST:",best_word,sorted(best_combo))
    print("see full results in",resultfile)
    with open (resultfile,"wb") as wp:
        for w in sorted(words, key=lambda k: (-len(words[k]),k)):
            chain =words[w]
            if(len(chain) > 0):
                chain.sort(key=len)
                if(len(chain[0])) ==1:
                    keycount = [w,str(len(chain))]
                    msg = ";".join(keycount) +";" + ",".join(chain) + "\n"
                    #wp.write(w.encode('utf-8') + ";".encode('utf-8') + str(len(chain)).encode('utf-8') + ";".encode('utf-8') + ','.join(chain).encode('utf-8') + "\n".encode('utf-8'))
                    wp.write(msg.encode('utf8'))
if __name__ == "__main__":
    ## concatgrams find words that are related. Two words are related if the shorter word can insert at any position and become the other word
    #example an -> can , an -> and
    start = time.time()
    main()
    seconds = time.time() - start
    print("took "  + str(seconds) + " seconds")