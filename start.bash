#!/usr/bin/env bash

echo "Moin Paul Neuer Versuch Fuer Shinys"

sshpass -p PaLeKe6280! ssh paul@192.168.1.47 'python3 /home/paul/Documents/DiscordBotForPokemongGO/main.py'

coordsurl=$(sshpass -p PaLeKe6280! ssh paul@192.168.1.47 'cat /home/paul/Documents/DiscordBotForPokemongGO/url.txt')


echo "opening Safari $coordsurl"

xdg-open Chrome "$coordsurl"

echo "send you the file"


