import discord 
import requests
import os,sys
import time
from discord.ext import commands 
from discord.utils import escape_mentions
def check_discord_py_version():
    try:
        import pkg_resources
        discord_version = pkg_resources.get_distribution("discord.py").version
        if discord_version == "1.7.2":
            return True
        else:
            print("You are using a discord.py version that is not supported. Installing discord.py version 1.7.2 with pip...")
            os.system("pip uninstall discord")
            os.system("pip install -U discord.py==1.7.2")
            print("discord.py installed successfully.")
            return True
    except ImportError:
        print("discord.py is not installed. Installing discord.py version 1.7.2 with pip...")
        os.system("pip install -U discord.py==1.7.2")
        print("discord.py installed successfully.")
        return True
def token():
    try:
        with open("token.txt", "r") as file: 
            token = file.read().strip()
            return token
    except FileNotFoundError:
        token = input("Enter your Discord Authentication Token: ")
        with open("token.txt", "w") as file:
            file.write(token)
        print("Token saved in token.txt.")
        return token



if __name__ == "__main__":
        if check_discord_py_version():
            print("Please ensure that you have opened ooba booga, have openAI module enabled and loaded the LLM before running this, if you haven't please do it... NOW")
            time.sleep(3)
            check = input("Are you using this on a self bot or a bot? Type S for selfbot or B for bot. Please note that selfbotting goes against Discord's TOS.: ")
            if check.lower() == "s":
               selfbot = True
            elif check.lower() == "b":
                real = True
            else:
                print("Invalid input")
                exit()
            token = token()
            messagecontext = input("Do you want to enable previous message context? Doing this will increase the chance of your LLM hallucinating however. In order for this to work properly you must ensure your LLM has a large amount of context, if it still doesn't work please modify the message context part to however the LLM likes. Y for yes and N for no: ")
            if messagecontext.lower() == "y":
                legit = True
            elif messagecontext.lower() == "n":
                legit = False
            charactercheck = input("Type Y if you want to use your own character, note that you must have the character in ooba booga already, otherwise type N: ")
            if charactercheck.lower() == "y":
                character = input("What is your character name in ooba booga?: ")
            elif charactercheck.lower() == "n":
                character = "Assistant"
            class Real(discord.Client):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    user_id = None
                    username = None
                async def on_ready(self):
                    print(f"{self.user} has connected to Discord!")
                    userid = f"<@{self.user.id}>"
                    username = self.user.name
                    await self.change_presence(status=discord.Status.online, activity=discord.Game("@me to llm | Large Language Model"))
            
                async def on_message(self, message):
                    if message.author == self.user:
                        return
                
                    async with message.channel.typing(): 
                        mentioned_users = message.mentions  

                        if self.user.mentioned_in(message):
                            mentioned_usernames = [member.name for member in mentioned_users]
                        
                            mentioned_user_ids = [f'<@{user.id}>' for user in mentioned_users]
                            for user_id, username in zip(mentioned_user_ids, mentioned_usernames):
                                message.content = message.content.replace(user_id, f"@{username}")
                        
                            if legit == True:
                                prev_message_context = await self.get_previous_message_context(message.channel)
                                message.content = f"Context: {prev_message_context} User: {message.content} (only reply to the User message, nothing else.)" if prev_message_context else message.content

                            assistant_message = await self.get_assistant_response(message.content, username, user_id)
                            assistant_message = escape_mentions(assistant_message)
                            if assistant_message:
                                await message.reply(assistant_message)
                                print("message sent", assistant_message)
                    
                        if message.reference and message.reference.cached_message:
                            referenced_message = message.reference.cached_message
                            mentioned_users = referenced_message.mentions if referenced_message.mentions else []
                            mentioned_usernames = [member.name for member in mentioned_users]
            
                            mentioned_user_ids = [f'<@{user.id}>' for user in mentioned_users]
                            for user_id, username in zip(mentioned_user_ids, mentioned_usernames):
                                referenced_message.content = referenced_message.content.replace(user_id, f"@{username}")
            
                            if referenced_message.author == self.user:  
                                if legit == True:
                                    prev_message_context = await self.get_previous_message_context(referenced_message.channel)
                                    user_message = f"Context: {prev_message_context} Bot message: {referenced_message.content} User message (only reply to the User message, nothing else.): {message.content}"
                                else:
                                    user_message = message.content
                                assistant_message = await self.get_assistant_response(user_message, username, user_id)
                                assistant_message = escape_mentions(assistant_message)
                
                                if assistant_message:
                                    await message.reply(assistant_message)
                                    while assistant_message:
                                        await message.reply(assistant_message[:2000])
                                        assistant_message = assistant_message[2000:]
                                    print("message sent", assistant_message)

                async def get_previous_message_context(self, channel):
                    prev_messages = await channel.history(limit=11).flatten()
                    prev_messages.reverse()
                    prev_messages.pop(10)
                    prev_message_texts = []
                    for message in prev_messages:
                        if message.author != self.user:
                            mentioned_users = message.mentions
                            mentioned_usernames = [member.name for member in mentioned_users]
                            mentioned_user_ids = [f'<@{user.id}>' for user in mentioned_users]
                            for user_id, username in zip(mentioned_user_ids, mentioned_usernames):
                                message.content = message.content.replace(user_id, f"@{username}")
                            author_username = message.author.name
                            prev_message_texts.append(f"@{author_username}: {message.content}")
                    return " ".join(prev_message_texts)


                async def get_assistant_response(self, user_message, username, user_id):
                    blocked_words = [username, user_id]
                    print(blocked_words)
                    for word in blocked_words:
                        if word in user_message:
                            user_message = user_message.replace(word, "")
                    url = "http://127.0.0.1:5000/v1/chat/completions"
                    headers = {"Content-Type": "application/json"}
                    history = [{"role": "user", "content": user_message}]
                    data = {"mode": "chat", "character": character, "messages": history}

                    response = requests.post(url, headers=headers, json=data, verify=False)
                    assistant_message = response.json()['choices'][0]['message']['content']
                    assistant_messages = []
                    while len(assistant_message) > 2000:
                        assistant_messages.append(assistant_message[:2000])
                        assistant_message = assistant_message[2000:]
                    assistant_messages.append(assistant_message)
                    return assistant_message
        if selfbot == True: 
            client = Real(self_bot=True)
            client.run(token, bot=False)
        elif real == True:
            intents = discord.Intents.default()
            client = Real(intents=intents)
            client.run(token)
