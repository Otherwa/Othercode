## Welcome to GitHub Pages


Syntax highlighted code block

# simple dictionary
## simple I/O route
### 26 aplha and digits supported

- Bulleted
- List

1. Numbered
2. List

**Othercode** and _v1.0_ and '
def ohelp():
    print(" #simple encoding pattern for vowel and consonants")
    print(f" #char and dig representation:\n")
    listl = [4, 9, 13, 17, 21, 25]
    print('===================================================')
    for ch, ch2, i in zip(list_1, list_2, range(32)):
        print(f' {i + 1}[{ch} - {ch2}] ', end='')
        if i in listl:
            print('\n')
    print('\n=================================================')
def oencode():
    x=str(input("Enter Text : "))
    x=x.lower()
    for lettr in x:
        if lettr not in list_1:
            return print('try again.\n text required e.g  a,b,c')
    inp = x
    print('Encoded : '+x, end=' ')
    j=''
    for char in inp:
        j+=list_1[char]+" "   
    v=open("C:\\Users\\athar\\OneDrive\\Desktop\\encode.txt",'w+')
    v.write(j)
    v.close()

def odecode():
    v=open("C:\\Users\\athar\\OneDrive\\Desktop\\encode.txt",'r+') #files directory acess needed
    inh =v.read()
    v.close()
    k = list(inh.split(' '))
    for lettr in k:
        if lettr not in list_2:
            return print('try again.\n pattern required e.g _-|,_|')
    print('Decoded :', end=' ')
    for char2 in k:
        print(list_2[char2], end='')
  
# a space bug discorverd  but works  
list_1={'':'',' ':'#','a':'_|','b':'|_|','c':'|_','d':'-_]','e':'[]','f':'[-_','g':'-|','h':'|-|','i':'|-','j':'_*|','k':'|_*|','l':'|_*','m':'-_*|','n':'[*]','o':'|-_*','p':'-*|','q':'|-*|','r':'|-*','s':'>','t':'v','u':'<','v':'^','w':'*>','x':'*v','y':'<*','z':'*^','1':'10','2':'9','3':'8','4':'7','5':'6','6':'5','7':'4','8':'3','9':'2','10':'1'}
list_2={v:k for k,v in list_1.items()}
print('Other Code: [all lower]')
print('=======================')
print("Type ohelp() for help & oencode(),odecode() for encoding\n")

