# python-translator

Simple yet effective module for translating. 

### Can translate more than 5000 characters unlike Google Translate

Uses requests to access https://translate.google.com/ and fetches the translated text.

#### installation:

__[PyPI](https://pypi.org/project/ptranslator/)__

* ##### Windows:
    `pip install ptranslator`
    
    _Dont forget to add "<path_to_python>/Scripts" to PATH_
   
* ##### Linux:
    `sudo pip install ptranslator`
    
    _Probably won't run unless you use `sudo` when installing_

* ##### _installation problems:_
    In this case refer to this [article](https://stackoverflow.com/questions/36092388/adding-installed-pip-package-to-path-automatically) or if you need any aditional help please feel free to contact me :)

#### Usage:
 `ptranslator "text" to_language(default=en) from_language(optional)`
 
 * ###### _In command line:_
    ```
    > ptranslator "Hallo Welt!"
    Hello World!
    > ptranslator "Здраво Свете!" en
    Hello World!
    > ptranslator "Hola Mundo!" en es
    Hello World!
    ```
 * ###### _in python script:_
    ```
    from ptranslator import translate
    # translate( text , to_language , from_language )
    translate("Hello World!", "de")  #second and third arguments are optional
    #output: Hallo Welt!
    ```
 
