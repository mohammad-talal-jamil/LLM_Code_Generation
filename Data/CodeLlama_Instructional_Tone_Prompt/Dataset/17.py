def parse_music(music_string):
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    music_list = music_string.split()
    return [note_dict[note] for note in music_list]
