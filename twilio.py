# send sms via twilio

import mechanicalsoup
import config
from twilio.rest import Client

def get_data():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://login.uninet.co.in")
    browser.select_form('form[action="https://login.uninet.co.in/login/process"]')
    browser["unme"] = config.username
    browser["passd"] = config.password

    browser.submit_selected()
    data = browser.get_current_page().find_all('h6')
    data = data[0].getText()
    data = data[:5]
    return data

data = get_data()
msg = "test Data remaining: " + data + " GB"

account = config.account
token = config.token
client = Client(account, token)

myTwilioNumber = "+12569065814"
samrat = "+918340238900"
aditya = "+917821915962"

message1 = client.messages.create(body = msg, from_=myTwilioNumber, to=samrat)
message2 = client.messages.create(body = msg, from_=myTwilioNumber, to=aditya)


