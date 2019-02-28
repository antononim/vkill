#!/usr/bin/env bash
echo -e "\e[1m STARTING INSTALLATION... \e[0m"
apt update
pkg install python*
pip install vk vk_api getpass > null
pip3 install vk vk_api getpass > null
echo alias vkill="python3 ~/vkill/vk_killer.py" >> ~/../usr/etc/bash.bashrc
echo -e '\e[1;3;31m Done! \e[0m'
rm null
