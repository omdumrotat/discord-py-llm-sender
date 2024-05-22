# discord-py-llm-sender
an ollama for discord.py  
# Requirements:
- A PC running [ollama](https://ollama.com/) 
- Another (or the same PC) running this Note: if you're running the py on another PC Please change the `127.0.0.1` part in line 150 to your other pc's IP Address
- discord.py==1.7.2 (anything newer or older won't work) 
- A LLM model (could be anything ollama has to offer but I recommend Dolphin LLaMA3)
# Howtorun:
- Make sure you have ollama, now run it `ollama run enterthemodelthatisavailableinollama.com`
- Run the .py, type the Discord Authentication Token and enjoy. (you only need to type it once as it'll save to a file)
# Notes:
Selfbotting is against Discord Terms of Service, use the selfbot function at your own risk. Otherwise, use the bot version instead.
This obviously doesn't come with a LLM by itself, you must host it on your own.
# Todo:
- LLaVA support (should be easy to add) Workingonit 🤔
- ~~Username for each message so the LLM knows who sent that message (message context mode only)~~ Added ✅
- Actual working 2k characters seperator Workingonit 🤔
- ~~More support for llm hosters by using OpenAI module instead of sending a request~~ Added ✅ (openai-module-ver branch)
- ~~Working message context (Can probably be fixed by using a better model)~~  should be added
- Working replying context (Can probably be fixed by using a better model)
