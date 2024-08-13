
import requests
import json

def split_message(message):
        smaller = message['embeds'][0]['description']
        split = smaller.split("(")
        split2  = split[1].split(")")
        url = split2[0]
        return url

def Get_Coords_with_Link(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Cookie': 'sessionid=prtxn4q930j3hwmv5b4kht1svm9mjzlo; csrftoken=zN3alGFkZaUmBC7hTEjFu8qdHlBgZ4eU8jSNkI4ytv5TIc28sIWk6mRoQIBV98KV'
    }
    l = requests.get(url,headers=headers)
    coordshtmlplace = l.text.find('id="community-coord"')
    htmlplaceslice = l.text[coordshtmlplace-40:coordshtmlplace-2]
    coordshtmlplace2 = htmlplaceslice.find("value")
    return htmlplaceslice[coordshtmlplace2+7:].split(",")

def Make_Url_For_SpooferPor(coords):
    copyurl = f"pokemongo://spprotele={coords[0]},{coords[1]}"
    return copyurl
    #pokemongo://spprotele=41.60903,-0.8680

def retrive_messages(channelid,detail):
    headers = {
        'authorization': 'NjkxOTgxMzMxNDc0ODA4ODMz.G-A2mw.tBLzqwmQ0vl5_13g3eftUu627g3NLfEeH6HiCw'
    }
    l = requests.get(f"https://discord.com/api/v8/channels/{channelid}/messages",headers=headers)
    messagejson = json.loads(l.text)
    count = 1
    message = messagejson[0]
    if detail == "generall":
        url = split_message(message)
        print(url)
        coords = Get_Coords_with_Link(url)
        copyurl = Make_Url_For_SpooferPor(coords)
        file = open("url.txt","w")
        file.write(copyurl)
        print(coords,copyurl)
    
    
        
        
retrive_messages('259536527221063683',"generall")
    