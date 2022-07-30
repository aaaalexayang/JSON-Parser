import json
from difflib import get_close_matches

with open('data.json') as myfile:
    mydict = json.load(myfile)
    
def dictionary(x):
    x = x.lower()
    if x in mydict:
        return mydict[x]
    elif x.capitalize() in mydict:
        return mydict[x.capitalize()]
    elif x.upper() in mydict:
        return mydict[x.upper()]
    elif get_close_matches(x, mydict):
        yn = input('Did you mean %s insteaad? Type Y or N' % get_close_matches(x, mydict)[0])
        if yn == 'Y': 
            return mydict[get_close_matches(x, mydict)[0]]
        elif yn == 'N':
            return 'No Such Word'
        else:
            return "Don't understand"
    else:
        return 'No Such Word'
            

word = input('Enter word: ')

answer= dictionary(word)

if type(answer)==list:
    for i in answer:
        print(i)
else:
    print(answer)