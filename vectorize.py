import json
from roget import vectorize_word
from pathlib import Path
from typing import Dict

import argparse

def vectorize(text: str) -> Dict[str, int]:
    '''
    Returns a sparse 1042-dimentional vector with the amount of words in each category.
    '''
    result = {}
    for word in text.split():
        for category in vectorize_word(word):
            if category in result.keys():
                result[category] += 1
            else:
                result[category] = 1

    return result

def frequences(vector: Dict[str, int]) -> Dict[str, float]:
    total = sum((i for i in vector.values()))
    return {cat: freq / total * 100 for cat, freq in vector.items()}

if __name__ == "__main__":
    basepath = Path.cwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", 
                        type=str, 
                        help="Path to the file with words.", 
                        required=True
                        )
    parser.add_argument("-ov", 
                        type=str, 
                        help="Path to the output text file with the vector of the text.", 
                        required=False, 
                        default=str(basepath / Path("out_vector.txt"))
                        )
    parser.add_argument("-of", 
                        type=str, 
                        help="Path to the output text file with the frequences of the text.", 
                        required=False, 
                        default=str(basepath / Path("out_frequences.txt"))
                        )

    args = parser.parse_args()

    words = Path(args.i)
    output_vector = Path(args.ov)
    output_frequences = Path(args.of)

    convertion_table = json.loads(Path("convert.json").read_text())

    vector = vectorize(words.read_text().lower())

    vector = dict(reversed(sorted(vector.items(), key=lambda item: item[1])))
    converted = {str((key, convertion_table[key])): value for key, value in vector.items()}
    output_vector.write_text(json.dumps(converted, indent=2))
    freq = frequences(vector)
    converted = {str((key, convertion_table[key])): value for key, value in vector.items()}
    freq = dict(reversed(sorted(freq.items(), key=lambda item: item[1])))
    output_frequences.write_text(json.dumps(converted, indent=2))
