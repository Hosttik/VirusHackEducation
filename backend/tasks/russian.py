import os
import pickle
import utils as ut
import random

ACCENTS = []

if os.path.exists('data/accents.pkl'):
    with open('data/accents.pkl', 'rb') as f:
        ACCENTS = pickle.load(f)

letters = 'аеёиоуэюя'
allletters = 'абвгдеёжзиёклмнопрстуфхцчшщьъыэюя'
allletters = allletters + allletters.upper()

def get_sample(vocab,pt):
    p = random.random()
    k_list = list(vocab.keys())
    if p>pt:
        key = random.choice(k_list)
        sample = ', '.join(random.sample(vocab[key], k=3))
        target = True
    else:
        k1 = random.choice([0,1])
        key1 = k_list[k1]
        key2 = k_list[1-k1]
        sample = random.sample(vocab[key1], k=2) + random.sample(vocab[key2],k=1)
        random.shuffle(sample)
        sample = ', '.join(sample)
        target = False
    return (sample, target)



def task2():
    text = '<i>(1)Чтобы защитить окружающую среду и исключить поступление газовых выбросов производства ' \
           'в атмосферу, на пути газового потока устанавливают специальные фильтры. (2)В качестве фильтрующего' \
           ' материала хорошо зарекомендовали себя ткани из тонковолокнистых полимеров на марлевой основе: ' \
           'они устойчивы к воздействию кислот, щелочей, высокой температуры и органических растворителей. ' \
           '(3)Основной недостаток <…> фильтров – низкая пылеёмкость, поэтому на производствах, где содержание' \
           ' пыли в газовых выбросах превышает допустимую норму, дополнительно устанавливают фильтры грубой очистки' \
           ' с волокнистыми насадками.</i><br><br>' \
           'Самостоятельно подберите указательное местоимение, которое должно стоять на месте пропуска в третьем (3)' \
           ' предложении текста. Запишите это местоимение.'
    answer = 'таких'
    return {'text': text, 'answer': answer, 'image': None}

def task4():
    if len(ACCENTS) > 0:
        words = []
        for _ in range(5):
            word = None
            while (word is None) or (word in words) or (len(word) < 6):
                index = ut.get_random_int(0, len(ACCENTS) - 1)
                word = ACCENTS[index]
            words.append(word)

        index = ut.get_random_int(0, 4)
        error_word = words[index]

        new_word = []
        flag = True
        for sym in error_word:
            if (sym in letters) and sym.islower() and flag:
                flag = False
                new_word.append(sym.upper())
            else:
                new_word.append(sym.lower())
        new_word = ''.join(new_word)

        words[index] = new_word
        words = [w.strip() for w in words]

        filtered_words = []
        for w in words:
            neww = [c for c in w if c in allletters]
            filtered_words.append(''.join(neww))
        words = filtered_words
    else:
        index = 3
        words = ['позвонИшь', 'красИвее', 'озлОбить', 'прибЫло', 'тОрты']

    text = 'В одном из приведённых ниже слов допущена ошибка в постановке ударения: НЕВЕРНО выделена буква, ' \
           'обозначающая ударный гласный звук. Выпишите это слово.<br><br>{}<br>{}<br>{}<br>{}<br>{}'.format(*words)
    answer = words[index].lower()
    return {'text': text, 'answer': answer, 'image': None}

def task6():
    text = 'Отредактируйте предложение: исправьте лексическую ошибку, исключив лишнее слово. Выпишите это слово. <br><br>' \
           '<i>В этом пейзаже не было ни одной кричащей краски, ни одной острой черты в рельефе, но его скупые ' \
           'озёрца, наполненные тёмной и спокойной водой, кажется, выражали главную суть воды больше, чем все моря и' \
           ' океаны.</i>'
    answer = 'главную'
    return {'text': text, 'answer': answer, 'image': None}

def task15():
    vocab = {'н':['багр..ый', 'лебеди..ый', 'кожа..ый', 'шерстя..ой', 'мыши..ый',
              'серебря..ый', 'песча..ый', 'ветре..ый (юноша)', 'еди..ый', 'сви..ой',
              'ю..ый', 'румя..ый', 'пря..ый', 'зеле..ый','гуси..ый'],
         'нн':['стекля..ый', 'оловя..ый', 'деревя..ый', 'традицио..ый', 'клюкве..ый',
               'соломе..ый', 'искусстве..ый', 'безветре..ая', 'дли..ый', 'исти..ый',
               'инфекцио..ый', 'дикови..ый', 'телефо..ый', 'тума..ый']}

    answer = []

    text = 'Укажите строки, во всех словах которых пропущено одно и то же количество букв "н".<br> '

    for i in range(1,6):
        sample, target = get_sample(vocab,pt=0.3)
        text += '<br>' + str(i)+") "+sample + '\n '
        if target:
            answer.append(i)

    return {'text': text, 'answer': answer, 'image': None}