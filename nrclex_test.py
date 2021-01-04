from nrclex import NRCLex

text_object = NRCLex(
'''
She stretched hers eagerly and gratefully towards him.
'''
)
#Return words list.

text_object.words


#Return sentences list.

print(text_object.sentences)


#Return affect list.

print(text_object.affect_list)


#Return affect dictionary.

print(text_object.affect_dict)


#Return raw emotional counts.

print(text_object.raw_emotion_scores)


#Return highest emotions.

print(text_object.top_emotions)


#Return affect frequencies.

print(text_object.affect_frequencies)

# Kinda cool but maybe a little underpowered..