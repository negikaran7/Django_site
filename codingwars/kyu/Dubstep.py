def song_decoder(song):
    return " ".join(song.replace("WUB", " ").split())


# def song_decoder(song):
#     song = song.split('WUB')
#     new_song = []
#     for i in song:
#         if i != '':
#             new_song += [i]
#     return " ".join(new_song)
