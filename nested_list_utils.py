''' 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5] '''

def flatten(input_list):
    l = []
    for i in input_list:
        if isinstance(i, list):
            l.extend(flatten(i))
        else:
            l.append(i)
    return l


'''2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]'''

def deep_reverse (input):
    l = []
    for i in input[::-1]:
        if isinstance(i, list):
            l.append(deep_reverse(i))
        else:
            l.append(i)
    return l
