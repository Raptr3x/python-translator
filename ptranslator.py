import re
import requests
import sys

desc = """
Name: python-translator

Usage:      ptranslator text to_language from_language

from_language and to_language are optional
to_language default is English
text that includes space needs to be inbetween double quotes

Example:
            ptranslator "Fahrrad"
            Bicycle
"""

def main():
    args = sys.argv
    if len(args) > 4 or len(args)<2:
        print(desc)
        return False
    txt = args[1]
    to_lang, from_lang="auto", "auto"
    if len(args)>2: to_lang = args[2]
    if len(args)>3: from_lang = args[3]

    translate(txt, to_lang, from_lang)

def translate(txt, to_lang, from_lang):
    
    head = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"}
    
    link = "http://translate.google.com/m?hl={}&sl={}&q={}".format(to_lang, from_lang, txt)
    r = requests.get(link, headers=head).text

    print(re.findall(r'class="t0">(.*?)<', r))

main()