music_list = [
    {
        "artist": "Radiohead",
        "song name": "How to Disappear Completely",
        "Album": "Kid A",
        "genre": "Alt Rock"
    },
    {
        "artist": "My Chemical Romance",
        "song name": "Sleep",
        "Album": "The Black Parade",
        "genre": "Emo"
    },
    {
        "artist": "Killing Joke",
        "song name": "Slave To Substance",
        "Album": "Absolute Dissent",
        "genre": "Industrial Metal"
    },
]

empty = []

for i in music_list:
    empty.append(list(i.values())[0])

def add_to_list(band):
    empty.append(band)