import requests
import json
import sys
import os
import random
import urllib3
import time
import string
s=requests.Session()
urllib3.disable_warnings()
def sendEmailF(s,fron,letter,subject,link,mail):
	z = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	payload={
		'action': 'score',
		'senderEmail': 'support'+str(z)+'@'+str(str(link).split("/")[2]),
		'senderName': str(fron),
		'replyTo': '',
		'subject': str(subject),
		'messageLetter': str(letter),
		'emailList': str(mail),
		'messageType': '1',
		'charset': 'UTF-8',
		'encode': '8bit',
		'action': 'send'
	}
	files=[]
	headers = {
  		'authority': str(str(link).split("/")[2]),
  		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  		'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
  		'cache-control': 'max-age=0',
  		'cookie': 'PHPSESSID=f0ri3cqgvh28e0upaagsgcurdr',
  		'origin': 'https://'+str(str(link).split("/")[2]),
  		'referer': str(link),
  		'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  		'sec-ch-ua-mobile': '?0',
  		'sec-ch-ua-platform': '"macOS"',
  		'sec-fetch-dest': 'document',
  		'sec-fetch-mode': 'navigate',
  		'sec-fetch-site': 'same-origin',
  		'sec-fetch-user': '?1',
  		'upgrade-insecure-requests': '1',
  		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
  	}
	s.post(link, headers=headers, data=payload, files=files, verify=False)

def sendEmail(s,mail,link):
	z = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	payload={
		'action': 'score',
		'senderEmail': 'support'+str(z)+'@'+str(str(link).split("/")[2]),
		'senderName': 'support'+str(z)+'@'+str(str(link).split("/")[2]),
		'replyTo': '',
		'subject': 'ARON-TN',
		'messageLetter': 'ARON-TN',
		'emailList': str(mail),
		'messageType': '1',
		'charset': 'UTF-8',
		'encode': '8bit',
		'action': 'send'
	}
	files=[]
	headers = {
  		'authority': str(str(link).split("/")[2]),
  		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  		'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
  		'cache-control': 'max-age=0',
  		'cookie': 'PHPSESSID=f0ri3cqgvh28e0upaagsgcurdr',
  		'origin': 'https://'+str(str(link).split("/")[2]),
  		'referer': str(link),
  		'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
  		'sec-ch-ua-mobile': '?0',
  		'sec-ch-ua-platform': '"macOS"',
  		'sec-fetch-dest': 'document',
  		'sec-fetch-mode': 'navigate',
  		'sec-fetch-site': 'same-origin',
  		'sec-fetch-user': '?1',
  		'upgrade-insecure-requests': '1',
  		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
  	}
	s.post(link, headers=headers, data=payload, files=files, verify=False)
def sezz(s,link):
	url = "https://api.internal.temp-mail.io/api/v3/email/new"
	x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	payload = "{\"name\":\""+str(x)+"\",\"domain\":\"best-john-boats.com\"}"
	headers = {
    	'authority': 'api.internal.temp-mail.io',
    	'accept': 'application/json, text/plain, */*',
    	'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    	'application-name': 'web',
    	'application-version': '2.2.29',
    	'content-type': 'application/json;charset=UTF-8',
    	'cookie': '_ga=GA1.2.471563460.1673987461; _gid=GA1.2.1556396931.1673987461; _gat=1',
    	'origin': 'https://temp-mail.io',
    	'referer': 'https://temp-mail.io/',
    	'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    	'sec-ch-ua-mobile': '?0',
    	'sec-ch-ua-platform': '"macOS"',
    	'sec-fetch-dest': 'empty',
    	'sec-fetch-mode': 'cors',
    	'sec-fetch-site': 'same-site',
    	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
	response = s.post(url, headers=headers, data=payload, verify=False).json()
	while(len(str(response["token"]))<1):
		x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
		payload = "{\"name\":\""+str(x)+"\",\"domain\":\"best-john-boats.com\"}"
		response = s.post(url, headers=headers, data=payload, verify=False).json()
	mail=str(response["email"])
	sendEmail(s,str(mail),str(link))
	url = "https://api.internal.temp-mail.io/api/v3/email/"+str(mail)+"/messages"
	payload={}
	headers = {
    	'authority': 'api.internal.temp-mail.io',
    	'accept': 'application/json, text/plain, */*',
    	'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    	'application-name': 'web',
    	'application-version': '2.2.29',
    	'cookie': '_ga=GA1.2.471563460.1673987461; _gid=GA1.2.1556396931.1673987461; _gat=1',
    	'origin': 'https://temp-mail.io',
    	'referer': 'https://temp-mail.io/',
    	'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    	'sec-ch-ua-mobile': '?0',
    	'sec-ch-ua-platform': '"macOS"',
    	'sec-fetch-dest': 'empty',
    	'sec-fetch-mode': 'cors',
    	'sec-fetch-site': 'same-site',
    	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
	}
	cus = 0
	tyr = ""
	getnotif = s.get(url, headers=headers, data=payload, verify=False).text
	while("ARON-TN" not in str(getnotif)):
		getnotif = s.get(url, headers=headers, data=payload, verify=False).text
		print("Waiting .....")
		time.sleep(4)
		cus+=1
		if(cus==10):
			tyr = "Timeout"
			break
	if(tyr == "Timeout") : return False
	else : return True
print("Mailer Sender By ARON-TN")
letterContent = str(input("Letter > "))
sendername = str(input("Sender Name > "))
subject = str(input("Subject > "))
mail_list = str(input("Mail list > "))
sites_list = str(input("Mailers list > "))
how_many_per_mailer = int(input("switch mailer after sending > "))
#######################################
c = []
emails=open(mail_list,'r', encoding='UTF-8', errors='ignore').read().splitlines()
for i in emails:
	c.append(str(i))
#######################################
sitel = []
sites=open(sites_list,'r', encoding='UTF-8', errors='ignore').read().splitlines()
for i in sites:
	sitel.append(str(i))
#######################################
tota = str(len(c))
ii = -1
sn = 0
cbon = True
while cbon:
	if(len(c)==0) : cbon = False;break
	if(len(sitel)==0) : cbon = False;break
	if(ii==len(sitel)) : ii = -1
	else : ii+= 1
	print(f"Testing Site {str(sitel[ii])}")
	if(sezz(s,str(sitel[ii]))) :
		print(f"{str(str(sitel[ii]))} > Delivery working !")
		with open(letterContent, "r") as f: contents = f.read()
		if(len(c)>int(how_many_per_mailer)):
			for _ in range(int(how_many_per_mailer)):
				sn+=1
				print(f"{str(sn)}/{str(tota)} sending to > {str(c[0])} From {str(sitel[ii])}")
				sendEmailF(s,str(sendername),str(contents),str(subject),str(sitel[ii]),str(c[0]))
				c.remove(str(c[0]))
		else:
			for _ in range(len(c)):
				sn+=1
				print(f"{str(sn)}/{str(tota)} sending to > {str(c[0])} From {str(sitel[ii])}")
				sendEmailF(s,str(sendername),str(contents),str(subject),str(sitel[ii]),str(c[0]))
				c.remove(str(c[0]))
	else :
		print(f"{str(str(sitel[ii]))} > Delivery not working !!!")
		sitel.remove(sitel[ii])
if(len(c)==0):
	print("I sent all emails !!!")
elif(len(sitel)==0):
	print("Please Add more mailers !")
else:
	print("Something wrong ..")






