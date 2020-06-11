from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)

# cred = "YWFjMzFhZDYtNWE0Ny00NGU3LTk0OTMtNTdmMzFkMjEwMDA1MzE4YjJjNDUtZTdh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
cred = "N2UyNGY5ZjEtMjBlOS00YmVlLTgxYWItZmYzM2QxNmI0YjBkYmExZjNlMWQtN2Mw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

def getMessage(id):
    print(1)
    header={"Authorization":"Bearer {}".format(cred)}
    url="https://webexapis.com/v1/messages/{}".format(id)
    messageData=requests.get(url,headers=header).json()
    return [messageData['text'],messageData['roomId']]

def doProcessandReply(room,message):
    print(2)
    header = {"Content-Type":"application/json","Authorization":"Bearer {}".format(cred)}
    url="https://webexapis.com/v1/messages"
    
    if 'add User' in message:
        print(message)
        messForm = message.split(' ')
        userId = messForm[2]
        firstName = messForm[3]
        lastName = messForm[4]
        pin = messForm[5]
        password = messForm[6]
        print(userId)
        soapUrl="https://10.10.20.1/axl/"
        soapheaders = {'Content-type':'text/html','SOAPAction':'CUCM:DB ver=10.0'}
        payload='''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/10.0">
                <soapenv:Header/>
                <soapenv:Body>
                <ns:addUser>
                <user>
                <userid>{}</userid>
                <firstName> {}</firstName>
                <lastName>{}</lastName>
                <pin>{}</pin>
                <password>{}</password>
                </user>
                </ns:addUser>
                </soapenv:Body>
                </soapenv:Envelope>'''.format(userId,firstName,lastName,pin,password)
        resp=requests.post(soapUrl,headers=soapheaders,data=payload,verify=False, auth=("administrator","ciscopsdt"))



        print(resp.status_code)
        # print(room)
        payload={"text":"Task is done :))","roomId":"{}".format(room)}
        resp=requests.post(url,headers=header,data=json.dumps(payload))
        print(resp.text)
        return resp.text
    elif 'do jabber provision' in message:
        messForm = message.split(' ')
        line = messForm[3]
        soapUrl="https://10.10.20.1/axl/"
        soapheaders = {'Content-type':'text/html','SOAPAction':'CUCM:DB ver=10.0'}
        payload='''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/10.0">
	                <soapenv:Header/>
                        <soapenv:Body>
                            <ns:addLine>
                                <line>
                                    <pattern>{}</pattern>
                                    <usage></usage>
                                </line>
                                
                                
                            </ns:addLine>
                            
                        </soapenv:Body>
                    </soapenv:Envelope>'''.format(line)
        resp=requests.post(soapUrl,headers=soapheaders,data=payload,verify=False, auth=("administrator","ciscopsdt"))
        print(resp.json())
        payload={"text":"Task is done :))","roomId":"{}".format(room)}
        resp=requests.post(url,headers=header,data=json.dumps(payload))
        print(resp.text)
        return resp.text
    elif message=='do task3':
        print(room)
        payload={"text":"Task is done :))","roomId":"{}".format(room)}
        resp=requests.post(url,headers=header,data=json.dumps(payload))
        print(resp.text)
        return resp.text
    elif message=='do task4':
        print(room)
        payload={"text":"Task is done :))","roomId":"{}".format(room)}
        resp=requests.post(url,headers=header,data=json.dumps(payload))
        print(resp.text)
        return resp.text
    

@app.route('/', methods=['POST'])
def receiveMessage():
    messageId=request.json["data"]["id"]
    # print(messageId)
    message,room=getMessage(messageId)
    print("here")
    reply=doProcessandReply(room,message)
    return reply

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()