# python-translator

Simple yet effective module for translating. 

### Can translate more than 5000 characters unlike Google Translate

Uses requests to access https://translate.google.com/ and fetches the translated text.

#### installation:

* ##### Windows:
    `pip install ptranslator`
    
    _Dont forget to add "<path_to_python>/Scripts" to PATH_
   
* ##### Linux:
    `sudo pip install ptranslator`
    
    _Probably won't run unless you use `sudo` when installing_

* ##### _installation problems:_
    In this case refer to this article:
    https://stackoverflow.com/questions/36092388/adding-installed-pip-package-to-path-automatically
    or if you need any aditional help please feel free to contact me :)

#### Usage:
 `ptranslator "text" to_language(default=en) from_language(optional)`
 
 ###### _In command line:_
    ```Shell
    > ptranslator "Hallo Welt!"
    Hello World!
    > ptranslator "Здраво Свете!" en
    Hello World!
    > ptranslator "Hola Mundo!" en es
    Hello World!
    ```
