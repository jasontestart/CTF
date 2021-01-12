#/usr/bin/bash -x
wget https://download.holidayhackchallenge.com/2020/santa-shop/santa-shop.exe
file santa-shop.exe
7za x santa-shop.exe
cd resources
ls
mkdir source
../node_modules/.bin/asar extract app.asar source
cd source
cat README.md
head main.js
