cchecks=0 
import random
def is_word_guessed(secret_word, letters_guessed):
   checks=0
   
   for word in secret_word:
      if word in letters_guessed:
         checks+= 1 
   if checks== len(str(secret_word) ):
      return True
   else:
      return False



def get_guessed_word(secret_word, letters_guessed):
   hint_word= list(secret_word)
   for i in range(len(secret_word)):
      if secret_word[i] not in letters_guessed:
         hint_word[i]= "_" 
   guessed_word = ''.join(hint_word)
   return guessed_word  


def get_available_letters(letters_guessed):
   import string
   all_letters1= string.ascii_lowercase 
   all_letters2 = list(all_letters1)
   x = list(letters_guessed)
   for i in x:
      all_letters2.remove(i)
   # all_letters3= all_letters2
   # n=0
   # for i in range(len(all_letters2)):
      
   #    if all_letters2[i] in letters_guessed:
   #       all_letters3[i]="_"
   #       n+=1
   # for i in range(n):
   #    all_letters3.remove("_")     
   # all_letters= ''.join(all_letters3)
   # return all_letters
   return all_letters2



def hangman(secret_word):
   i = random.randint(0,len(secret_word)-1)
   print("hint letter is at position no. ",i+1)
   print("Welcome to the game Hangman!")
   print("I am thinking of ", len(secret_word)," letters word")
   n=10
   k=0
   c=3
   import string
   print("You have ",n," guesses left")
   print("available letters=",string.ascii_lowercase)
   print("You have ",c," warnings left")
   letters_guessed1 =(input("guess a letter ")).lower()
   while letters_guessed1.isalpha()==False:
      print("You have enterd a invalid input")
      c-=1
      if c>=0:
         print("You have ",c," warnings left")
         letters_guessed1= str(input("guess a letter ")).lower()
      else:
         print("You have been kicked out of the game")
         break
   letters_guessed=list(letters_guessed1)
   if secret_word[i]==letters_guessed:
      print(hangman_hint(get_guessed_word(secret_word,letters_guessed)))
   if str(letters_guessed) in secret_word:
      k=0
   else:
      if letters_guessed1 in ["a", "e", "i", "o", "u"]:
         k+=2
      else:
         k+=1
   
   while k<n and c>=0:
      if is_word_guessed(secret_word,letters_guessed)==True:
         print("Congo you guessed the word")
         break
      else:
         print(get_guessed_word(secret_word,letters_guessed))
         print("available letters=",get_available_letters(letters_guessed))
         if n-k>0:
            print("You have ",n-k," guesses left")
            print("You have ",c," warnings left")
            a=str(input("guess a letter again "))
            while a.isalpha()==False:
               print("You have enterd a invalid input")
               c-=1
               if c>=0:
                  print("You have ",c," warnings left")
                  letters_guessed1= (input("guess a letter again ")).lower()
               else:
                  print("You have been kicked out of the game")
                  break
            if secret_word[i]==a:
               b=a.lower()
               if len(a)==1:
                  letters_guessed.append(b)
               print(hangman_hint(get_guessed_word(secret_word,letters_guessed)))
            if a not in secret_word:
               if a in ["a", "e", "i", "o", "u"]:
                  k+=2
               else:
                  k+=1
            b=a.lower()
            if len(a)==1:
               letters_guessed.append(b)
            else:
               letters_guessed=list(b)
               if letters_guessed==list(secret_word):
                  print("What a guess,You have won the game")
                  break
               else:
                  k+=2
         else :
            print(secret_word)
            print("You have lost the game")
            print("Better luck next time")
   if is_word_guessed(secret_word,letters_guessed)==True and n==k:
      print("Congo you guessed the word")
      print(secret_word)

   else:
      print(secret_word)
      print("You have lost the game")
      print("Better luck next time")

         
import random
def hangman_hint(guessed_word):
   hints=[]
   for word in load_words():
      flag = False
      if len(word) == len(secret_word):
         for k in range(len(secret_word)):
            if str(guessed_word)[k].isalpha()==True:
               if word[k]==str(guessed_word)[k]:
                  flag = True
               else:
                  flag = False
                  break
         if (flag): 
            hints.append(word)
   return hints


WORDLIST_FILENAME = "words.txt"


def load_words():
   """
   Returns a list of valid words. Words are strings of lowercase letters.
    
   Depending on the size of the word list, this function may
   take a while to finish.
   """
   print("Loading word list from file...")
   # inFile: file
   inFile = open(WORDLIST_FILENAME, 'r')
   # line: string
   line = inFile.readline()
    # wordlist: list of strings
   wordlist = line.split()
   print("  ", len(wordlist), "words loaded.")
   return wordlist



def choose_word(wordlist):
   """
   wordlist (list): list of words (strings)
    
   Returns a word from wordlist at random
   """
   return random.choice(wordlist)
secret_word= choose_word(load_words())
hangman(secret_word)


         



