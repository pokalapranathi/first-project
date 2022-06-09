p1={}
p2={}
def anagrams(str1,str2):
        if len(str1)!=len(str2):
                return False
        else:
                num=0
                for x in str1:
                        p1[num]=x
                        num+=1
                num=0
                for x in str2:
                        p2[num]=x
                        num+=1
                a1=sorted(p1.values())
                b1=sorted(p2.values())
                if a1==b1:
                        return True
                else:
                        return False
string1=input("Enter the string")
string2=input("Enter the string to find wheather it is anagram")
print(anagrams(string1,string2))
                
