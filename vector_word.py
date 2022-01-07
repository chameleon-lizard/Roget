from typing import List, Dict
from pathlib import Path

from roget_tools_master.roget import Roget
import argparse
import json

def vectorize_word(word: str) -> List[str]:
    r = Roget()
    if word in r.thes_dict.keys():
        return [i[3:] for i in r.thes_dict[word]]
    else:
        return []

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
