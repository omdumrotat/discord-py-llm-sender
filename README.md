# discord-py-llm-sender
an any llm runner and hoster thing for discord.py 
# Requirements:
- A PC running A LLM runner and hoster (by default it uses the default LM Studio port and api_key so please change that if youre not using LM Studio)
- Another (or the same PC) running this Note: if you're running the py on another PC Please change the `127.0.0.1` part in line 150 to your other pc's IP Address
- discord.py==1.7.2 (anything newer or older won't work) 
- A LLM model (could be anything you want but I recommend Dolphin LLaMA3)
# Notes:
Selfbotting is against Discord Terms of Service, use the selfbot function at your own risk. Otherwise, use the bot version instead.
This obviously doesn't come with a LLM by itself, you must host it on your own.
# Todo:
- ~~Username for each message so the LLM knows who sent that message (message context mode only)~~ Added ✅
- Actual working 2k characters seperator Workingonit 🤔
- ~~More support for llm hosters by using OpenAI module instead of sending a request~~ Added ✅
- Working message context (Can probably be fixed by using a better model) 
- Working replying context (Can probably be fixed by using a better model)
