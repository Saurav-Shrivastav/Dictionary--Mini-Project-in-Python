# Dictionary--Mini-Project-in-Python

### Dictionary - Operating through Command Line

## Description
This is a smart dictionary. Now, I call it smart because it can detect errors in entries by the user and then search for a word which the user may have wanted to enter. 

## Flow of the program 
The flow of the program is as follows:
1. Prompt the user for a word.
2. If the word exists in the dictionary,  
      1. display it's meaning.
3. If the word doesn't exist in the dictionary, it searches for the word which has a similarity ratio of at least 0.7 with the entered 
   word. If it finds a similar word :
      1. The user is asked if he meant to enter the newly found word and then displays it's meaning if the user relies with a yes.
      2. If the word is not what the user meant the program is exited after printing a message.
4. If it doesn't find any similar word :
      1. The program is exited after printing a message.
      
## Libraries Used:
-Built in Libraries :
  1. JSON
  2. DIFFLIB

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
