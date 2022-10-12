
from va_core import VA_Core
import functools
  
dict=VA_Core.getAllLocationOfAText('File')

def compare(cord1,cord2):
    print(cord1,cord2)
    if (cord1[0]<=cord2[0] and cord1[1]<=cord2[1]):
        return -1
    elif (cord1[0]<=cord2[0] and cord1[1]>=cord2[1]):
        return 1
    elif (cord1[0]>=cord2[0] and cord1[1]>=cord2[1]):return 1
    elif(cord1[0]>=cord2[0] and cord1[1]<=cord2[1]):return -1
    else:return 0
   
# print(dict
def getSorted(dict):

    for key,value in dict.items():
        print(value)
        dict[key]=sorted(value,key=functools.cmp_to_key(compare),reverse=True)
    return dict

print(dict)