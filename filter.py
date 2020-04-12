



def filterFor(filter):
    with open('words.txt', 'r') as wordsFile:
        #words = set(words.read().split())
        words = []
        for word in wordsFile.read().split():
            if filter in word:
                words.append(word)

    return sorted(words)


if __name__ == '__main__':
    words = filterFor('kill')
    for word in words:
        print(word) 
    print(words)