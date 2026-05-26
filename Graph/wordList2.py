from queue import Queue
def wordList2(beginWord,endWord,wordList):
    if endWord not in wordSet:
        return []
    q = Queue()
    wordSet = set(wordList)

    result = []
    q.put([beginWord])
    level =1
    usedonWord = set()
    while not q.empty():
        path  = q.get()
        if len(path) > level:
            level = len(path)
            for word in usedonWord:
                wordSet.discard(word)
            usedonWord.clear()
        if path[-1] == endWord:
            if not result or len(path) == len(result[0]):
                result.append(path)
            continue
        for i in range(len(path[-1])):
            for ch in range(ord("a"), ord("z")+1):
                new_word = path[-1][:i] + chr(ch) + path[-1][i+1:]
                if new_word in wordSet:
                    new_path = path + [new_word]
                    q.put(new_path)
                    usedonWord.add(new_word)
                    

    return result           
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(wordList2(beginWord,endWord,wordList))