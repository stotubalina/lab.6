#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    sentence = input("Введите предложение: ")
    sentence = sentence.replace('c', '')
    sentence = sentence.replace('с', '')
    sentence = sentence.replace('C', '')
    sentence = sentence.replace('С', '')
    print(sentence)
