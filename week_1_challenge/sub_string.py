def sub_string(str1):
    i=0
    while i < len(str1)-1:  
        if (str1[i]+str1[i+1]=='AB') or (str1[i]+str1[i+1]=='CD'):
            str2 = str1.replace(str1[i]+str1[i+1], "")
            return sub_string(str2)
        i=i+1
    return len(str1)

str1=input("enter string : ")
print(sub_string(str1))









