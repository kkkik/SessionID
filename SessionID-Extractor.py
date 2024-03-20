import requests
from user_agent import generate_user_agent
token=input(f"\x1b[1;36mEnter Token: ")
id=input("\x1b[1;36mEnter Id:")
def Send_to_Telegram(token,id):
	req = requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + str +"&text=" + str(message))
	print("تم ارساله بنجاح ، تاكد انك ارسلت /start مسبقًا .")
def Extract(user,password):
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '2.4901',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()) ,
        'viewport-width': '809',
        'x-asbd-id': '129477',
        'x-csrftoken': 'xmHxyNUhnRrSp13eJy8vuPPcr0XvUtNZ',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1008158962',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': f'{user}',
    }
    k= requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
    if "userId" in k.text:
            geto = k.cookies
            sessss= geto.get_dict()
            sesss = sessss['csrftoken']
            sess = f"{sessss['sessionid']}"
            message = f"""==============\n Done Extract The Session \n==============\n - Session : [ {sess} ] .\n - Dev @K_n_y\n=============="""
            print(f"\x1b[1;32m"+sess)
            Send_to_Telegram(token,id)
    elif "checkpoint_url" in k.text:
        print(
        f"\x1b[1;33m- This Account Are secured ."
        )
    else:
        print(
        f"\x1b[1;31m- Login Information are not same .\x1b[1;31m"
        )
        # Connections Are From Channel . Not mine (@K _ N _ Y)
Extract(user=input(f"\x1b[1;37mEnter User:\x1b[1;37m"),password=input(f"\nEnter Pass:"));exit("- Dev @k_n_y .")