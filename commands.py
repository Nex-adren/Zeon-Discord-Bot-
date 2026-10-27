from discord.ext import commands
import python_weather
import random


@commands.command()
async def ping(ctx):
    await ctx.send("Pong!")


@commands.command()
async def weather(ctx, *, city: str):
    async with python_weather.Client() as client:
        weather = await client.get(city)

        await ctx.send(
            f"Погода в городе {city}: {weather.temperature}°"
        )



@commands.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=(amount + 1) - 1)
    await ctx.send(f"Delete message: {amount}")



@commands.command()
async def cube(ctx):
    randomlist = [1, 2, 3, 4, 5, 6]
    await ctx.send("Кубик: " + str(random.choice(randomlist)))