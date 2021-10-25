# here in the tuple you can add those all swear words you want to add 
blacklistedwords = ('whateverswearwordsyouhavehere')  

#you can place this in your events line
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith(blacklistedwords):
        await message.delete()
        await message.channel.send('your message contains blacklisted words please refrain from swearing', delete_after = 0.5)          
    await bot.process_commands(message)
#for your note this is not a complete code of a bot this is only a small piece of code that helps to monitor words that are spoken by your server members and help to control them 
#you can add this code into your bot if you want to or get an idea of how it works
#its like kinda of a template
#and this code is written by me with the help of discord.py docs , make sure to check out the discord.py docs if you dont understand anything written here


    
    
