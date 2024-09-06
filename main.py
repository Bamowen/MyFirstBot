from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#STEP 0: Load our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#STEP 1: Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

#STEP 2: Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because intents were not enabled")
        return
    
    if is_private := user_message[0] == '?': #If first char is "?" then assign true to is_private
        user_message = user_message[1:] #Take message from char 2 onward

    try:
        if (not response):
            response: str = get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response) # If message is private send in DM, otherwise in channel
    except Exception as send_except:
        print(send_except) #TODO: Proper logging

#STEP 3: Handling startup for bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

#STEP 4: Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:  #Author is bot, don't respond to itself
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#Step 5: Main entry point
def main() -> None:
    client.run(token = TOKEN)

if __name__ == '__main__':
    main()