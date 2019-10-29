import logging
import time
import datetime

import requests
from pygame import mixer
from bs4 import BeautifulSoup


def main():
    while True:
        r = requests.get('https://asterios.tm/index.php?cmd=rss&serv=8&filter=keyboss')
        bs = BeautifulSoup(r.text, 'html.parser')
        table = bs.find('table', width=650)

        # your boss name
        boss_name = 'Death Lord Hallate'

        if boss_name in table.prettify():
            mixer.init()
            mixer.music.load('sound.mp3')
            mixer.music.play()
            msg = f'{datetime.datetime.now()} Killed: {boss_name}'
            logging.warning(msg)

        a = table.find('a')
        msg = f'{datetime.datetime.now()} Last Killed: {a.next_element}'
        logging.warning(msg)
        time.sleep(6)


if __name__ == '__main__':
    main()
