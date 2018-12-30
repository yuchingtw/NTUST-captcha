# -*- coding: utf-8 -*-

__version__ = '0.1'

import pickle
import numpy as np
from PIL import Image


def load_data(data_path='.'):
    with open('data.data', 'rb') as fp:
        data = pickle.load(fp)
    with open('label.data', 'rb') as fp:
        label = pickle.load(fp)

    return data, label


def convert_to_bw(img):
    '''Convert image to black/white makes them easy to process.'''
    img = img.convert('1')
    return img


def crop_image(img):
    numbers = [None] * 3
    numbers[1] = img.crop((31, 0, 45, 40))
    numbers[2] = img.crop((49, 0, 63, 40))
    numbers[0] = img.crop((13, 0, 27, 40))

    alphabets = [None] * 3
    alphabets[0] = img.crop((66, 0, 84, 40))
    alphabets[1] = img.crop((90, 0, 101, 40))
    alphabets[2] = img.crop((105, 0, 120, 40))

    return numbers, alphabets


def convert(img):

    data, label = load_data()

    img = convert_to_bw(img)

    numbers, alphabets = crop_image(img)

    '''Convert by minimum MSE of samples.'''
    text = ''
    for i in numbers:
        mse = [((i - x) ** 2).mean() for x in data[0]]
        text += label[0][mse.index(min(mse))]

    for i in enumerate(alphabets, start=1):
        mse = [((i[1] - x) ** 2).mean() for x in data[i[0]]]
        text += label[1][mse.index(min(mse))]
    return text


def test():
    from datetime import datetime

    img = Image.open("VCode.png")
    start = datetime.now()
    text = convert(img)

    print(text, 'spent:', datetime.now() - start)


if __name__ == '__main__':
    test()
