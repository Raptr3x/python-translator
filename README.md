# python-translator

Simple yet effective module for translating. 


Uses requests to access https://translate.google.com/ and fetches the translated text.

###Not supported anymore

#### installation:

__[PyPI](https://pypi.org/project/ptranslator/)__

* ##### Windows:
    `pip install ptranslator`
    
    _Dont forget to add "<path_to_python>/Scripts" to PATH_
   
* ##### Linux:
    `sudo pip install ptranslator`
    
    _Probably won't run unless you use `sudo` when installing_

* ##### _installation problems:_
    In this case refer to this [article](https://stackoverflow.com/a/36160069/7775953) or if you need any aditional help please feel free to contact me :)

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
 
