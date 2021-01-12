#!/usr/bin/bash -x
ls
grep munchkin munchkin_19315479765589239
rm munchkin_19315479765589239
pwd
ls -a
history | grep munchkin
env | grep munchkin
cd workshop/
grep -i munchkin toolbox*
ls -l lollipop_engine
chmod +x lollipop_engine
./lollipop_engine
cd /home/elf/workshop/electrical;mv blown_fuse0 fuse0
ln -s fuse0 fuse1
cp fuse1 fuse2
echo "MUNCHKIN_REPELLENT" >> fuse2
cd /opt/munchkin_den
ls -R | grep -i munchkin
find /opt/munchkin_den -user munchkin
find /opt/munchkin_den -size -110k -size +108k
ps -elf | grep munchkin
netstat -lt
curl --output - http://127.0.0.1:54321
kill -9 192205
