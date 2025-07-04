
def length_of_longest_substring(s):
    char_index={}
    start = 0
    max_len=0

    for i,char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char]+1

        char_index[char] =i
        max_len = max(max_len, i- start+1)
    return max_len

while True:
    s=input("enter a string : ")
    if  s.lower=='q':
        break
    result = length_of_longest_substring(s)
    print(f"longest substring : {result}")