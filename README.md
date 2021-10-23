# Roget 

Simple script to get stuff from [Roget's hyperlinked thesaurus site](http://www.roget.org). All the credit goes to them, I'm just fooling their robots.txt.

## Installation

Use virtual environments. They're cool.

```
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

If you're lazy, you can just do

```
pip install -r requrements.txt
```

## Usage
- `python roget.py -h` - gives you help.
- `python roget.py -i input.txt` - uses space-separated words in input.txt to get their groups in the roget thesaurus and save them into out.json
- `python roget.py -i input.txt -o output.json` - same as above, but with explicitly defined output path.