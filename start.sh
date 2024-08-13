#!/usr/bin/env bash
#!/usr/bin/expect -f
echo "start bash file"
while true; do
    spawn sshpass -p PaLeKe6280! ssh paul@192.168.1.47
    cd /home/paul/Documents/DiscordBotForPokemongGO
    python3 main.py
    coordsurl=$(cat 'url.txt')
    cd ..
    ls
    sleep 5
done


