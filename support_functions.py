# coding=utf-8
from itertools import chain, izip_longest
import openpyxl as pyxl
import csv
import os
import re


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        if last == '':
            return s[start:]
        else:
            end = s.index(last, start)
            return s[start:end]
    except ValueError:
        return "0000"


def byord(x):
    """Função utilizada para ordenar uma lista de Ranges de Células
    pela soma do valor ASCII das strings encontradas neste range"""
    ascii = 0
    for i in range(len(re.search("[a-zA-Z]+", x).group(0))):
        ascii += ord(x[i])
    return ascii


def bydigit(x):
    """Função utilizada para ordenar uma lista de Ranges de Células
     pelo valor dos INDEXES das linhas"""
    return int(re.search("[-+]?\d+[\.]?\d*", x).group(0))


def remove_duplicate_dicts(data_list):
    seen = set()
    result = []
    data_list = sorted(data_list, key=lambda x: x.get('rows')[0], reverse=True)
    for d in data_list:
        h = d.copy()
        h.pop('rows')
        h = tuple(h.items())
        if h not in seen:
            result.append(d)
            seen.add(h)
    return result


def roundrobin(*iterables):
    sentinel = object()
    return (x for x in chain(*izip_longest(fillvalue=sentinel, *iterables)) if x is not sentinel)


def export_excel_to_csv(file_input):
    base_folder = os.path.abspath(os.getcwd())
    temp_output = 'bsc_lac_rac.csv'
    full_path = os.path.join(base_folder, temp_output)
    wb = pyxl.load_workbook(file_input)
    ws = wb.active
    with open(full_path, 'wb') as fout:
        c = csv.writer(fout)
        for row in ws.rows:
            c.writerow([cell.value for cell in row])
    return full_path


def export_csv_to_dict_list(file_input, key_list):
    list_of_unused_keys = set()
    list_of_dicts = list()
    final_list_of_dicts = list()
    aux_set = set()
    with open(file_input) as fin:
        contents = csv.DictReader(fin)
        for row in contents:
            list_of_dicts.append(row)

    for key in list_of_dicts[0]:
        if key not in key_list:
            list_of_unused_keys.add(key)

    for dicts in list_of_dicts:
        for key in list_of_unused_keys:
            dicts.pop(key, None)

    for dicts in list_of_dicts:
        dicts_copy = dicts.copy()
        dicts_copy = tuple(dicts_copy.items())
        if dicts_copy not in aux_set:
            final_list_of_dicts.append(dicts)
            aux_set.add(dicts_copy)

    os.remove(file_input)
    return final_list_of_dicts
