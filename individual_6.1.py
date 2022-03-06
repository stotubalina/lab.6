#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    bucket_list = input("Введите текст: ")
    result = len(bucket_list.split(' '))
    print("В тексте " + str(result) + " слов.")
