# str1=input("enter string : ")
# sub_str=[]
# for i in range(0,len(str1)):
#     sub_str.append(str1[i])
#     if(len(sub_str)>=2):
#         if((sub_str[-2]+sub_str[-1]=='AB' or sub_str[-2]+sub_str[-1]=='CD')):
#             sub_str.pop()
#             sub_str.pop()
# print(len(sub_str))

# def sub_string(str1,sub_str):
#     for i in sub_str: #iterating the substring to find in the string(str1)
#         found=str1.find(i)
#         # if the substring is found in the string(str1)
#         if(found!=-1):
#             str2=str1.replace(i,'') #remove the substring from the string(str1) by using replace method
#             return sub_string(str2,sub_str) #call the function recursively with the new string(str2) and the given sub string(sub_str)
#     return len(str1) #return the length of the string(str1)after removing substrings

# str1=input("enter string : ")
# sub_str=['AB','CD']
# print(sub_string(str1,sub_str))

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









