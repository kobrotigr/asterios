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
        boss_name = 'Death Lord Hallate'
        if boss_name in table.prettify():
            mixer.init()
            mixer.music.load('sound.mp3')
            mixer.music.play()
            print(datetime.datetime.now(), 'boss has been killed: ', boss_name)

        a = table.find('a')
        print(datetime.datetime.now(), 'last killed boss was:', a.next_element)
        time.sleep(6)


if __name__ == '__main__':
    main()
