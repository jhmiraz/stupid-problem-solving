def anagram(words):
    anagrams={}
    for word in words:
        sorted_word=''.join(sorted(word.lower()))
        anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
    return list(anagrams.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result= anagram(words)
print(result)