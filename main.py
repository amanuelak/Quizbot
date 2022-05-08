from SECRET import token
import json
from nextcord.ext import commands
import requests
import asyncio



bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("The bot is ready")  

def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("http://127.0.0.1:8000/api/random")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"


    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = id
        id += 1

    return(qs,answer)


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    if message.content.startswith('$question'):
        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await bot.wait_for('message', check=check, timeout=120.0)
        except asyncio.TimeoutError:
            return await message.channel.send("You took so long. The answer is " + str(answer))

        if int(guess.content) == answer:
            await message.channel.send("You are correct!")
        else:
            await message.channel.send("Sorry, you are wrong. The answer is " + str(answer))



bot.run(token)
