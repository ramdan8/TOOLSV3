#bin#bash
#perintah
q="-e"
e="echo"
s="sleep 1"
ss="sleep 2"
sss="sleep 3"
#color
m="\033[1;31m"
h="\033[1;32m"
k="\033[1;33m"
b="\033[1;34m"
bl="\033[1;36m"
p="\033[1;37m"
#figlet
clear
echo
echo $q $bl"Install Package Dulu Jika Baru Menggunakan Tools Ini"
echo $q $k "Jika anda pengguna Termux Ketik$m apt"
echo $q $k "jika anda pengguna$b Linux/NETHUNTER$k ketik$m sudo"
echo $q $k "jika sudah pernah menginstall package nya silahkan ketik$m n"

read -p "[GALIRUS-404]===> " apah
if [ "$apah" = "sudo" ]
then
echo $q $k "INSTALL$h MODULE/PACKAGE"
sleep 2
sudo apt update -y
sudo apt install python3 python2 python -y
sudo apt install bash php git wget -y
pip install requests mechanize bs4
pip install fake_usragent
pip install pycryptodome 
pip install rich
pip install keyboard
pip install colorama
pip install tqdm
pkg install ruby -y
gem install lolcat
pkg install curl -y
pkg install figlet
pkg install zip -y
pkg install unzip -y
cd
cd TOOLSV3 
pip install -r requirements.txt
bash go.sh
elif [ "$apah" = "apt" ]
then
apt update && apt upgrade -y
apt install python3 python2 python -y
apt install bash php git wget -y
pip install requests mechanize bs4
pip install fake_usragent
pip install pycryptodome
pip install rich keyboard
pip install colorama tqdm
pkg install ruby -y
gem install lolcat
pkg install curl -y
pkg install figlet
pkg install zip -y
pkg install unzip -y
cd
cd TOOLSV3 
pip install -r requirements.txt
bash go.sh

elif [ "$apah" = "n" ]
then
sleep 1
echo $q $k "MEMBUKA TOOLS"
sleep 2
cd
cd TOOLSV3 
bash go.sh

else
echo $q $k "YANG BENER ISINYA"
sleep 2
fi
