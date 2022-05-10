#!/usr/bin/env python3 -u
import os
import random

def readFile(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    return list(map(lambda x: x.strip(), filter(lambda x: len(x.strip().split("\t")) > 1, lines)))

def list_to_columned_list(lis): 
    listed = list(map(lambda x: x.split("\t"), lis))
    transposedLIst = [*zip(*listed)]
    return transposedLIst

langs = ["spa", "ita", "ces", "eng", "fra", "hun", "lat", "rus"]
level = "word"
lang = "mon"
traind = readFile(f'dataset/{lang}.word.train.tsv')
random.shuffle(traind)
train = list_to_columned_list(traind)
test = list_to_columned_list(readFile(f'dataset/{lang}.{level}.dev.tsv'))
play = list_to_columned_list(readFile(f'dataset/{lang}.{level}.dev.tsv'))
print(lang)
train_body = train[0]
train_tran = train[1]
test_body = test[0]
test_tran = test[1]
play_body = play[0]
play_tran = play[1]
print("total body: %i" % len(train_body))
print("total morph: %i" % len(train_body))


def convert_morph(line):
    line = str(line).replace(" @@", "@").replace(" ", "_").replace("\n", "")
    return ' '.join(line)


def convert_main(line):
    line = str(line).replace(" ", "_").replace("\n", "")
    return ' '.join(line)


os.makedirs('data/morph', exist_ok=True)
with open(f'data/morph/train.{lang}', 'w', encoding='utf-8') as f:
    lines = [convert_main(line) for line in train_body[:]]
    f.write('\n'.join(lines) + '\n')
with open(f'data/morph/train.{lang}morph', 'w', encoding='utf-8') as f:
    lines = [convert_morph(line) for line in train_tran[:]]
    f.write('\n'.join(lines) + '\n')
with open(f'data/morph/valid.{lang}', 'w', encoding='utf-8') as f:
    lines = [convert_main(line) for line in play_body[:]]
    f.write('\n'.join(lines) + '\n')
with open(f'data/morph/valid.{lang}morph', 'w', encoding='utf-8') as f:
    lines = [convert_morph(line) for line in play_tran[:]]
    f.write('\n'.join(lines) + '\n')
with open(f'data/morph/test.{lang}', 'w', encoding='utf-8') as f:
    lines = [convert_main(line) for line in test_body[:]]
    f.write('\n'.join(lines) + '\n')
with open(f'data/morph/test.{lang}morph', 'w', encoding='utf-8') as f:
    lines = [convert_morph(line) for line in test_tran[:]]
    f.write('\n'.join(lines) + '\n')
