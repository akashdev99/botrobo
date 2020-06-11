import requests
import json

# auth ="YWFjMzFhZDYtNWE0Ny00NGU3LTk0OTMtNTdmMzFkMjEwMDA1MzE4YjJjNDUtZTdh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
auth ="N2UyNGY5ZjEtMjBlOS00YmVlLTgxYWItZmYzM2QxNmI0YjBkYmExZjNlMWQtN2Mw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
header = {"Content-Type":"application/json","Authorization":"Bearer {}".format(auth)}
url ="https://webexapis.com/v1/webhooks"
payload={
    "name":"bothooks",
    "targetUrl":"http://9bcba3d816a9.ngrok.io",
    "resource":"messages",
    "event":"created"
}
info=requests.post(url,headers=header,data=json.dumps(payload))
print(info.json())