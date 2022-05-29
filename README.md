# Roget 

Repository for roget text vectorizer for the "Semantic Analysis of Group Values Structure Using Roget Thesaurus: Automated Algorithm" paper.

## What is it?

The authors have written a script in Python. The program is publicly available and can be used for a wide range of research. For this purpose it is necessary to download the .zip file archive, which can be found at https://github.com/chameleon-lizard/Roget, and then unzip it. The program itself is started via the gui.exe file in the gui folder, after which a window with four quadrants opens. The Input window displays the input data to be entered into the input.txt file, which is located in the Roget-main folder. After clicking the Vectorize button, the results are displayed in the two quadrants of Output. Both upper and lower quadrants show the code, the name of the semantic group belonging to it, and the occurrence of this code in the word array under test. The upper quadrant shows how many times this semantic group occurred in the array in absolute values, the lower quadrant shows the frequency of the code/semantic group as a percentage of the total number of codes. The data is automatically exported to the files created in each session in the Roget-main folder, and the data in them is automatically updated after the program runs. Codes with absolute numbers are in the file vector.json, and those with percentages are in frequencies.json. Besides, the file non-recognized.txt contains all the words to which no correspondence was found in the thesaurus.
The most convenient data format for further work is a vector consisting of 1044 values. The position number is a number of semantic group code (codes are lined up in ascending order), the value is the frequency of occurrence of a given code as a decimal fraction (without percent). Exactly such vectors were used in all subsequent operations.

If you want to vectorize a text by yourself, try using [this file](https://raw.githubusercontent.com/chameleon-lizard/Roget/main/input.txt) as an input.

## Installation

All in the releases. Don't even think about trying to build it on your own, it's dependency hell.

If you still want to do this by yourself, you'll need to:
- Download `roget-tools`
- Install `spacy`, `tkinter`, `en_core_web_lg` language model for spacy and `pyinstaller`
- Build `gui.py` via the `pyinstaller` (without the -F flag!)
- Copy `roget-tools` to the `dist/gui`
- Copy `en_core_web_lg` from wherever pip downloaded it into the `dist/gui`
- Copy `convert.json` into the `dist/gui`

## How to cite:
Andreyuk D., Livitina A., Sushko N. (2022) "Semantic Analysis of Group Values Structure Using Roget Thesaurus: Automated Algorithm" Gosudarstvennoe upravlenie. Elektronniy vestnik, iss.91, p.148-161. DOI: 10.24412/2070-1381-2022-91-148-161 (online available at http://ee-journal.spa.msu.ru/vestnik/item/91_2022andreyuk_levitina_sushko.htm)
