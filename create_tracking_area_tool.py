# coding=utf-8
import re

import xlsxwriter

from os import getcwd

import huawei_tracking_area_tool as huawei

import f5_tracking_area_tool as f5

from ordered_set import OrderedSet


def create_workbook_tac(workbook_name, tacs_criadas, project_name):
    workbook = xlsxwriter.Workbook(workbook_name)
    worksheet_descricao = workbook.add_worksheet('Descricao')

    worksheet_f5 = workbook.add_worksheet('F5 DNS')

    if len(f5.create_naptrrecord_f5) != 0:
        worksheet_f5.write('A1', 'Utilizar o arquivo com o nome "{name}_entradas_NAPTR.txt." no script '
                                 'cvna_f5_app.py para realizar a config.'.format(name=project_name))

    if len(huawei.create_naptrrecord_mnc02_s10_huawei) != 0:
        worksheet_mnc02_huawei = workbook.add_worksheet('iDNS_Huawei_MNC02')

        worksheet_mnc02_huawei.set_tab_color('green')

        worksheet_mnc02_huawei.write_column('A1', OrderedSet(huawei.create_naptrrecord_mnc02_s11_huawei))
        worksheet_mnc02_huawei.write_column('A' + str(len(OrderedSet(huawei.create_naptrrecord_mnc02_s11_huawei)) + 3),
                                            OrderedSet(huawei.create_naptrrecord_mnc02_s10_huawei))
        worksheet_mnc02_huawei.write('A' + str(
            len(OrderedSet(huawei.create_naptrrecord_mnc02_s11_huawei)) + 3 + len(
                OrderedSet(huawei.create_naptrrecord_mnc02_s10_huawei)) + 2), 'SAV CFG:;')

    if len(huawei.create_tai_lai_manaus) != 0:
        worksheet_manaus_mme_huawei = workbook.add_worksheet('MME MANAUS')

        worksheet_manaus_mme_huawei.set_tab_color('red')

        worksheet_manaus_mme_huawei.write_column('A1', OrderedSet(huawei.create_lai_vlr_manaus))
        worksheet_manaus_mme_huawei.write_column('A' + str(len(OrderedSet(huawei.create_lai_vlr_manaus)) + 3),
                                                 OrderedSet(huawei.create_tai_lai_manaus))

    if len(huawei.create_tai_lai_blm_rce) != 0:
        worksheet_blm_rce_mme_huawei = workbook.add_worksheet('MME BLM e RCE')

        worksheet_blm_rce_mme_huawei.set_tab_color('white')

        worksheet_blm_rce_mme_huawei.write_column('A1', OrderedSet(huawei.create_lai_vlr_blm_rce))
        worksheet_blm_rce_mme_huawei.write_column('A' + str(len(OrderedSet(huawei.create_lai_vlr_blm_rce)) + 3),
                                                  OrderedSet(huawei.create_tai_lai_blm_rce))

    if len(huawei.create_tai_lai_bhe_sdr) != 0:
        worksheet_bhe_sdr_mme_huawei = workbook.add_worksheet('MME BHE e SDR')

        worksheet_bhe_sdr_mme_huawei.set_tab_color('black')

        worksheet_bhe_sdr_mme_huawei.write_column('A1', OrderedSet(huawei.create_lai_vlr_bhe_sdr))
        worksheet_bhe_sdr_mme_huawei.write_column('A' + str(len(OrderedSet(huawei.create_lai_vlr_bhe_sdr)) + 3),
                                                  OrderedSet(huawei.create_tai_lai_bhe_sdr))

    if len(huawei.create_tai_lai_rj) != 0:
        worksheet_rj_mme_huawei = workbook.add_worksheet('MMEs RJ')

        worksheet_rj_mme_huawei.set_tab_color('green')

        worksheet_rj_mme_huawei.write_column('A1', OrderedSet(huawei.create_lai_vlr_rj))
        worksheet_rj_mme_huawei.write_column('A' + str(len(OrderedSet(huawei.create_lai_vlr_rj)) + 3),
                                             OrderedSet(huawei.create_tai_lai_rj))
    if len(huawei.create_tai_lai_mnc03) != 0:
        worksheet_sp_mme_huawei = workbook.add_worksheet('MMEs SP')

        worksheet_sp_mme_huawei.set_tab_color('yellow')

        worksheet_sp_mme_huawei.write_column('A1', OrderedSet(huawei.create_lai_vlr_mnc03))
        worksheet_sp_mme_huawei.write_column('A' + str(len(OrderedSet(huawei.create_lai_vlr_mnc03)) + 3),
                                             OrderedSet(huawei.create_tai_lai_mnc03))

    if len(huawei.create_naptrrecord_mnc03_s10_huawei) != 0:
        worksheet_mnc03_huawei = workbook.add_worksheet('iDNS_Huawei_MNC03')

        worksheet_mnc03_huawei.set_tab_color('yellow')

        worksheet_mnc03_huawei.write_column('A1', OrderedSet(huawei.create_naptrrecord_mnc03_s11_huawei))
        worksheet_mnc03_huawei.write_column('A' + str(len(OrderedSet(huawei.create_naptrrecord_mnc03_s11_huawei)) + 3),
                                            OrderedSet(huawei.create_naptrrecord_mnc03_s10_huawei))
        worksheet_mnc03_huawei.write('A' + str(
            len(OrderedSet(huawei.create_naptrrecord_mnc03_s11_huawei)) + 3 + len(
                OrderedSet(huawei.create_naptrrecord_mnc03_s10_huawei)) + 2), 'SAV CFG:;')

    if len(huawei.create_naptrrecord_mnc04_s10_huawei) != 0:
        worksheet_mnc04_huawei = workbook.add_worksheet('iDNS_Huawei_MNC04')

        worksheet_mnc04_huawei.set_tab_color('blue')

        worksheet_mnc04_huawei.write_column('A1', OrderedSet(huawei.create_naptrrecord_mnc04_s11_huawei))
        worksheet_mnc04_huawei.write_column('A' + str(len(OrderedSet(huawei.create_naptrrecord_mnc04_s11_huawei)) + 3),
                                            OrderedSet(huawei.create_naptrrecord_mnc04_s10_huawei))
        worksheet_mnc04_huawei.write('A' + str(
            len(OrderedSet(huawei.create_naptrrecord_mnc04_s11_huawei)) + 3 + len(
                OrderedSet(huawei.create_naptrrecord_mnc04_s10_huawei)) + 2), 'SAV CFG:;')

    if len(huawei.create_tai_lai_mnc04) != 0:
        worksheet_mnc04_mme_huawei = workbook.add_worksheet('MME BSA e CTA')

        worksheet_mnc04_mme_huawei.set_tab_color('blue')

        worksheet_mnc04_mme_huawei.write_column('A1', OrderedSet(huawei.create_lai_vlr_mnc04))
        worksheet_mnc04_mme_huawei.write_column('A' + str(len(OrderedSet(huawei.create_lai_vlr_mnc04)) + 3),
                                                OrderedSet(huawei.create_tai_lai_mnc04))

    worksheet_descricao.write('A1', u'Este projeto contempla as seguintes TACs: {0:s}'.format(tacs_criadas))
    print('Seu projeto foi criado no diretorio abaixo:')
    print(getcwd() + '\\' + workbook_name + '\n')
    workbook.close()


def main_create_tracking_area_tool():
    pattern = re.compile(r'\s+')

    counter_workbook = 0

    while True:
        lac_list = []
        lac_hex = []
        tac_list = []
        tac_hex = []

        nome_projeto = raw_input('Digite o nome do projeto: ')

        tac_lacs = raw_input(
            'Digite as TACs;LACs a serem criadas (ex: 31258;50912,32456;56024,36389;58063), utilize ponto e virgula ";"'
            ' como separador de TAC;LAC e a virgula como separador das relacoes: ')

        if tac_lacs == 'exit':
            break
        else:
            tac_lacs = re.sub(pattern, '', tac_lacs)

            for values in xrange(len(tac_lacs.split(','))):
                tac_list.append(tac_lacs.split(',')[values].split(';')[0])
                lac_list.append(tac_lacs.split(',')[values].split(';')[1])

            for tacs in tac_list:
                tac_hex.append(format(int(tacs), '04x').upper())

            for lacs in lac_list:
                lac_hex.append(format(int(lacs), '04x').upper())

            # Huawei Function Calls
            # huawei.create_naptrrecord_s11_huawei(tac_list, tac_hex) # DNS Desativado
            # huawei.create_naptrrecord_s10_huawei(tac_list, tac_hex) # DNS Desativado
            huawei.create_tai_lai(lac_list, lac_hex, tac_hex)

            # F5 Function Calls
            f5.create_naptrrecord_s10_f5(tac_list, tac_hex)
            f5.create_naptrrecord_s11_f5(tac_list, tac_hex)
            f5.export_json_f5(nome_projeto)

            nome_workbook = 'Inclusao_TAC_Projeto_{0:s}.xlsx'.format(nome_projeto)

            lista_tacs = ''
            for values in tac_list:
                lista_tacs += u'{0:s}  '.format(values)

            create_workbook_tac(nome_workbook, lista_tacs, nome_projeto)

            counter_workbook += 1

            yes_or_no = raw_input('Voce deseja criar mais projetos de TAC;LAC? (S ou N) : ')
            if yes_or_no.lower() == 's':

                # reload(ericsson)
                reload(huawei)
                reload(f5)

                continue

            elif yes_or_no.lower() == 'n':
                break


if __name__ == '__main__':
    main_create_tracking_area_tool()
