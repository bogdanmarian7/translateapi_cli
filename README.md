# translateapi_cli
CLI Translate client which uses the free and open source [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) api, self-hosted .

## Install:
Create a virtual environment with virtualenv or with conda and activate it.
Then install using setup.py

To install using virtualenv, run the following commands:
```cmd
virtualenv env -p python3
env\Scripts\activate

pip install .
```

## Use:
Run "translate-cli" in cmd using the following arguments:
```cmd
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Text to be translated or path to
                        a text file or directory which
                        contains text files
  -sl [SLANG], --slang [SLANG]
                        Source language.
  -tl [TLANG], --tlang [TLANG]
                        Target language.
  -s [SAVE], --save [SAVE]
                        Save translations as text files.
```

### Examples:

- To translate the sentence "Programming is fun." from english to german language we use the following syntax:
```cmd
translate-cli -t "Programming is fun." -sl en -tl de
```
output:
```cmd
Programmierung macht Spaß.
```
- To translate text files inside a directory we pass the directory path to -t:
```cmd
translate-cli -t C:\Dir\DirToTranslate -sl en -tl de

```
- To translate a specific text file, we give its full path to -t:
```cmd
translate-cli -t C:\Dir\text_file.txt -sl en -tl de
```
>**Note:** All the examples are set to translate the text from english to german.
>To change the languages, modify -sl and -tl argumens.


To see the available languages, in python interpreter run the following commands:
```python
from src.helpers import translateapi
from pprint import pprint
ob = translateapi.TranslateApi()
pprint(ob.supported_languages())
```

>**Note:** In this project, the default url for API is a public one. To change it, change the value of DEFAULT_URL
inside [translateapi.py](https://github.com/bogdanmarian7/translateapi_cli/blob/main/src/helpers/translateapi.py)
If you self host the [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)  api, you should change the value of DEFAULT_URL to "http://localhost:5000"
