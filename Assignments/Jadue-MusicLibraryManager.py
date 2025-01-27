# Brandon Jadue
# 3/18/24
# This program will manage a music library using dictionaries.
import time

# music_library = { "Rock": { "ArtistA": {"Song1", "Song2"},
 #                           "ArtistB": {"Song3", "Song4"} },
 #                 "Pop": { "ArtistC": {"Song5", "Song6"},
 #                           "ArtistD": {"Song7", "Song8"} } }

# creating dictionary
music_library_manager = {}
#1
def addSong():
    # user input
    genre = input("Enter the genre of your song: \n")
    artist = input("Enter the artist of your song: \n")
    song = input("Enter the title of your song: \n")
    # create dictionary if it does not exist
    if genre not in music_library_manager:
        music_library_manager[genre] = {}
    if artist not in music_library_manager[genre]:
        music_library_manager[genre][artist] = []
    music_library_manager[genre][artist].append(song)
    print(f'Added "{song}" by {artist} to your library.')
#2
def editSong():
    choice = input("Edit artist or song? (1-2): \n")
    if choice == "1":
        for genre in music_library_manager:
            for key in music_library_manager[genre]:
                print(key)
        oldArtist = input("Enter the artist you want to edit: \n")
        newArtist = input("Enter the new name of the artist: \n")
        for genre in music_library_manager:
            if oldArtist in music_library_manager[genre]:
                for value in music_library_manager[genre][oldArtist]:
                    migrating = []
                    migrating.append(value)
                del music_library_manager[genre][oldArtist]
                music_library_manager[genre][newArtist] = []
                music_library_manager[genre][newArtist] = migrating

    elif choice == '2':
        artist = input("Enter the artist of the song you want to edit: \n")
        for genre in music_library_manager:
            if artist in music_library_manager[genre]:
                print(f"The following songs have been found for {artist}.")
                print(music_library_manager[genre][artist])
                oldSongName = input("Which one do you want to edit?:\n")
                newSongName = input(f"Enter the new name for {oldSongName}:\n")
                music_library_manager[genre][artist].remove(oldSongName)
                music_library_manager[genre][artist].append(newSongName)
            else:
                continue
#3
def showLibrary():
    for genre in music_library_manager:
        print(f"{genre}--")
        for artist in music_library_manager[genre]:
            print(f"\t{artist}")
            for song in music_library_manager[genre][artist]:
                print(f"\t\t{song}")
#4
def songCount():
    print("\nAvailable artists:")
    for genre in music_library_manager:
        for key in music_library_manager[genre]:
            print(key)
    artist = input("Enter the artist you would like to count: \n")
    for genre in music_library_manager:
        if artist in music_library_manager[genre]:
            count = len(music_library_manager[genre][artist])
            print(f"{artist} has {count} song(s).")
        else:
            continue
#5
def genreCount():
    count1 = 0
    count2 = 0
    print("\nAvailable genres:")
    for key in music_library_manager:
        print (key)
    genre1 = input("Enter the first genre you would like to compare:\n")
    genre2 = input("Enter the second genre you would like to compare:\n")
    for artist in music_library_manager[genre1]:
        count1 += int(len(music_library_manager[genre1][artist]))
    for artist in music_library_manager[genre2]:
        count2 += int(len(music_library_manager[genre2][artist]))
    if count1 > count2:
        print(f"{genre1} has more songs.")
    elif count2 > count1:
        print(f"{genre2} has more songs.")
#6
def uniqueArtist():
    count = 0
    for genre in music_library_manager:
        for artist in music_library_manager[genre]:
            print(artist)
            count += 1
    print(f"There are {count} unique artists in your library.")
#7
def saveLibrary():
    usrLibName = input("Enter the name of the file you would like to save to:\n")
    libraryFile = open(f"{usrLibName}_library.txt", "w")
    libraryFile.write(f"Music Library - {usrLibName.upper()}")
    libraryFile.close()
    libraryFile = open(f"{usrLibName}_library.txt", "a")
    for genre in music_library_manager:
        libraryFile.write(f"\n{genre}--")
        for artist in music_library_manager[genre]:
            libraryFile.write(f"\n\t{artist}")
            for song in music_library_manager[genre][artist]:
                libraryFile.write(f"\n\t\t{song}")
    libraryFile.close()
    print(f"Library has been save to {usrLibName}_library.txt")

def menu():
    print("\nPlease select an action."
          "\n1. Add a song to your library."
          "\n2. Edit song info from your library."
          "\n3. Show libary."
          "\n4. Display how many songs are by a specific artist."
          "\n5. Compare genres."
          "\n6. Display all unique artists in the libary."
          "\n7. Save your library to a text file."
          "\nType 'Exit' to close the program.")
    usrChoice = input("\n(1-7)\n")
    return usrChoice

def main():
    # defining repeat variable
    goAgain = 'y'
    print("Welcome to the Music Library Manager")
    # repeat function
    while goAgain.lower() == 'y':
        time.sleep(1)
        usrChoice = menu()
        if usrChoice == "1":
            addSong()
        elif usrChoice == "2":
            editSong()
        elif usrChoice == '3':
            showLibrary()
            time.sleep(1)
        elif usrChoice == '4':
            songCount()
        elif usrChoice == '5':
            genreCount()
        elif usrChoice == '6':
            uniqueArtist()
        elif usrChoice == '7':
            saveLibrary()
        elif usrChoice.lower() == 'exit':
            print("Bye.")
            goAgain = 'n'
        else:
            print('Not a valid option.')

if __name__ == '__main__':
    main()
