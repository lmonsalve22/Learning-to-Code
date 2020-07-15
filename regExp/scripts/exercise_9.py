"""Write a Python program to extract
year, month and date from a an url."""

import re

def finder(url):
    return re.findall(r'\d{4,4}\/\d{2,2}\/\d{2,2}', url)

print(finder('url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"'))
print(finder('https://www.washingtonpost.com/world/middle_east/coronavirus-united-arab-emirates-dubai-abu-dhabi/2020/07/12/23fbfef2-bf89-11ea-8908-68a2b9eae9e0_story.html'))
