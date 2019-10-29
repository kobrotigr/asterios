import os
import time

import requests
from bs4 import BeautifulSoup


def main():
    while True:
        r = requests.get('https://asterios.tm/index.php?cmd=rss&serv=8&filter=keyboss')
        bs = BeautifulSoup(r.text, 'html.parser')
        table = bs.find('table', width=650)
        if 'Death Lord Hallate' in table.prettify():
            # your alert here!
            print('yes')

        a = table.find('a')
        print('last boss was:', a.next_element)
        time.sleep(6)

        # ========================================================================
        # os.system('aplay sound.mp3')
        # winsound.PlaySound('sound.mp3', winsound.SND_ASYNC)
        # ========================================================================


if __name__ == '__main__':
    main()
