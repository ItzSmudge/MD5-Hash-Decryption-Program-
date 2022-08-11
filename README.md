# MD5-Hash-Decryption-Program
REMEMBER : THIS PROGRAM SHOULD ONLY BE USED FOR EDUCATIONAL PURPOSES. THE OWNER WILL NOT CLAIM RESPONSIBILITY FOR ANY UNAUTHOTISED ACTIVITY THAT USERS CARRY OUT WITH THIS PROGRAM

A program that decrypts md5 hashes of 4 digit to 8 digit PIN numbers (integers) by comparing the hash with encoded formats of wordlist contents. 
This is not an ideal program for cracking most passwords, but this is just to demostrate the process of password hash decryption.
I hope you will find this code to be useful :)

PROGRAM REQUIREMENTS : WORDLIST AS A TEXT FILE, WORDLIST CREATION PROGRAM.
 
NOTE : This program works for PIN numbers ranging from 4 to 8 digits only. 
 
In order to create a wordlist, I used crunch in Linux. I used Kali linux for this. This process will be the same for all Debian and Ubuntu based distros.

Crunch can be installed with the following command in ubuntu and debian based distros:

        sudo apt install crunch

For other distros such as Fedora etc, the .tgz file can be downloaded from this link: 
https://sourceforge.net/projects/crunch-wordlist/files/latest/download

The wordlist can be created with the following command:

crunch 4 8 0123456789 -o file path/nameoffile.txt

For example in my case it was:

       crunch 4 8 0123456789 -o /home/username/Documents/PIN.txt
Update : A md5 hash generator pprogram is now available.

The has output of the program will look similar to as follows: 
       b'96e79218965eb72c92a549dd5a330112'
  
The required has is the string within the 'quotation marks'

![image](https://user-images.githubusercontent.com/74146327/119104123-f2d05900-ba2c-11eb-8d18-39201d4e2ce3.png)

(I have uploaded images for ease)

Explanation:
crunch 4 8 0123456789 -o /home/username/Documents/PIN.txt
  |    | |     |            
  |    | |   range of characters
  |    | | 
  |    | maximum number of characters in a password
  |   minimum number of characters in a password
  |
command call

REMEMBER : crunch is just one way of creating a wordlist. Online utilities such as at 
https://www.wordlist-generator.net/ 
This can be used for non-linux users.

However, crunch is a more convenient way of making one.
I apologise for being unable to upload the wordlist for file size restrictions.
