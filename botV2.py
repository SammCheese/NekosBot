#https://discord.com/api/oauth2/authorize?client_id=599960468555169832&permissions=8&scope=bot

import asyncio, discord, random
from discord.ext import commands
from setup import *
from nekos import *
from r34 import *
from e621 import *
from e926 import *
from gelbooru import *
from reddit import *


# Define bot
bot = commands.Bot(command_prefix=config['Prefix'], case_insensitive=True)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}.")


@bot.command(aliases=['n'])
async def nekos(ctx, *args):
    choice = " ".join(args)
    choice = choice.split(' ')[0]

    # Check if channel is SFW.
    if not ctx.message.channel.is_nsfw():
        if choice in SFW_categories or choice.lower() == "random":
            Request = nekos_class(choice, SFW_categories)

            url = Request.get_url()
            Image = Request.show_image(url)

            return await ctx.message.channel.send(file=discord.File(fp=Image, filename=url.split('/')[-1]))

        elif choice in NSFW_categories:
            return await ctx.message.channel.send("I'm sorry, this is a NSFW category. Please enter a NSFW channel to view this category.")

        else:
            return await ctx.message.channel.send("This category does not exist.")
    

    # Channel is NSFW.
    elif ctx.message.channel.is_nsfw():
        if choice in all_categories or choice.lower() == "random":
            Request = nekos_class(choice, all_categories)

            url = Request.get_url()
            Image = Request.show_image(url)

            return await ctx.message.channel.send(file=discord.File(fp=Image, filename=url.split('/')[-1], spoiler=True))
        
        else:
            return await ctx.message.channel.send("This category does not exist.")


@bot.command(aliases=['r34'])
async def rule34(ctx, *args):
    if ctx.message.channel.is_nsfw():
        tags = []
        PID = 1
        for arg in args:
            tags.append(arg)

        if not tags:
            PID = random.randint(1,750)

        request = rule34_class(tags)
        url = request.get_urls(PID)
        if url == "Error":
            return await ctx.message.channel.send("I'm sorry, there are no images with the given tags.")
        else:
            image = request.get_image(url)

        return await ctx.message.channel.send(file=discord.File(fp=image, filename=url.split('/')[-1], spoiler=True))
    else:
        return await ctx.message.channel.send("I'm sorry, this is a NSFW function. Please enter a NSFW channel to view this.")


@bot.command(aliases=['e6'])
async def e621(ctx, *args):
    # 10100100
    if ctx.message.channel.is_nsfw():
        tags = []
        PID = 1
        for arg in args:
            tags.append(arg)
        try:
            if tags[-1].isnumeric():
                PID = tags[-1]
                tags.remove(PID)
        except IndexError:
            PID = random.randint(1, 50)

        request = e621_class(tags)
        image_url = request.get_urls(PID)
        if image_url == "Error":
            return await ctx.message.channel.send("I'm sorry, there are no images with the given tags.")
        else:
            image = request.get_image(image_url)

        return await ctx.message.channel.send(file=discord.File(fp=image, filename=image_url.split('/')[-1], spoiler=True))
    else:
        return await ctx.message.channel.send("I'm sorry, this is a NSFW function. Please enter a NSFW channel to view this.")


@bot.command(aliases=['e9'])
async def e926(ctx, *args):
    tags = []
    PID = 1
    for arg in args:
        tags.append(arg)
    try:
        if tags[-1].isnumeric():
            PID = tags[-1]
            tags.remove(PID)
    except IndexError:
        PID = random.randint(1, 50)

    request = e926_class(tags)
    image_url = request.get_urls(PID)
    if image_url == "Error":
        return await ctx.message.channel.send("I'm sorry, there are no images with the given tags.")
    else:
        image = request.get_image(image_url)

    try:
        return await ctx.message.channel.send(file=discord.File(fp=image, filename=image_url.split('/')[-1]))
    except discord.errors.HTTPException:
        return await ctx.message.channel.send("I'm poor and don't have nitro. This image is too large for me.")


@bot.command(aliases=['gb'])
async def gelbooru(ctx, *args):
    if ctx.message.channel.is_nsfw():
        tags = []
        PID = 1
        for arg in args:
            tags.append(arg)


        if not tags:
            PID = random.randint(1, 200)

            

        request = gelbooru_class(tags)
        url = request.get_urls(PID)
        if url == "Error":
            return await ctx.message.channel.send("I'm sorry, there are no images with the given tags.")
        else:
            image = request.get_image(url)

        return await ctx.message.channel.send(file=discord.File(fp=image, filename=url.split('/')[-1], spoiler=True))
    else:
        return await ctx.message.channel.send("I'm sorry, this is a NSFW function. Please enter a NSFW channel to view this.")


@bot.command(aliases=['r'])
async def get_Reddit(ctx, *args):
	subreddit="".join(args)
	subreddit=subreddit.lower()
    

	if ctx.message.channel.is_nsfw():
		Get_Reddit_Images=Reddit_API(subreddit)
		Url_Buffer=Get_Reddit_Images.get_submissions(subreddit)

		if Url_Buffer=="That's not in the list":
			return await ctx.message.channel.send(Url_Buffer)

		await ctx.message.channel.send("Fetching...")
		form,Image,name=Get_Reddit_Images.GET_image(Url_Buffer)

		return await ctx.message.channel.send(file=discord.File(fp=Image,filename=name+form))

	else:
	    return await ctx.message.channel.send("I'm sorry, this is a NSFW function. Please enter a NSFW channel to view this.")


bot.run(config['Token'])