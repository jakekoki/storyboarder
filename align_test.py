from afaligner import *
from nrclex import NRCLex
import re
import os

def _clean_html(raw_html):
    '''Isolates the words in each html tag from xhtml file of words.'''

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)

    return cleantext

def generate_xhtml_dict():
    xhtml = open("text_in/walden.xhtml", "r")
    xhtml_dict = {}
    for i, line in enumerate(xhtml.readlines()):
        idx = "f" + str(i)
        text = _clean_html(line)
        xhtml_dict[idx] = text.strip(" \n")

    return xhtml_dict

def process_fragment(fragment, xhtml_dict):
    for key, val in list(fragment.items()):
        fragment[key]['text'] = xhtml_dict[key]
        fragment[key]['emotion'] = NRCLex(xhtml_dict[key]).affect_frequencies

    return fragment

def output_json(sync_map, output_dir):
    xhtml_dict = generate_xhtml_dict()
    for text_path, fragments in sync_map.items():
        text_name = get_name_from_path(text_path)
        file_path = os.path.join(output_dir, f'{drop_extension(text_name)}.json')
        fragments = process_fragment(fragments, xhtml_dict)
        with open(file_path, 'w') as f:
            json.dump(fragments, f, indent=2)

sync_map = align(
    'text_in',
    'audio_in',
    output_dir="audio_out",
    output_format='json',
    skip_penalty=0.8,
    radius=100
)

output_json(sync_map, "audio_out")