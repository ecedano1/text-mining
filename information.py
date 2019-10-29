# reddit@reddit-VirtualBox:~$ curl -X POST -d 'grant_type=password&username=ecedano1&password=ECedano11!' --user '1RjIws9QcWKMww:-K-88s47llEE3_1FASt-ey_UHZ4 
# ' https://www.reddit.com/api/v1/access_token

import requests
import requests.auth

client_auth = requests.auth.HTTPBasicAuth('1RjIws9QcWKMww', '-K-88s47llEE3_1FASt-ey_UHZ4')
post_data = {"grant_type": "password", "username": "ecedano1", "password": "ECedano11!"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
response.json()

# {'access_token': '228222014149-282vufm1HRjKyKaHWT0DepoUZlY', 'token_type': 'bearer', 'expires_in': 3600, 'scope': '*'}

headers = {"Authorization": "bearer 228222014149-282vufm1HRjKyKaHWT0DepoUZlY", "User-Agent": "ChangeMeClient/0.1 by ecedano1"}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
response.json()