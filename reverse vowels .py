def reverseVowels(s):
        u=[]
        v=[]
        for i in range(len(s)):
            if s[i] == "A" or "E" or "I" or "O" or "U" or "a" or "e" or "i" or "o" or "u":
                u.append(i)
                v.append(s[i])
            else:
                pass
        print(u,v)
reverseVowels("leetcode")