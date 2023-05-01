import requests
import os

payload = {
    "content": "New Build Is Done"
}

header = {
    "authorization": os.environ.get("DISCORD_KEY")
}

r = requests.post("https://discord.com/api/v9/channels/1102700859843940385/messages", data=payload, headers=header)
