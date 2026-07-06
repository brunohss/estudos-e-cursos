#!/bin/bash
echo "Atualizando o servidor"
apt-get update
apt-get upgrade -y

echo "Instalando Apache e unzip no servidor"
apt-get install apache2 unzip -y

cd /tmp
echo "Baixando e instalandoos arquivos da aplicação"
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
unzip main.zip
cd linux-site-dio.main
cp -R * /var/www/html
