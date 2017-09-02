# bobo
OwO

~~I cannot find a complete table online, so I made one and post it here.~~
I cannot find a good boshamy IME for my RHEL box, so I made one and post it here.
It can adjust word order based on the txt file you give.
So you can grab some chat logs, some novels etc to make the word order more practically.
Put your .txt files in assest folder and run make, it will make a IME that optimized for it.
 
# file list

- liu.txt : table it self
- chinese.txt : chinese words ordered by word frequency based on online chat.
- assets/red_house.txt : a famous chinese novel

# how to use?

````
 $ make && sudo make install && make reload
````

# ToubleShoot

## Q1: I cannot type some words, like omf (嗎)

A1:

Click the language icon and switch to tradictional chinese mode.

# Known Issue

 - No icon (liu.svg).
 - the novel, red house, is just too old. People don't talk like this in real life.
