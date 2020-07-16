"""Finding a url in a script"""

import re

def finder(url):
    """using findall""" 
    regex = 'https?:\/\/[\w]+\.\w+[\.\w]+[\/\w]*-?'
    content = re.findall(regex, url)
    print(content)

finder('<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>')

finder('<script type="text/javascript" async="" src="https://cse.google.com/cse.js?cx=013584948386948090933:pjqiqxq1drs"></script>')