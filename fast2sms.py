# send sms via fast2sms

import requests
import mechanicalsoup
import config

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
msg = "Data remaining: " + data + " GB"

url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=" + msg + "&language=english&route=p&numbers=8340238900,7821915962&flash=1"

headers = {
    'authorization': config.api,
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)

