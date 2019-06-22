import discord
from discord.ext.commands import Bot
import time 
import threading

client = Bot(command_prefix=".")
wordList = ["A", "B", "C"]
global roles
roles = []

help = ""
helpFile = open("Help.txt", "r")
helpFileLines = helpFile.readlines()
helpFileLine = helpFile.readline()
for helpFileLine in helpFileLines:
	help = help + helpFileLine
helpFile.close()

gaming = ""
gamingFile = open("Gaming.txt", "r")
gamingFileLines = gamingFile.readlines()
gamingFileLine = gamingFile.readline()
for gamingFileLine in gamingFileLines:
	gaming = gaming + gamingFileLine
	roles.append(gamingFileLine)
gamingFile.close()

languages = ""
languageFile = open("ProgrammingLanguages.txt", "r")
languageFileLines = languageFile.readlines()
languageFileLine = languageFile.readline()
for languageFileLine in languageFileLines:
	languages = languages + languageFileLine
	roles.append(languageFileLine)
roles.append(" ")
languageFile.close()

def getRoleName(index):
	return games[index]
	
def getMember(index):
	j = 0
	userFile = open("Nutzer.txt", "r")
	userFileLines = userFile.readlines()
	userFileLine = userFile.readline()
	for userFileLine in userFileLines:
		if j == index:
			return j
		j = j + 1
		
def getRole(index):
	j = 0
	role = ""
	roling = []
	roleFile = open("Rollen.txt", "r")
	roleFileLines = roleFile.readlines()
	roleFileLine = roleFile.readline()
	for roleFileLine in roleFileLines:
		if j == index:
			role = ''.join(roleFileLine)
			str(role)
			roling= role.split(" ")
	return roling
	
def getIndexOfRole(role):
	print("Entering")
	count = 0
	sRole = str(role)
	print(sRole)
	for i in roles:
		sRoles = str(roles[count])
		print(sRoles)
		if sRoles == sRole:
			return count
		count = count + 1
	return 1024
	
def addRole(username, roleid):
	print("Adding role for ", username, " ", roleid)
	j = 0
	n = 0
	existing = False
	userWriteFile = open("Nutzer.txt", "w")
	roleWriteFile = open("Rollen.txt", "w")
	uWFLines = userWriteFile.readlines()
	uWFLine = userWriteFile.readline()
	rWFLines = roleWriteFile.readlines()
	rWFLine = roleWriteFile.readline()
	for uWFLine in uWFLines:
		if uWFLine == username:
			existing = True
			break
		j = j + 1
	if existing == False:
		userWriteFile.write(username)
		for uWFLine in uWFLines:
			if uWFLine == username:
				break
			j = j +1
		existing == True
	if existing == True:
		for rWFLine in rWFLines:
			if n == j:
				backup = rWFLine
				backup = backup + " " + roleid
				rWFLines[1] = backup
				roleWriteFile.writelines()
			n = n + 1
			
			
					
@client.event
async def on_ready():
	print("Bot registered as {0.user}".format(client))
	
@client.event
async def on_message(message):
	i = 0
	if message.author == client.user:
		return 0
	if message.content.startswith("/help"):
		sendHelp = message.author.mention + "Dir wird die Hilfe per DM gesendet!"
		await message.channel.send(sendHelp)
		await message.author.send(help)
	if message.content.startswith("/ping"):
		await message.channel.send("Pong")
	if message.content.startswith("/rolle"):
		splitMessage = message.content.split(" ")
		for split in splitMessage:
			wordList[i] = split
			i = i + 1
		if wordList[2] == "" or 0:
			toSend = message.author.mention + "Das dritte Argument fehlt!"
			await message.channel.send(toSend)
			return 255
		if wordList[1] == "neu":
			tryit = getIndexOfRole(wordList[2])
			if tryit == 1024:
				print("Rolle ned gfunden")
				mtS = message.author.mention + "Die Rolle konnte nicht gefunden werden!"
				await message.channel.send(mtS)
			else:
				ior = tryit
				print("Fuege hinzu")
				addRole(message.author, ior)
		elif wordList[1] == "entfernen":
			return
		elif wordList[1] == "hilfe":
				return
		elif wordList[1] == "list":
			if wordList[2] == "gaming":
				await message.author.send(gaming)
			elif wordList[2] == "programmieren":
				await message.author.send(languages)
			else:
				await message.channel.send(message.author.mention + "Das dritte Argument ist falsch!")
				return 255
	

client.run("NTcyMDQxNDk3Njk2OTI3Nzg0.XQ23jg.wi61xaSZTmYMM3KiO8P3RkOvlgc")