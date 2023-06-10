import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

progress_bar = tqdm(total=2)

array = ["player1", "player2", "player3"]
out = []

def check_username(username):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    json = response.json() if response.status_code == 200 else None
    if json and "id" in json:
        out.append(username)
    progress_bar.update()

def check_usernames():
    progress_bar.reset(total=len(array))
    for username in array:
        check_username(username)
    progress_bar.close()
    with open('output.txt', 'w') as f:
        f.write(f'["{", ".join(out)}"]')
        print('Done.')
    print(out)

check_usernames()
