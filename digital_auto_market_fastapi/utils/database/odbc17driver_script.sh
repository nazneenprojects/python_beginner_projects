#!/bin/bash

# Check if the Ubuntu version is supported
if ! [[ "16.04 18.04 20.04 22.04" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi

# Add the Microsoft repository key
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc

# Add the Microsoft repository for Ubuntu 22.04
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Update package list and install SQL Server ODBC driver
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Optional: Install bcp and sqlcmd tools
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools

# Update PATH for mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc

# Optional: Install unixODBC development headers
sudo apt-get install -y unixodbc-dev
