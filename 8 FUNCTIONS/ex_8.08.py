'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop.'''

def make_album(artist, title, songs = None):
    if songs:
        alb = {'Artist':artist, 'Title':title}
        if songs:
            alb['songs'] = songs
    else:
        alb = {'Artist':artist, 'Title':title}
    return alb


print("Please enter the information about the album and the songs.")
while True:
    print("Enter 'q' when you done...")
    artist = input("Who is the artist: ")
    if artist == 'q':
        break
    title = input("Enter the title: ")
    if title == 'q':
        break
    songs = input("Enter no. of songs: ")
    if songs == 'q':
        break

    album = make_album(artist,title,songs)
    print(album) 