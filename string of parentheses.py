<<<<<<< HEAD
def anagram(words):
    anagrams={}
    for word in words:
        sorted_word=''.join(sorted(word.lower()))
        anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
    return list(anagrams.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result= anagram(words)
print(result)
=======


def isValid(str_char):
    stack=[]
    bracket={')':'(', ']':'[', '}':'{'}  #{'key':'value'}

    for char in str_char:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket:
            if not stack or stack.pop() != bracket[char]:
                return False
    return len(stack)==0





char=str(input("enter bracket: "))
print(isValid(char))
>>>>>>> 5417efed4cebb6dd7c2a03d8811fca2d61f0377c
