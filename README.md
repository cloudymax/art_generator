# Art Generator

Fun command line app to make word art using figlet

## Usage
font = sys.argv[1]
text_color = sys.argv[2]
bg_color = sys.argv[3]
payload = sys.argv[4]

```zsh
export FONT="poison"
export TEXT_COLOR="ansimagenta"
export BG_COLOR="ansigreen"
export PAYLOAD="Poison"

python3 art_generator.py $FONT $TEXT_COLOR $BG_COLOR $PAYLOAD

python3 art_generator.py "poison" "ansimagenta" "ansigreen" "Poison"
```

![Example](example.png)