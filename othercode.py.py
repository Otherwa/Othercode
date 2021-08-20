list_1={' ':'#','a':'_|','b':'|_|','c':'|_','d':'-_]','e':'[]','f':'[-_','g':'-|','h':'|-|','i':'|-','j':'_*|','k':'|_*|','l':'|_*','m':'-_*|','n':'[*]','o':'|-_*','p':'-*|','q':'|-*|','r':'|-*','s':'>','t':'v','u':'<','v':'^','w':'*>','x':'*v','y':'<*','z':'*^'}
list_2={v:k for k,v in list_1.items()}
print('Other Code: [all lower]')
print("ohelp() for help & oencode(),odecode() for encoding")
def ohelp():
    print("simple encoding pattern for vowel and consonants")
    print("char representation:")
    for ch,ch2 in zip(list_1,list_2):
        print(f'|{ch} - {ch2}|',end='\n')

   
def oencode(x):
    inp=x
    for char in inp:
        print(list_1[char],end=" ")
    

def odecode(x):
    inh=x
    k=list(inh.split(' '))
    for char2 in k:
        print(list_2[char2],end='')
    
