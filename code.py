
import os 

target = input("enter target ip :")
wordlist = input("Enter wordlist path:  ")
  
with open(wordlist,"r") as f:
     for share in f:
         share = share.strip()
         
         cmd ="smbclient -N //" + target + "/" + share + " > /dev/null 2>&1" 
        
         if os.system(cmd) == 0:
             print("[+] anonymous access : " , share)

