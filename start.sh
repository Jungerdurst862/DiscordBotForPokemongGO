#!/usr/bin/env bash
echo "start bash file"
while true; do
    spawn sshpass -p PaLeKe6280! ssh paul@192.168.1.47
    cd /home/paul/Documents/DiscordBotForPokemongGO
    coordsurl=$(cat 'url.txt')
    echo "Update Url:"$coordsurl
    sleep 5
done


