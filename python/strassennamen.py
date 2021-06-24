import sys
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def plotting_all(dicti, filename, number_streets, better_name):
    plt.title(f'Anzahl an Straßen: {number_streets} - {better_name}')
    plt.bar(*zip(*dicti.items()))
    plt.xlim(-.6, len(dicti) - .4)

    plt.axes([0.22, 0.51, 0.76, 0.425])
    plt.bar(*zip(*dicti.items()))
    plt.xlim(-.6, len(dicti) - .4)
    plt.yscale('log')

    plt.savefig(filename)


def plotting_first(dicti, filename, number_streets, better_name):
    plt.title(f'Anzahl an Straßen: {number_streets} - {better_name}')
    plt.bar(*zip(*dicti.items()))
    plt.xlim(-.6, len(dicti) - .4)

    plt.axes([0.33, 0.44, 0.65, 0.495])
    plt.bar(*zip(*dicti.items()))
    plt.xlim(-.6, len(dicti) - .4)
    plt.yscale('log')

    plt.savefig(filename)


def split(word):
    return [char for char in word]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        words = f.read().split('\n')
    words = words[1:-1]

    firstletter = ""
    str = ""

    for word in words:
        firstletter += word[0]
        word = word.lower()
        str += word

    countsC = Counter(split(str))
    counts = dict()
    for key, elem in countsC.most_common(np.unique(split(str)).size):
        counts[key] = elem

    countsL = Counter(split(firstletter))
    firstL = dict()
    for key, elem in countsL.most_common(np.unique(split(firstletter)).size):
        firstL[key] = elem

    plt.figure(constrained_layout=True)
    plotting_all(counts, 'build/strassen-gesamt.pdf', len(words), "Häufigkeit Gesamt")

    plt.figure(constrained_layout=True, figsize=(5, 5))
    plotting_all(counts, 'build/strassen-gesamt.png', len(words), "Häufigkeit Gesamt")

    plt.figure(constrained_layout=True)
    plotting_first(firstL, 'build/strassen-first.pdf', len(words), "Häufigkeit Erster Buchstabe")

    plt.figure(constrained_layout=True, figsize=(5, 5))
    plotting_first(firstL, 'build/strassen-first.png', len(words), "Häufigkeit Erster Buchstabe")
