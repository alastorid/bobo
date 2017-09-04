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

# Prerequisite

- ibus
- ibus-table
- python
- patch
- git

# how to use?

````
# install prerequisite first
sudo yum -y install ibus ibus-table python patch git
git clone https://github.com/alastorid/bobo.git
cd bobo
make && sudo make install && make reload
````

Then find it in language settings.

# ToubleShoot

## I cannot type some words, like omf (嗎)

The default ibus input mode is simplified chinese mode which will filter out all traditional chinese words. And the filter is just buggy. Patch table.py to skip filter by default. 

````
sudo patch -p0 -d/ < patch/table.py.patch
ibus restart
````

# Known Issue

 - No icon (liu.svg).
 - the novel, red house, is just too old. People don't talk like this in real life.

# Q&A

## Why the first candidate of TOH = 棞 not 面 

because 

    面 = TOH **or TJ**
    棞 = TOH **only**

So TOH gives 棞 highest priority. If you want to type 面, use TJ instead.
