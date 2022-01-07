# Roget 

Text vectorization using [roget-tools](https://github.com/prpole/roget-tools). 

## Installation

All in the releases. Don't even think about trying to build it on your own, it's dependency hell.

If you still want to do this by yourself, you'll need to:
- Download `roget-tools`
- Install `spacy`, `tkinter`, `en_core_web_lg` language model for spacy and `pyinstaller`
- Build `gui.py` via the `pyinstaller` (without the -F flag!)
- Copy `roget-tools` to the `dist/gui`
- Copy `en_core_web_lg` from wherever pip downloaded it into the `dist/gui`
- Copy `convert.json` into the `dist/gui`

I am deeply sorry for all of this.
