#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist
  
def fragchecker(list,fragment):
  j = 0
  while j < len(list):
    if list[j].startswith(fragment):
      return True
    else:
      j+=1
  return False  
def wordchecker(list,fragment):
  n = 0
  while n < len(list):
    if list[n]==(fragment):
      return True
    else:
      n+=1
  return False  
 
def main():
    words = load_wordlist()
    print(f"{len(words)} words loaded.")
    i=0
    frag = "" 
    while i<1:
      turn = 1
      if turn == 1:
        letter = input("Player one, pick a letter: ")
        if letter.isdigit()==True:
          print("Please pick a letter, not a number! ")
        elif len(letter) > 1:
          print("Please put down only one letter! ")
        else: 
          frag += letter.upper()
          print("Player one chose",frag, "giving the fragment:",frag)
          if fragchecker(words,frag)==False:
            i+=1
          elif len(frag)>2:
            if wordchecker(words,frag)==True:
              i+=4
            else:
              turn+=1
          else:
            turn+=1
      if turn == 2:
          letter = input("Player two, pick a letter: ")
          if letter.isdigit()==True:
            print("Please pick a letter, not a number! ")
          elif len(letter) > 1:
            print("Please put down only one letter! ")
          else: 
            frag += letter.upper()
            print("Player two chose",frag, "giving the fragment:",frag)
            if fragchecker(words,frag)==False:
              i+=2
            elif len(frag)>2:
              if wordchecker(words,frag)==True:
                i+=3
              else:
                turn-=1
            else:
              turn-=1
    if i==1:
      print("That will not make a word, player 2 wins!")
    if i==2:
      print("That will not make a word, player 1 wins!")
    if i==3:
      print("Player 2 wins with the word:", frag)
    if i==4:
      print("Player 1 wins with the word:", frag)
main()