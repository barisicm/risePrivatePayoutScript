import requests
import json
import sys
import time
import copy
import logging

NODE = "https://yournodeIP:port"
NODEPAY = "http://yournodeIP:port"
PUBKEY = ""
LOGFILE = 'privatepoollogs.json'
ERRORLOG = 'errorlog.txt'
TRANSACTIONFEE = 0.1
SECRET = "secret"
SECONDSECRET = "secret"
RISEPERDAY = 420
PAYINGDELEGATEADDRESS=""

def loadLog ():
	try:
		data = json.load (open (LOGFILE, 'r'))
	except:
		data = {
			"failedToLoad": True
		}
		logging.basicConfig(filename=ERRORLOG, level=logging.DEBUG)
		logging.debug('The file with the voter addresses and amounts to payout failed to load.')
		print('The file with the voter addresses and amounts to payout failed to load.')
	return data	

def getDelegateBalance ():

	b = requests.get(NODEPAY +"/api/accounts/getBalance?address=" + PAYINGDELEGATEADDRESS).json ()
	balance = int(b["balance"])/100000000

	return balance

def doPayouts (log):
	doPayouts = False

	if getDelegateBalance () > RISEPERDAY:
		doPayouts = True

	#if log failed to load then exit the function
	if log["failedToLoad"] == True:
		print("The file with the voter addresses and amounts to payout failed to load.")
		return 0
	else:
		if doPayouts == True:
			f = open ('payments.sh', 'w')
			for voter in log['voters']:
				address = log['voters'][voter]['address']
				toPayout = log['voters'][voter]['amountToPayout']
				voterName = voter
				f.write ('echo Sending ' + str(toPayout) + ' to ' + str(address) + ' owner name : ' + voterName +  '\n')

				data = { "secret": SECRET, "amount": int (toPayout * 100000000), "recipientId": address }
				if SECONDSECRET != None:
					data['secondSecret'] = SECONDSECRET

				f.write ('curl -k -H  "Content-Type: application/json" -X PUT -d \'' + json.dumps (data) + '\' ' + NODEPAY + "/api/transactions\n\n")
				f.write ('sleep 10\n')

			f.close ()	
				

if __name__ == "__main__":
	#Load logfile
	log = loadLog ()

	#Do Payouts
	doPayouts (log)

