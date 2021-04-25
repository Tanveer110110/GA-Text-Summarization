import os
import numpy as np
from sacremoses import MosesTokenizer

def read_vocab():
    dictionary = list()
    with open("vocab.txt", "r", encoding='utf-8') as in_file:
        vocab_lines = in_file.readlines()

        for line in vocab_lines:
            dictionary.append(line.rstrip())

    return dictionary

def build_vocab():
    vocab_file = "vocab.txt"
    vocab_list = list()
    tokenizer = MosesTokenizer(lang='en')

    for file in os.listdir("dataset/body"):
        filename = os.fsdecode(file)

        with open(f"dataset/body/{filename}", 'r', encoding='utf-8') as in_file:
            corpus_lines = in_file.readlines()
            corpus_lines = tokenizer.tokenize(corpus_lines)

            for line in corpus_lines:
                for word in line.split():
                    if word.lower() not in vocab_list:
                        vocab_list.append(word.lower())

    with open(vocab_file, 'w', encoding='utf-8') as out_file:
        for word in vocab_list:
            out_file.write(f"{word}\n")

def create_dictionary(words, weights):
    dictionary = {}
    for i in range(len(words)):
        dictionary[words[i]] = weights[i]

    return dictionary
