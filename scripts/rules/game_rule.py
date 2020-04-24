#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')


game_words = "电子竞技,电竞,DOTA,DotA,dota,InfiWar,FileFront,WCG20,War3,WAR3,ADC,Grubby,星际2,BioWare,育碧,Ubisoft,Blizzard"
game_words = game_words.split(",")

with open(sys.argv[1], 'r') as file:
    index = 0
    for line in file:
        line = line.strip()
        for game_word in game_words:
            if game_word in line:
                print("%s\t%s" % (index, "游戏"))
                break
        index += 1

