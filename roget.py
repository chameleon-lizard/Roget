from typing import List, Dict
from pathlib import Path

import argparse
import requests
import json
import re

def getWordGroups(seekwords: List[str]) -> Dict[str, List[int]]:
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
    result = {}
    for word in seekwords:
        data = {
            'seekword': word
        }
        response = requests.post(url, headers=headers, data=data)
        groups = re.findall("<b>#\d\d\d", response.text)
        result[word] = [int(number[4:]) for number in groups]

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
