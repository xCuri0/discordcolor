# discordcolor
script to change discord's accent colors
## usage
first extract discord's css by opening devtools, going to sources and then saving the css file.

use the script like this for it to output css for your new colors into your terminal. you can apply the css it generates using beautifuldiscord or something similar
```
./discordcolor.py ./discord.css '#e267af' '#d762a6'
```
## dependencies
* python3
* cssutils