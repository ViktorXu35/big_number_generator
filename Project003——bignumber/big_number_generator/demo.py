"""
Автор: Виктор Сюй © 2021
Автор имеет все права на использование, распространение, адаптацию, и т. п., касающиеся данной программы.
Почта для обратной связи: viktor.p.xu@yandex.ru
"""

import random
from itertools import chain
import tkinter as tk


def generator():
    n = random.choices([p for p in range(10)], k=random.randint(4, 13))
    nu = ''
    for i in n:
        nu += str(i)
    return int(nu)


# convert it to russian
class Russian:
    def __init__(self, o):
        self.dic1 = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
                     9: 'девять'}
        self.dic2 = {10: 'десять', 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
                     15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: 'девятнадцать',
                     20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
                     80: 'восемьдесят', 90: 'девяносто'}
        self.dic3 = {1: "сто", 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот',
                     8: 'восемьсот', 9: 'девятьсот'}
        self.dic4_1 = {1: 'тысяча', 2: 'миллион', 3: 'миллиард', 4: 'триллион'}
        self.dic4_2 = {1: 'тысячи', 2: 'миллиона', 3: 'миллиарда', 4: 'триллиона'}
        self.dic4_3 = {1: 'тысяч', 2: 'миллионов', 3: 'миллиардов', 4: 'триллионов'}
        self.o = o

    def _read_three(self, str_n):
        hun = int(str_n[0])
        rest = int(str_n[1:3])
        if self.dic2.get(rest) is not None:
            return (self.dic3.get(hun, '') + ' ' + self.dic2.get(rest, '')).lstrip(' ').replace('  ', ' ')
        else:
            temp = str(rest).rjust(2, '0')
            rest1 = int(temp[0]) * 10
            rest2 = int(temp[1])
            return (self.dic3.get(hun, '') + ' ' + self.dic2.get(rest1, '') + ' ' + self.dic1.get(rest2, '')) \
                .lstrip(' ').replace('  ', ' ')

    def _gender(self, str_tho):
        li = str_tho.split(' ')
        if li[-1] == 'один':
            li[-1] = 'одна'
        elif li[-1] == 'два':
            li[-1] = 'две'
        return ' '.join(li)

    def _case(self, str_three):
        li = str_three.split(' ')
        case1 = ['один', "одна"]
        case2 = ['два', "две", "три", "четыре"]
        if li[-1] in case1:
            return self.dic4_1
        elif li[-1] in case2:
            return self.dic4_2
        else:
            return self.dic4_3

    def run(self):
        li = [i.rjust(3, '0') for i in format(self.o, ',').split(',')]
        ls = []
        un = []
        for k in li:
            ls.append(self._read_three(k))
        if len(li) == 1:
            return ' '.join(ls)
        elif len(li) >= 2:
            ls[-2] = self._gender(ls[-2])
            for i, item in enumerate(ls):
                un.append(self._case(item).get(len(li) - 1 - i, ''))
            return ' '.join(list(chain.from_iterable(zip(ls, un))))


class Chinese:
    def __init__(self, o):
        self.dic1 = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 0: '零'}
        self.dic2 = {1: "万", 2: '亿', 3: '兆'}
        self.o = o

    def _str_split(self, o):
        s = str(o)
        li = list(s)
        leng = int(len(li) / 4)
        result = []
        for i in range(leng):
            temp = []
            for q in range(4):
                temp.append(li.pop())
            result.append(''.join(temp[::-1]).rjust(4, '0'))
        if any(li):
            result.append(''.join(li).rjust(4, '0'))
        return result[::-1]

    def _read_four(self, str_four):
        d1, d2, d3, d4 = str_four
        # n_r = str(int(str_four))
        r = self.dic1.get(int(d1), '') + '千' + self.dic1.get(int(d2), '') + '百' + self.dic1.get(int(d3), '') \
            + '十' + self.dic1.get(int(d4), '')
        no_list = ['零千', '零百', '零十', '零零', '零零']
        for i in no_list:
            r = r.replace(i, '零')
        return r.rstrip('零').replace('二千','两千').replace('二百','两百')

    def run(self):
        li = self._str_split(str(self.o))
        ls = []
        un = []
        for i in li:
            ls.append(self._read_four(i))
        for k in range(len(li)):
            un.append(self.dic2.get(len(li) - 1 - k, ''))
        return ''.join(list(chain.from_iterable(zip(ls, un)))).lstrip('零')


class Show:
    def __init__(self):
        self.num = 0

    def update(self):
        self.num = generator()
        label_r = tk.Label(win, text=' '*30000 + '\n' + ' '*30000, font=('Times New Roman', 15), wraplength=700)
        label_c = tk.Label(win, text=' '*30000 + '\n' + ' '*30000, font=('Times New Roman', 15), wraplength=700)
        label_r.place(relx=0.5, rely=0.45, anchor='center')
        label_c.place(relx=0.5, rely=0.55, anchor='center')

    def show_number(self):
        r = tk.StringVar()
        r.set(format(self.num, ','))
        label_n = tk.Label(win, textvariable=r, font=('', 40), bg=win.cget('bg'), width=width, anchor='center')
        label_n.place(relx=0.5, rely=0.3, anchor='center')


    def show_russian(self):
        r_r = tk.StringVar()
        count_r = int(str(r_r).replace('PY_VAR', ''))
        label_r = tk.Label(win, text='', font=('Times New Roman', 15), wraplength=700)
        if int(count_r / 2) == count_r / 2:
            label_r['text'] = Russian(self.num).run()
        else:
            label_r['text'] = Russian(self.num).run() + '\n' + Russian(self.num).run()
            label_r['fg'] = win.cget('bg')
        label_r.place(relx=0.5, rely=0.45, anchor='center')

    def show_chinese(self):
        c_r = tk.StringVar()
        count_c = int(str(c_r).replace('PY_VAR', ''))
        label_c = tk.Label(win, text='', font=('Times New Roman', 15), wraplength=700)
        if int(count_c / 2) == count_c / 2:
            label_c['text'] = Chinese(self.num).run()
        else:
            label_c['text'] = Chinese(self.num).run()
            label_c['fg'] = win.cget('bg')
        label_c.place(relx=0.5, rely=0.55, anchor='center')


if __name__ == '__main__':
    win = tk.Tk()
    win.title('Big Number Generator')
    width = 800
    height = 600
    win.geometry(f'{width}x{height}')
    label0 = tk.Label(win, text="Big Number Generator", font=('Times New Roman', 30))
    label0.place(relx=0.5, rely=0.15, anchor='center')
    label1 = tk.Label(win, text="Автор: Виктор Сюй © 2021\nАвтор имеет все права на использование, распространение, "
                                "адаптацию, и т. п., касающиеся данной программы.\nПочта для обратной связи: "
                                "viktor.p.xu@yandex.ru")
    label1.place(relx=0.5, rely=0.9, anchor='center')
    show = Show()
    button0 = tk.Button(win, text='Generate', command=lambda: [show.update(), show.show_number()])
    button0.place(relx=0.5, rely=0.7, anchor='center')
    button_r = tk.Button(win, text='Русский', command=lambda: show.show_russian())
    button_r.place(relx=0.3, rely=0.7, anchor='center')
    button_c = tk.Button(win, text='中文', command=lambda: show.show_chinese())
    button_c.place(relx=0.7, rely=0.7, anchor='center')
    win.mainloop()
