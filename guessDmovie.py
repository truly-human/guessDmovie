# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:37:53 2021

@author: Abrar Aslam
"""

import random
movies=['tenet','spy kids','the godfather','iron man','parasite','ghostbusters','get out','the exorcist','the terminator','the shining','blade runner','the lord of the rings','black panther','interstellar','call me by your name','spirited away','coco','creed','american psycho','memento','pulp fiction','star wars','titanic','the matrix','back to the future','the social network','captain america','captain marvel','the incredible hulk','thor','the avengers','guardians of the galaxy','doctor strange','endgame','infinity war']

def createQstn(movie):
    n=len(movie)
    letter=list(movie)
    tempQ=[]
    for i in range(n):
        if letter[i]==' ':
            tempQ.append(" ")
        else:
            tempQ.append("*")
    qstn="".join(str(x) for x in tempQ)
    return qstn
    
def isPresent(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    arrMov=list(movie)
    arrQn=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if arrMov[i]=='' or arrMov[i]==letter:
            temp.append(arrMov[i])
        else:
            if arrQn[i]=='*':
                temp.append('*')
            else:
                temp.append(arrMov[i])
    newQn=''.join(str(x) for x in temp)
    return newQn

def play():
    clue=0
    wrong=0
    cont=1
    while(cont):
        ranMov=random.choice(movies)
        realQstn=createQstn(ranMov)
        print("GUESS THE MOVIE: ",realQstn)
        modQstn=realQstn
        ns=True
        print('use small case letters')
        print('first letter reveal is free')
        letter=input("first reveal: ")
        while(ns):
            #letter=input("reveal the letter: ")
            if(isPresent(letter,ranMov)):
                modQstn=unlock(modQstn,ranMov,letter)
                if(modQstn==ranMov):
                    print(ranMov)
                    print('S O L V E D')
                    print("solved with ",clue," clues and ",wrong," wrong answers")
                    break
                print(modQstn)
                d=int(input('press 1 if u know the movie | press 2 to reveal a letter(clue) :'))
                if(d==1):
                    ans=input("enter your answer :")
                    if ans==ranMov:
                        print('C O R R E C T')
                        print("solved with ",clue," clues and ",wrong," wrong answers")
                        break
                    else:
                        print("wrong answer try again")
                        wrong=wrong+1
                else:
                    clue=clue+1
            else:
                print(letter,'is not present')
                clue=clue+1
            letter=input("reveal the letter: ")
        cont=int(input('press 1 to continue | 0 to exit'))
            
play()