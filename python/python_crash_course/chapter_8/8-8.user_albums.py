""" Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s 
artist and title. Once you have that information, call 
make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop. """

def make_album(name, album_title):
    return {'name': name, 'album': album_title}

while True:
    print('just enter "q" to quit')
    artist_name = input('What\'s the name of the artist?: ')
    if artist_name == 'q':
        break
    artist_album = input('Wha\'s the name of the album?: ')
    if artist_album == 'q':
        break

    info = make_album(artist_name, artist_album)

    print(info)