# discord-py-llm-sender
an ooba booga (or any llm runner and hoster thing) for discord.py
# Requirements:
- A PC running [oobabooga text generation webui](https://github.com/oobabooga/text-generation-webui) (anything simillar will work but you have to tinker with the get_assistant_response function)
- Another (or the same PC) running this Note: if you're running the py on another PC Please change the `127.0.0.1` part in line 150 to your other pc's IP Address
- discord.py==1.7.2 (anything newer or older won't work) 
- A LLM model (could be anything you want but I recommend Dolphin LLaMA3)
# Howtorun:
- Make sure you have ooba booga or anything simillar as described above, now run it 
- Go to your Web UI Panel, then session, in extensions click openai, press `Save UI defaults to settings.yaml` and press apply flags/extensions and restart
- Go to model, download a LLM Model (if you haven't already) and load it
- Run the .py, type the Discord Authentication Token and enjoy.
# Notes:
Selfbotting is against Discord Terms of Service, use the selfbot function at your own risk. Otherwise, use the bot version instead.
This obviously doesn't come with a LLM by itself, you must host it on your own.
# Todo:
- ~~Username for each message so the LLM knows who sent that message (message context mode only)~~ Added ✅
- Actual working 2k characters seperator Workingonit 🤔
- More support for llm hosters by using OpenAI module instead of sending a request Workingonit 🤔
- Working message context (Can probably be fixed by using a better model) 
- Working replying context (Can probably be fixed by using a better model)
