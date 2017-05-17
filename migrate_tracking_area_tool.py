# coding=utf-8
import re

import xlsxwriter

import json

from os import getcwd

from ordered_set import OrderedSet

from support_variables import add_resrec, rmv_resrec, view_dns, tac_mnc02, tac_mnc03, tac_mnc04

# Variables

create_naptrrecord_mnc02_s10_huawei = []
delete_naptrrecord_mnc02_s10_huawei = []

create_naptrrecord_mnc03_s10_huawei = []
delete_naptrrecord_mnc03_s10_huawei = []

create_naptrrecord_mnc04_s10_huawei = []
delete_naptrrecord_mnc04_s10_huawei = []

create_naptrrecord_mnc02_s10_f5 = []
delete_naptrrecord_mnc02_s10_f5 = []

create_naptrrecord_mnc03_s10_f5 = []
delete_naptrrecord_mnc03_s10_f5 = []

create_naptrrecord_mnc04_s10_f5 = []
delete_naptrrecord_mnc04_s10_f5 = []


def create_workbook_tac(workbook_name, tacs_migradas, mme_atual, mme_futuro):
    workbook = xlsxwriter.Workbook(workbook_name)
    worksheet_descricao = workbook.add_worksheet('Descricao')

    if len(create_naptrrecord_mnc02_s10_huawei) != 0:
        worksheet_mnc02_huawei = workbook.add_worksheet('iDNS_Huawei_MNC02')

        worksheet_mnc02_huawei.set_tab_color('green')

        worksheet_mnc02_huawei.write_column('A1', OrderedSet(delete_naptrrecord_mnc02_s10_huawei))

        worksheet_mnc02_huawei.write_column('A{}'.format(str(len(OrderedSet(delete_naptrrecord_mnc02_s10_huawei)) + 3)),
                                            OrderedSet(create_naptrrecord_mnc02_s10_huawei)
                                            )

        worksheet_mnc02_huawei.write('A{}'.format(str(len(OrderedSet(delete_naptrrecord_mnc02_s10_huawei)) +
                                                      len(OrderedSet(create_naptrrecord_mnc02_s10_huawei)) + 5)),
                                     'SAV CFG:;')

    if len(create_naptrrecord_mnc03_s10_huawei) != 0:
        worksheet_mnc03_huawei = workbook.add_worksheet('iDNS_Huawei_MNC03')

        worksheet_mnc03_huawei.set_tab_color('yellow')

        worksheet_mnc03_huawei.write_column('A1', OrderedSet(delete_naptrrecord_mnc03_s10_huawei))

        worksheet_mnc03_huawei.write_column('A{}'.format(str(len(OrderedSet(delete_naptrrecord_mnc03_s10_huawei)) + 3)),
                                            OrderedSet(create_naptrrecord_mnc03_s10_huawei)
                                            )

        worksheet_mnc03_huawei.write('A{}'.format(str(len(OrderedSet(delete_naptrrecord_mnc03_s10_huawei)) +
                                                      len(OrderedSet(create_naptrrecord_mnc03_s10_huawei)) + 5)),
                                     'SAV CFG:;')

    if len(create_naptrrecord_mnc04_s10_huawei) != 0:
        worksheet_mnc04_huawei = workbook.add_worksheet('iDNS_Huawei_MNC04')

        worksheet_mnc04_huawei.set_tab_color('blue')

        worksheet_mnc04_huawei.write_column('A1', OrderedSet(delete_naptrrecord_mnc04_s10_huawei))

        worksheet_mnc04_huawei.write_column('A{}'.format(str(len(OrderedSet(delete_naptrrecord_mnc04_s10_huawei)) + 3)),
                                            OrderedSet(create_naptrrecord_mnc04_s10_huawei)
                                            )

        worksheet_mnc04_huawei.write('A{}'.format(str(len(OrderedSet(delete_naptrrecord_mnc04_s10_huawei)) +
                                                      len(OrderedSet(create_naptrrecord_mnc04_s10_huawei)) + 5)),
                                     'SAV CFG:;')

    worksheet_descricao.write('A1', u'Este projeto contempla as seguintes TACs: {0:s}'.format(tacs_migradas))
    worksheet_descricao.write('A2', 'O projeto visa remover o apontamento da interface s10 do(s) MME(s) {} e '
                                    'adicionar o apontamento para o(s) '
                                    'MME(s) {}'.format(mme_atual, mme_futuro))

    print('Seu projeto foi criado no diretorio abaixo:')
    print(getcwd() + '\\' + workbook_name + '\n')
    workbook.close()


def naptrrecord_s10_huawei(lista_tac_dec, lista_tac_hex, lista_mme_atual, lista_mme_novo):
    counter_huawei = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] in tac_mnc02:
            for views in view_dns:
                for mme in lista_mme_novo:
                    create_naptrrecord_mnc02_s10_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name=mme,
                                          view_name=views)
                    )

                for mme in lista_mme_atual:
                    delete_naptrrecord_mnc02_s10_huawei.append(
                        rmv_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-mme:x-s10', interface='s10', node_name=mme,
                                          view_name=views)
                    )
        if TAC[0:2] in tac_mnc03:
            for views in view_dns:
                for mme in lista_mme_novo:
                    create_naptrrecord_mnc03_s10_huawei.append(
                        add_resrec.format(mnc='003', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name=mme,
                                          view_name=views)
                    )

                for mme in lista_mme_atual:
                    delete_naptrrecord_mnc03_s10_huawei.append(
                        rmv_resrec.format(mnc='003', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-mme:x-s10', interface='s10', node_name=mme,
                                          view_name=views)
                    )
        if TAC[0:2] in tac_mnc04:
            for views in view_dns:
                for mme in lista_mme_novo:
                    create_naptrrecord_mnc04_s10_huawei.append(
                        add_resrec.format(mnc='004', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name=mme,
                                          view_name=views)
                    )

                for mme in lista_mme_atual:
                    delete_naptrrecord_mnc04_s10_huawei.append(
                        rmv_resrec.format(mnc='004', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-mme:x-s10', interface='s10', node_name=mme,
                                          view_name=views)
                    )

        counter_huawei += 1


def naptrrecord_s10_f5(lista_tac_dec, lista_tac_hex, lista_mme_atual, lista_mme_novo):
    counter_f5 = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] in tac_mnc02:
            for mme in lista_mme_novo:
                create_naptrrecord_mnc02_s10_f5.append({
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'a',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

            for mme in lista_mme_atual:
                delete_naptrrecord_mnc02_s10_f5.append({
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'a',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )
        if TAC[0:2] in tac_mnc03:
            for mme in lista_mme_novo:
                create_naptrrecord_mnc03_s10_f5.append({
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'a',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

            for mme in lista_mme_atual:
                delete_naptrrecord_mnc03_s10_f5.append({
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'a',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )
        if TAC[0:2] in tac_mnc04:
            for mme in lista_mme_novo:
                create_naptrrecord_mnc04_s10_f5.append({
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'a',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

            for mme in lista_mme_atual:
                delete_naptrrecord_mnc04_s10_f5.append({
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'a',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

        counter_f5 += 1


def export_json_f5(project_name):
    if len(create_naptrrecord_mnc02_s10_f5) != 0:
        with open('{}_entradas_NAPTR_mnc02.txt'.format(project_name), 'wb') as mnc02:
            for dicts in create_naptrrecord_mnc02_s10_f5:
                mnc02.write(json.dumps(dicts))
                mnc02.write('\n')
        with open('{}_entradas_NAPTR_mnc02_delete.txt'.format(project_name), 'wb') as mnc02:
            for dicts in delete_naptrrecord_mnc02_s10_f5:
                mnc02.write(json.dumps(dicts))
                mnc02.write('\n')
    if len(create_naptrrecord_mnc03_s10_f5) != 0:
        with open('{}_entradas_NAPTR_mnc03.txt'.format(project_name), 'wb') as mnc03:
            for dicts in create_naptrrecord_mnc03_s10_f5:
                mnc03.write(json.dumps(dicts))
                mnc03.write('\n')
        with open('{}_entradas_NAPTR_mnc03_delete.txt'.format(project_name), 'wb') as mnc03:
            for dicts in delete_naptrrecord_mnc03_s10_f5:
                mnc03.write(json.dumps(dicts))
                mnc03.write('\n')
    if len(create_naptrrecord_mnc04_s10_f5) != 0:
        with open('{}_entradas_NAPTR_mnc04.txt'.format(project_name), 'wb') as mnc04:
            for dicts in create_naptrrecord_mnc04_s10_f5:
                mnc04.write(json.dumps(dicts))
                mnc04.write('\n')
        with open('{}_entradas_NAPTR_mnc04_delete.txt'.format(project_name), 'wb') as mnc04:
            for dicts in delete_naptrrecord_mnc04_s10_f5:
                mnc04.write(json.dumps(dicts))
                mnc04.write('\n')


def main_create_tracking_area_tool():
    global create_naptrrecord_mnc02_s10_huawei
    global delete_naptrrecord_mnc02_s10_huawei

    global create_naptrrecord_mnc03_s10_huawei
    global delete_naptrrecord_mnc03_s10_huawei

    global create_naptrrecord_mnc04_s10_huawei
    global delete_naptrrecord_mnc04_s10_huawei

    global create_naptrrecord_mnc02_s10_f5
    global delete_naptrrecord_mnc02_s10_f5

    global create_naptrrecord_mnc03_s10_f5
    global delete_naptrrecord_mnc03_s10_f5

    global create_naptrrecord_mnc04_s10_f5
    global delete_naptrrecord_mnc04_s10_f5

    pattern = re.compile(r'\s+')

    counter_workbook = 0

    while True:

        tac_hex = []

        nome_projeto = raw_input('Digite o nome do projeto: ')

        tacs = raw_input(
            'Digite as TACs a serem migradas (ex: 31258,32456,36389), utilize a virgula como separador das TACs: ')

        mme_atual = raw_input(
            'Digite o(s) nome(s) do(s) MME(s) a(os) qual(is) a TAC pertence, separando por virgula (DMRJO2,DMSNE2): ')

        mme_novo = raw_input(
            'Digite o(s) nome(s) do(s) MME(s) para o(s) qual(is) a TAC sera migrada, separando por virgula '
            '(DMRJO3,DMRJO4): '
        )

        if tacs == 'exit':
            break
        else:
            tacs = re.sub(pattern, '', tacs)

            tac_list = tacs.split(',')

            for tacs in tac_list:
                tac_hex.append(format(int(tacs), '04x').upper())

            mme_novo = mme_novo.upper()

            mme_novo = re.sub(pattern, '', mme_novo)

            lista_mme_novo = mme_novo.split(',')

            mme_atual = mme_atual.upper()

            mme_atual = re.sub(pattern, '', mme_atual)

            lista_mme_atual = mme_atual.split(',')

            nome_workbook = 'Inclusao_TAC_Projeto_{0:s}.xlsx'.format(nome_projeto)

            naptrrecord_s10_huawei(tac_list, tac_hex, lista_mme_atual, lista_mme_novo)
            naptrrecord_s10_f5(tac_list, tac_hex, lista_mme_atual, lista_mme_novo)
            export_json_f5(nome_projeto)

            lista_tacs = ''
            for values in tac_list:
                lista_tacs += u'{0:s}  '.format(values)

            create_workbook_tac(nome_workbook, lista_tacs, mme_atual, mme_novo)

            counter_workbook += 1

            yes_or_no = raw_input('Voce deseja criar mais projetos de TAC? (S ou N) : ')
            if yes_or_no == 'S' or yes_or_no == 's':
                create_naptrrecord_mnc02_s10_huawei = []
                delete_naptrrecord_mnc02_s10_huawei = []

                create_naptrrecord_mnc03_s10_huawei = []
                delete_naptrrecord_mnc03_s10_huawei = []

                create_naptrrecord_mnc04_s10_huawei = []
                delete_naptrrecord_mnc04_s10_huawei = []

                create_naptrrecord_mnc02_s10_f5 = []
                delete_naptrrecord_mnc02_s10_f5 = []

                create_naptrrecord_mnc03_s10_f5 = []
                delete_naptrrecord_mnc03_s10_f5 = []

                create_naptrrecord_mnc04_s10_f5 = []
                delete_naptrrecord_mnc04_s10_f5 = []

                continue

            elif yes_or_no == 'N' or yes_or_no == 'n':
                break


if __name__ == '__main__':
    main_create_tracking_area_tool()
