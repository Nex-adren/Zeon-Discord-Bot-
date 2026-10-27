from discord.ext import commands
import time

last_message = {}

async def anti_spam(message):
    user_id = message.author.id
    current_time = time.time()

    if user_id in last_message:
        if current_time - last_message[user_id] < 3:
            await message.delete()
            await message.channel.send("Анти-спам: " + message.author.mention)
            return

    last_message[user_id] = current_time

    
    print(message.author)
    print(message.content)