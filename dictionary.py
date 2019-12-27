import json     # importing the json module

from difflib import get_close_matches   # we import the get_close_matchesfunction from the difflib module
                                        # This functions helps in finding the closest match entered by
                                        # The user when we get an input that is not present in the
                                        # the dataset

data = json.load(open("data.json"))     # deserialising the json document to a python object.
                                        # The python object is a dictionary.

# print(type(data))     # comes out to be of type dict()

def func(w) :
    w = w.lower()           # Since all the words in data.json are in lowercase
    l = get_close_matches(w, data.keys(), cutoff = 0.7)
    if w in data:
        return data[w]
    elif len(l)>0 :
        yn = input("Did you mean %s instead? \nEnter 'Y' if Yes, 'N' if No: " % get_close_matches(w, data.keys(), cutoff = 0.7)[0] )
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys(), cutoff = 0.7)[0]]
        elif yn == "n" :
            return "The word enetered by you doesn't exist. Please Double check it."
        else :
            return "We didn't understand your entry."
    else :
        return "The word enetered by you doesn't exist. Please Double check it."

word = input("Enter a word : ")

output = func(word)

if type(output) == list :
    count = 0
    for i in range(len(output)) :
        count = count + 1
        print(count, output[i])
else:
    print(output)
