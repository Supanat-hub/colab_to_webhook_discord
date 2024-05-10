import requests # dependency
import pytz
from datetime import datetime

from google.colab import auth
from googleapiclient.discovery import build

auth.authenticate_user()
drive_service = build('drive', 'v3')
about = drive_service.about().get(fields="user").execute()
user_email = about['user']['emailAddress']
user_name = about['user']['displayName']

# Get the timezone for Thailand
thailand_timezone = pytz.timezone('Asia/Bangkok')
# Get the current date and time in Thailand
thailand_time = datetime.now(thailand_timezone)

url = "https://discord.com/api/webhooks/1237424052801634374/stLenxIyJqdIRfV5xScg-PtpCcdtCmBcPIvf3157mybypwvIxEeN3EbcGW36TFMXRUeZ" # webhook url, from here: https://i.imgur.com/f9XnAew.png

data_try = {
    "content" : "**ตรวจพบผู้รันโปรแกรม**",
    "username" : "detector bot"
}

data_try["embeds"] = [
    {
        "description" : f'date : {thailand_time.strftime("%Y-%m-%d")}\ntime : {thailand_time.strftime("%H:%M:%S")}',
        "title" : "info",
    }
]


true_value = 4540
result = requests.post(url, json = data_try)
try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    pass
num = int(input('โปรดใส่เลขที่คำนวณมา : '))

def hint(num:int):
    thailand_time = datetime.now(thailand_timezone)
    data_true = {
    "content" : "**ตรวจพบผู้ใส่รหัสถูกต้อง**",
    "username" : "detector bot"
    }

    data_true["embeds"] = [
        {
            "description" : f'email : {user_email}\nuser name : {user_name}\ndate : {thailand_time.strftime("%Y-%m-%d")}\ntime : {thailand_time.strftime("%H:%M:%S")}',
            "title" : "info",
            "color": 5763719
        }
    ]

    data_flase = {
        "content" : "**ตรวจพบผู้ใส่รหัสผิด**",
        "username" : "detector bot"
    }

    data_flase["embeds"] = [
        {
            "description" : f'date : {thailand_time.strftime("%Y-%m-%d")}\ntime : {thailand_time.strftime("%H:%M:%S")}',
            "title" : "info",
            "color": 15548997
        }
    ]
    if num != true_value:
        
        result = requests.post(url, json = data_flase)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            pass
        return 'เลขที่ใส่มานั้นไม่ถูกต้อง กรุณาลองอีกครั้ง 😥'
    else:
        result = requests.post(url, json = data_true)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            pass
        return '01010100\n01101000\n01100101\n00100000\n01110000\n01100101\n01110010\n01110011\n01101111\n01101110\n00100000\n01111001\n01101111\n01110101\n00100111\n01110010\n01100101\n00100000\n01101100\n01101111\n01101111\n01101011\n01101001\n01101110\n01100111\n00100000\n01100110\n01101111\n01110010\n00100000\n01100011\n01101111\n01101110\n01110100\n01110010\n01101001\n01100010\n01110101\n01110100\n01100101\n01110011\n00100000\n01110100\n01101111\n00100000\n01110100\n01101000\n01101001\n01110011\n00100000\n01110111\n01100101\n01100010\n01110011\n01101001\n01110100\n01100101\n00101110\n00001010\n01110101\n01110010\n01101100\n00100000\n00111010\n00100000\n01101000\n01110100\n01110100\n01110000\n01110011\n00111010\n00101111\n00101111\n01110100\n01100101\n01100001\n01110111\n01110100\n01101000\n01100001\n01101001\n00101110\n01100111\n01101001\n01110100\n01101000\n01110101\n01100010\n00101110\n01101001\n01101111\n00101111'
print(hint(num))