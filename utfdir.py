#!/usr/bin/python
# -*- coding: utf-8 -*-

# how to use:
# py utfdir "c:\123\"
# py utfdir "c:\123.txt"

# if you don't give any parameter, utfdir will process the dir it live in:
# py utfdir

import os
import sys
import chardet

if len(sys.argv) == 1:
    user_path = os.getcwd()
else:
    user_path = sys.argv[1]

# I was thinking about add "*.m" matlab files, but it's seems like matlab love
# Matlab prefers local encoding instead of UTF encoding.
file_types = ['.h', '.cpp', '.hpp', '.txt', '.py', '.md', '.py' ]

# change here if you want other code, not utf8
target_code = 'UTF-8-SIG'

# you can change here to 'ascii', if you want leave ascii files unchanged.
other_code_dont_need_to_decode = None

def encode_files_to_utf8(filename, ignore_extension=False):
    tmp = os.path.splitext(filename)[1]
    if tmp not in file_types and not ignore_extension:
        return
    handle = open(filename, "rb")
    data = handle.read()
    handle.close()
    if len(data) < 65536*4:
        guessed_code = chardet.detect(data)['encoding']
    else:
        guessed_code = chardet.detect(data[0:65536])['encoding']
    if guessed_code is None:
        return
    if guessed_code != target_code and guessed_code != other_code_dont_need_to_decode:
        print('code \"' + guessed_code + '\" found in file \"' + filename +
              '\", begin to process!')
        decoded_text = data.decode(guessed_code).encode(target_code)
        handle = open(filename, 'wb')
        handle.write(decoded_text)
        handle.close()


def walk_dir_than_process(input_dir):
    print('process into :\"' + input_dir + '\"')
    for root, dirs, files in os.walk(input_dir):
        for name in files:
            encode_files_to_utf8(os.path.join(root, name))

print("We are about to run utfdir at path \"" + user_path + "\"")
if os.path.exists(user_path):
    if os.path.isfile(user_path):
        encode_files_to_utf8(user_path, True)
    else:
        walk_dir_than_process(user_path)
    print("Success!!")
else:
    print(
        "The path you selected:\"" + user_path +
        "\" don't seems like a file or folder, utfdir will do nothing but exit."
    )

# 判断操作系统，如果是windows就让它暂停一下，这样windows用户看着爽。
if sys.platform == 'win32':
    os.system("pause")