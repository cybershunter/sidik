#!/bin/sh

b="\033[1m"
u="\033[4m"
bl="\033[30m"
r="\033[31m"
g="\033[32m"
bu="\033[34m"
m="\033[35m"
c="\033[36m"
w="\033[37m"
endc="\033[0m"
enda="\033[0m"
blue="\033[1;34m"
cyan="\033[1;36m"
red="\033[1;31m"


figlet LUTFI | lolcat



           echo "\033[1;31mTools Biasa Bukan Luar Biasa"

    echo "•••••••••••••••••••••••••••••••••••••••••••••••••••••"
    echo "•tools :Jaringan      : Lutfi aulia sidik           •" | lolcat
    echo "•team  :LUTFI_sks     : 085********                 •" | lolcat
    echo "•NO WA :085323354869  : lutfi sidik                 •" | lolcat
    echo "•••••••••••••••••••••••••••••••••••••••••••••••••••••"


echo "\033[1;32mMau milih yang Mana?!!"

echo "•••••••••••••••••••••••••••••••••••"
echo "[1].\033[1;32mStabilkan jaringan 4G"
echo "[2].\033[1;32mStabilkan jaringan 3G"
echo "[3].\033[1;32mLutfi_SKS            "
echo "[4].\033[1;32mAlamat Lutfi         "
echo "[5].\033[1;32mAmanat dari Lutfi    "
echo "[6].\033[1;32mkeluar               "
echo "•••••••••••••••••••••••••••••••••••"
read -p "masukan pilihan anda disini :" pilih;

if [ $pilih = "1"  ]
then
sleep 2
    echo "Mensatabilkan jaringan 4G..."
    cd $home
    ping 217.160.0.201
    echo "selasai bagus gak jaringan nya...."

elif [ $pilih = "2" ]
then

   echo "mensatabilkan jaringan 3G.."
   cd $home
   ping 172.217.194.91
   echo "selesai bagus gak jaringan nya.."

elif [ $pilih = "3" ]
then
sleep 2

   echo "\033[30mnomer WA:085323354869"
   sleep 2
   echo "\033[30mnama Facebook:Lutfi sidik"
   sleep 2
   echo "\033[30mnama FF:TNB lutfi"

elif [ $pilih = "4" ]
then
sleep 2
    echo "provinsi:jawabarat"
    sleep 2
    echo "kota:tasikmalaya"
    sleep 2
    echo "kab:tasikmalaya"
    sleep 2
    echo "kec:sukarame"
    sleep 2
    echo "kap:taneuh bereum"
    sleep 2
    echo "RT:08"
    sleep 2
    echo "RW:02"

elif [ $pilih = "5" ]
then
sleep 2
    echo "\033[1;34mGunakan lah tools ini dengan bijak"
    sleep 2
    echo "\033[1;34mJangan di rubah tools ini"
    sleep 2
    echo "\033[1;34mKarena saya capek buat nya!!"
    sleep 2
    echo "\033[1;34mPaham ngak!!!!!!!!!!"
    sleep 2
    echo "\033[1;34mTank you atas perhatian anda"

elif [ $pilih = "6" ]
then
sleep 2
    echo "\033[1;34mterimakasih sudah mengunakan tools ini"
    sleep 2
    echo "\033[1;34msemoga bermamfaat"
    cd $home
    sleep 2
    echo "\033[1;34mdadah^_^........"
    sleep 2
    exit

else
   echo "\033[1;31mNomer yang anda masukan tidak ada dalam daftar"
   sleep 2
   echo "\033[1;31mCobalagi masukan nomer yang tersedia"
fi
    