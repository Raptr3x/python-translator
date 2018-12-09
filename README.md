# python-translator

.. image:: https://img.shields.io/pypi/v/pip.svg
   :target: https://pypi.org/project/ptranslator/

Simple yet effective module for translating. 

### Can translate more than 5000 characters unlike Google Translate

Uses requests to access https://translate.google.com/ and fetches the translated text.

#### install:
    `pip install ptranslator`


#### Usage:
 `ptranslator "text" to_language(default=en) from_language(optional)`
 
 ###### _In command line:_
    ```
    > ptranslator "Hallo Welt!"
    Hello World!
    > ptranslator "Здраво Свете!" en
    Hello World!
    > ptranslator "Hola Mundo!" en es
    Hello World!
    ```
