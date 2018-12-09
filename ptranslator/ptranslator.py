import re
import requests
import sys

"""
MIT License

Copyright (c) 2018 Bogdan Čaleta Ivković

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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

    print(re.findall(r'class="t0">(.*?)<', r)[0])

if __name__ == '__main__':
    main()