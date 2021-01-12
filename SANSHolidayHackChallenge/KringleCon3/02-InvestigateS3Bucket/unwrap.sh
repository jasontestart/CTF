#!/usr/bin/bash -x
cd wrapper3000
ls
file package
cat package
base64 -d package > package.bin
file package.bin
mv package.bin package.zip
unzip package.zip
bunzip2 package.txt.Z.xz.xxd.tar.bz2
tar xf package.txt.Z.xz.xxd.tar
xxd -r package.txt.Z.xz.xxd > package.txt.Z.xz
unxz package.txt.Z.xz
uncompress package.txt.Z
cat package.txt
