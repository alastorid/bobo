# bobo
OwO

~~I cannot find a complete table online, so I made one and post it here.~~

I cannot find a good boshamy IME for my RHEL box, so I made one and post it here.
It can adjust the  word order based on the txt file you gave.
So you can grab some chat logs or some novels to make the word order more practically.
Put your .txt files in assest folder and run make, it will make a IME that optimized for it.
 
# file list

- liu.txt : table it self
- assets/red_house.txt : a famous chinese novel

# how to use?

````
 $ make && sudo make install && make reload
````

Then find it in language settings.

# ToubleShoot

## Q1: I cannot type some words, like omf (嗎)

````
sudo patch -p0 -d/ < patch/table.py.patch
ibus restart
````

# Known Issue

 - No icon (liu.svg).
 - the novel, red house, is just too old. People don't talk like this in real life.
