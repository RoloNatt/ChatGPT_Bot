import discord
from discord.ext import commands
import os
import openai
from dotenv import load_dotenv

# Get discord token from a file
load_dotenv('tokens/discord_token.env')
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Get openai token from a file
load_dotenv('tokens/openai_token.env')
openai.api_key = os.getenv("OPENAI_TOKEN")

intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix= "!", intents=intents)

@bot.command()
async def chat(ctx, *args):
    try:
        prompt = ''.join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",    
            messages=[{"role": "user", "content": f"{prompt} "}]
        )

        reply = ""
        
        if not 'error' in response:
            reply = response['choices'][0]['message']['content']
            await ctx.channel.send(reply)

    except Exception:
        await ctx.channel.send("Something went wrong.")

bot.run(DISCORD_TOKEN)
