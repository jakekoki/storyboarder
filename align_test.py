from afaligner import *
import re
import os

def clean_html(raw_html):
    '''Isolates the words in each html tag from xhtml file of words.'''

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)

    return cleantext

def final_output_json():
    xhtml = open("text_in/text.xhtml", "r")
    for i, line in enumerate(xhtml.readlines()):
        print(i, clean_html(line))

def output_json(sync_map, output_dir):
    for text_path, fragments in sync_map.items():
        text_name = get_name_from_path(text_path)
        # file_path = os.path.join(output_dir, f'{drop_extension(text_name)}.json')
        # print(file_path)
        print(fragments)
        break
        # with open(file_path, 'w') as f:
        #     json.dump(fragments, f, indent=2)

sync_map = align(
    'text_in',
    'audio_in',
    output_dir="audio_out",
    output_format='json'
)

# final_output_json()
# output_json(sync_map, "audio_out")