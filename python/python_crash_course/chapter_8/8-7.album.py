""" Write a function called make_album() that builds 
a dictionary describing a music album. The function should
take in an artist name and an album title, and it should 
return a dictionary containing these two pieces of information. """

def make_album(name, album_title, tracks=''):
    if tracks:
        full_info = {'name': name, 'album': album_title, 'tracks': tracks}
    else:
        full_info = {'name': name, 'album': album_title}
    
    return full_info

print(make_album('james', 'pureza lyrikal'))
print(make_album('lp', 'covers'))
print(make_album('james', 'pureza lyrikal', 12))
