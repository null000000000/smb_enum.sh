#!/bin/bash

echo "Enter target IP:"
read target

echo "Enter wordlist path:"
read wordlist

while read -r share; do
     if smbclient -N "//$target/$share" &> /dev/null; then
        echo "[+] Anonymous access: $share"
     fi
done < "$wordlist"


