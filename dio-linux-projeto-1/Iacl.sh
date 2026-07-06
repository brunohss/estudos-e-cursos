#!/bin/bash/
echo " Criando grupo de usuarios..."

groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo " Criando diretorio..." 
echo " Criando permicoes dos grupos..."

mkdir /publico
chmod 777 /publico

mkdir /adm
chown root:GRP_ADM /adm
chmod 770 /adm

mkdir /ven
chown root:GRP_VEN /ven
chmod 770 /ven

mkdir /sec
chown root:GRP_SEC /sec
chmod 770 /sec


echo " Criando usuarios..."

useradd marcos -m -s /bin/bash -p $(openssl passwd -crypt Senha123) 	-G GRP_ADM
useradd pedro -m -s /bin/bash -p $(openssl passwd -crypt Senha123)		-G GRP_ADM
useradd joao -m -s /bin/bash -p $(openssl passwd -crypt Senha123)		-G GRP_ADM


useradd jose -m -s /bin/bash -p $(openssl passwd -crypt Senha123)		-G GRP_VEN
useradd carla -m -s /bin/bash -p $(openssl passwd -crypt Senha123)		-G GRP_VEN
useradd tiago -m -s /bin/bash -p $(openssl passwd -crypt Senha123)		-G GRP_VEN


useradd antonio -m -s /bin/bash -p $(openssl passwd -crypt Senha123)	-G GRP_SEC
useradd stefani -m -s /bin/bash -p $(openssl passwd -crypt Senha123)	-G GRP_SEC
useradd marcele -m -s /bin/bash -p $(openssl passwd -crypt Senha123)	-G GRP_SEC

echo "fim"

