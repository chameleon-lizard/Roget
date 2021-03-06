from typing import List, Dict
from pathlib import Path
from time import sleep

import argparse
import requests
import json
import re

def vectorize_word(word: str) -> List[str]:
    url = "http://www.roget.org/scripts/qq.php"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.roget.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'http://www.roget.org/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-GPC': '1',
    }
    
    data = {
        'seekword': word
    }
    response = requests.post(url, headers=headers, data=data)
    groups = re.findall(re.compile("(<b>#\d\d\d\d|<b>#\d\d\da|<b>#\d\d\db|<b>#\d\d\d|<b>#\d\da|<b>#\d\d|<b>#\d)"), response.text)
    result = [str(number[4:]) for number in groups]

    sleep(0.3)

    return result

def getWordGroups(seekwords: List[str]) -> Dict[str, List[int]]:
    result = {}
    for word in seekwords:
        result[word] = vectorize_word(word)

    return result

if __name__ == "__main__":
    basepath = Path.cwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", 
                        type=str, 
                        help="Path to the file with words.", 
                        required=True
                        )
    parser.add_argument("-o", 
                        type=str, 
                        help="Path to the output JSON file with words as keys and lists of integer groups as values.", 
                        required=False, 
                        default=str(basepath / Path("out.json"))
                        )

    args = parser.parse_args()

    words = Path(args.i)
    output = Path(args.o)

    result = getWordGroups(words.read_text().lower().split())
    output.write_text(json.dumps(result, indent=2))
