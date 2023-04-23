#bin/bash
cd
rm -rf ngrok-stable-linux-arm.zip
sleep 5
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
chmod 777 ngrok
rm -rf ngrok-stable-linux-arm.zip
clear
figlet "NGROK" | lolcat
echo "			by.Galirus" | lolcat

cd
echo "ngrok : Successfull" | lolcat
echo "masukkan token ngrok Silahkan Daftar akum ngrok di www.ngrok.com" | lolcat
echo "Buka new session" | lolcat
echo "cd lalu ls dan liat apakah ada file ngrok ?" | lolcat
echo "Jika ada LANJUT" | lolcat
echo "Jalankan ngrok/masukkan token"  | lolcat
read "y/n :" isi
