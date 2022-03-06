#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input(str("Введите слово: "))
    word = list(word)

    third = word[2]
    last = word[-1]

    word[2] = last
    word[-1] = third

    print("".join(word))
