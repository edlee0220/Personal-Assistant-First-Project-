import random
import webbrowser
import os
import yagmail
import datetime
#importing all module ^^
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)
pass1 = 1234

jokes = ["Knock, knock. Whos there? Canoe! Canoe who? Canoe come out and play with me today?","Knock, knock. Whos there? Lettuce. Lettuce who? Lettuce in, its cold out here.", "Knock, knock. Whos there? A broken pencil. A broken pencil who. Oh never mind its pointless.", "Knock, knock. Whos there? I am. I am who? You do not know who you are?"]
random_jokes = random.choice(jokes)
maps = ['maps', 'open google maps', 'open maps', 'please open google maps']

google = ['google', 'open google', 'please open google']

mail = ['mail', 'open mail', 'open google mail', 'please open google mail', 'gmail', 'open gmail', 'please open gmail']

safari = ['safari', 'open safari', 'please open safari']

calc = ['calc', 'calculator', 'open calc', 'open calculator', 'please open calc', 'please open calculator']

dict = ['dict', 'dictionary', 'open dict', 'open dictionary', 'please open dict', 'please open dictionary']

cal = ['cal', 'calendar', 'open cal', 'open calendar']

con = ['contacts', 'con', 'open contacts']

dash = ['dash', 'dashboard', 'open dashboard', 'open dash']

chess = ['chess', 'play chess', 'open chess']

face = ['facetime', 'face', 'open facetime']

band = ['garageband', 'garage band', 'band', 'garage', 'open band', 'open garage', 'open garage band', 'open garageband']

movie = ['imovie', 'open imovie']

ibooks = ['ibooks', 'open ibooks']

itunes = ['itunes', 'open itunes']

kindle = ['kindle', 'open kindle']

launch = ['launchpad', 'open launchpad']

amail = ['email', 'open email']

messages = ['messages', 'open messages']

notes = ['notes', 'open notes']

photos = ['photos', 'open photos']

reminders = ['reminders', 'open reminders']

stickies = ['stickies', 'open stickies']
textwrangler = ['textwrangler', 'text wrangler', 'open textwrangler', 'open text wrangler']

textedit = ['textedit', 'text edit', 'text', 'open text edit', 'open textedit']
xcode = ['xcode', 'open xcode']
emailing = ['send email', 'send']
time = ['time', 'tell time', 'what time is it?', 'what time is it']
command = ['new command']
website = ['web', 'website', 'open website', 'open new website', 'new website', 'new tab']
file = ['check', 'file check', 'check for file', 'file exist', 'exist']
read = ['read source code', 'source code']
open = ['open', 'open application', 'open app']
are = ['good','fine','okay','ok','great','excellent','perfect']
bad = ['bad','ugh']
app = ['open application', 'open app', 'application','app']
joke = ['tell me a joke','joke']
os.system("say 'Hello, I am a computer but I would like to get to know you. What is your name?")
reply = raw_input('Name: ')
os.system("say 'Hello' "+ reply +" 'How are you?'")
replay2 = raw_input('How are you?: ')
if replay2 in are:
	os.system("say 'Good, What would you like me to do for you today?' ")
elif replay2 in bad:
	os.system("say 'I am sorry to hear that. Would you like me to do anything for you? '")
else:
	os.system("say 'I do not understand. Would you like me to do anything for you? '")
while True:	
	reply3 = raw_input('What would you like to do?: ')
	if reply3 in app:
		userInput = raw_input('Application: ')	
		if userInput in safari:
			os.system("open /Applications/Safari.app")
		elif userInput in calc:
			os.system("open /Applications/Calculator.app")
		elif userInput in dict:
			os.system("open /Applications/Dictionary.app")
		elif userInput in cal:
			os.system("open /Applications/Calendar.app")
		elif userInput in con:
			os.system("open /Applications/Contacts.app")
		elif userInput in dash:
			os.system("open /Applications/Dashboard.app")
		elif userInput in chess:
			os.system("open /Applications/Chess.app")
		elif userInput in face:
			os.system("open /Applications/FaceTime.app")
		elif userInput in band:
			os.system("open /Applications/GarageBand.app")
		elif userInput in movie:
			os.system("open /Applications/iMovie.app")
		elif userInput in ibooks:
			os.system("open /Applications/iBooks.app")
		elif userInput in itunes:
			os.system("open /Applications/iTunes.app")
		elif userInput in kindle:	
			os.system("open /Applications/Kindle.app")
		elif userInput in launch:
			os.system("open /Applications/Launchpad.app")
		elif userInput in amail:
			os.system("open /Applications/Mail.app")
		elif userInput in con:
			os.system("open /Applications/Contacts.app")
		elif userInput in messages:
			os.system("open /Applications/Messages.app")
		elif userInput in notes:
			os.system("open /Applications/Notes.app")
		elif userInput in photos:
			os.system("open /Applications/Photos.app")
		elif userInput in reminders:
			os.system("open /Applications/Reminders.app")
		elif userInput in stickies:
			os.system("open /Applications/Stickies.app")
		elif userInput in textwrangler:
			os.system("open /Applications/TextWrangler.app")
		elif userInput in textedit:
			os.system("open /Applications/TextEdit.app")
		elif userInput in xcode:
			os.system("open /Applications/Xcode.app")
	elif reply3 in emailing:
		emailh = raw_input('Your email: ')
		email = raw_input('Send to: ')
		subject = raw_input('Subject: ')
		body = raw_input('Body: ')
		yagmail.SMTP(emailh).send(email, subject, body)
		print('Email Sent.')
	elif reply3 in joke:
		os.system("say 'Ok, ' "+ random.choice(jokes) +"")
		
		
	