#!/bin/sh

OUTPUT=$(cat /etc/*release)
if  echo $OUTPUT | grep -q "CentOS Linux 7" ; then
	echo "Checking and installing curl and wget"
yum install curl wget -y 1> /dev/null
yum update curl wget ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "CentOS Linux 8" ; then
	echo -e "\nDetecting Centos 8...\n"
yum install curl wget -y 1> /dev/null
yum update curl wget ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "CloudLinux 7" ; then
	echo "Checking and installing curl and wget"
yum install curl wget -y 1> /dev/null
yum update curl wget ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "AlmaLinux 8" ; then
	echo "Checking and installing curl and wget"
yum install curl wget -y 1> /dev/null
yum update curl wget ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "Rocky Linux" ; then
	echo "Checking and installing curl and wget"
yum install curl wget -y 1> /dev/null
yum update curl wget ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "Ubuntu 18.04" ; then
apt install -y -qq wget curl
elif echo $OUTPUT | grep -q "Ubuntu 20.04" ; then
apt install -y -qq wget curl
else

                echo -e "\nUnable to detect your OS...\n"
                echo -e "\nCyberPanel is supported on Ubuntu 18.04, Ubuntu 20.04, Ubuntu 22.04, CentOS 7.x, CentOS 8.x,  CloudLinux 7.x, CloudLinux 8.x and AlmaLinux 8.x...\n"
                exit 1
fi

rm -f cyberpanel.sh
rm -f install.tar.gz
curl --silent -o cyberpanel.sh "https://raw.githubusercontent.com/tbaldur/cyberpanel-LTS/stable/cyberpanel.sh" 2>/dev/null
chmod +x cyberpanel.sh
./cyberpanel.sh $@
