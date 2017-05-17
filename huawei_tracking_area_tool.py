from support_variables import *

# MNC02 Variables
delete_tac_naptrrecord_mnc02_huawei = []
create_naptrrecord_mnc02_s11_huawei = []
create_naptrrecord_mnc02_s10_huawei = []

create_lai_vlr_manaus = []
create_tai_lai_manaus = []

create_lai_vlr_bhe_sdr = []
create_tai_lai_bhe_sdr = []

create_lai_vlr_blm_rce = []
create_tai_lai_blm_rce = []

create_lai_vlr_rj = []
create_tai_lai_rj = []

# MNC03 Variables
delete_tac_naptrrecord_mnc03_huawei = []
create_naptrrecord_mnc03_s11_huawei = []
create_naptrrecord_mnc03_s10_huawei = []

create_lai_vlr_mnc03 = []
create_tai_lai_mnc03 = []

# MNC04 Variables
delete_tac_naptrrecord_mnc04_huawei = []
create_naptrrecord_mnc04_s11_huawei = []
create_naptrrecord_mnc04_s10_huawei = []

create_lai_vlr_mnc04 = []
create_tai_lai_mnc04 = []


def create_tai_lai(lista_lac_dec, lista_lac_hex, lista_tac_hex):
    counter_huawei = 0
    for LAC in lista_lac_dec:
        if LAC[-2:] == '92' or LAC[-2:] == '97':

            create_lai_vlr_manaus.append('ADD LAIVLR: BGNLAI="72402%s", ENDLAI="72402%s", VLRNO="%s";' % (
                lista_lac_hex[counter_huawei], lista_lac_hex[counter_huawei],
                lai_vlr.get(vlr_anf.get(LAC[-2:]))))
            create_tai_lai_manaus.append(
                'ADD TAILAI: BGNTAI="72402%s", ENDTAI="72402%s", SUBRANGE=ALL_USER, LAI="72402%s";' % (
                    lista_tac_hex[counter_huawei], lista_tac_hex[counter_huawei],
                    lista_lac_hex[counter_huawei]))

        elif LAC[-2] == '4' or LAC[-2] == '5' or LAC[-2] == '6':

            create_lai_vlr_mnc04.append('ADD LAIVLR: BGNLAI="72404%s", ENDLAI="72404%s", VLRNO="%s";' % (
                lista_lac_hex[counter_huawei], lista_lac_hex[counter_huawei],
                lai_vlr.get(vlr_anf.get(LAC[-2:]))))
            create_tai_lai_mnc04.append(
                'ADD TAILAI: BGNTAI="72404%s", ENDTAI="72404%s", SUBRANGE=ALL_USER, LAI="72404%s";' % (
                    lista_tac_hex[counter_huawei], lista_tac_hex[counter_huawei],
                    lista_lac_hex[counter_huawei]))

        elif LAC[-2] == '3' or LAC[-2] == '7':

            create_lai_vlr_bhe_sdr.append('ADD LAIVLR: BGNLAI="72402%s", ENDLAI="72402%s", VLRNO="%s";' % (
                lista_lac_hex[counter_huawei], lista_lac_hex[counter_huawei],
                lai_vlr.get(vlr_anf.get(LAC[-2:]))))
            create_tai_lai_bhe_sdr.append(
                'ADD TAILAI: BGNTAI="72402%s", ENDTAI="72402%s", SUBRANGE=ALL_USER, LAI="72402%s";' % (
                    lista_tac_hex[counter_huawei], lista_tac_hex[counter_huawei],
                    lista_lac_hex[counter_huawei]))

        elif LAC[-2] == '2':

            create_lai_vlr_rj.append('ADD LAIVLR: BGNLAI="72402%s", ENDLAI="72402%s", VLRNO="%s";' % (
                lista_lac_hex[counter_huawei], lista_lac_hex[counter_huawei],
                lai_vlr.get(vlr_anf.get(LAC[-2:]))))
            create_tai_lai_rj.append(
                'ADD TAILAI: BGNTAI="72402%s", ENDTAI="72402%s", SUBRANGE=ALL_USER, LAI="72402%s";' % (
                    lista_tac_hex[counter_huawei], lista_tac_hex[counter_huawei],
                    lista_lac_hex[counter_huawei]))

        elif LAC[-2] == '1':

            create_lai_vlr_mnc03.append('ADD LAIVLR: BGNLAI="72403%s", ENDLAI="72403%s", VLRNO="%s";' % (
                lista_lac_hex[counter_huawei], lista_lac_hex[counter_huawei],
                lai_vlr.get(vlr_anf.get(LAC[-2:]))))
            create_tai_lai_mnc03.append(
                'ADD TAILAI: BGNTAI="72403%s", ENDTAI="72403%s", SUBRANGE=ALL_USER, LAI="72403%s";' % (
                    lista_tac_hex[counter_huawei], lista_tac_hex[counter_huawei],
                    lista_lac_hex[counter_huawei]))

        else:

            create_lai_vlr_blm_rce.append('ADD LAIVLR: BGNLAI="72402%s", ENDLAI="72402%s", VLRNO="%s";' % (
                lista_lac_hex[counter_huawei], lista_lac_hex[counter_huawei],
                lai_vlr.get(vlr_anf.get(LAC[-2:]))))
            create_tai_lai_blm_rce.append(
                'ADD TAILAI: BGNTAI="72402%s", ENDTAI="72402%s", SUBRANGE=ALL_USER, LAI="72402%s";' % (
                    lista_tac_hex[counter_huawei], lista_tac_hex[counter_huawei],
                    lista_lac_hex[counter_huawei]))

        counter_huawei += 1


def create_naptrrecord_s10_huawei(lista_tac_dec, lista_tac_hex):
    counter_huawei = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] == '33' or TAC[0:2] == '37':
            for views in view_dns:
                create_naptrrecord_mnc02_s10_huawei.append(
                    add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMBHE1',
                                      view_name=views)
                )
                create_naptrrecord_mnc02_s10_huawei.append(
                    add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMSDR1',
                                      view_name=views)
                )

        elif TAC[0:2] == '34' or TAC[0:2] == '35' or TAC[0:2] == '36':
            for views in view_dns:
                create_naptrrecord_mnc04_s10_huawei.append(
                    add_resrec.format(mnc='004', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMBSA1',
                                      view_name=views)
                )
                create_naptrrecord_mnc04_s10_huawei.append(
                    add_resrec.format(mnc='004', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMCTA1',
                                      view_name=views)
                )

        elif TAC[0:3] == '392' or TAC[0:3] == '397':
            for views in view_dns:
                create_naptrrecord_mnc02_s10_huawei.append(
                    add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMMNS1',
                                      view_name=views)
                )

        elif TAC[0:3] == '311' or TAC[0:3] == '312' or TAC[0:3] == '316' or TAC[0:3] == '317' or TAC[0:3] == '318':
            for views in view_dns:
                create_naptrrecord_mnc03_s10_huawei.append(
                    add_resrec.format(mnc='003', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMSNE3',
                                      view_name=views)
                )
                create_naptrrecord_mnc03_s10_huawei.append(
                    add_resrec.format(mnc='003', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMSNE4',
                                      view_name=views)
                )
                create_naptrrecord_mnc03_s10_huawei.append(
                    add_resrec.format(mnc='003', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMSPO1',
                                      view_name=views)
                )

                create_naptrrecord_mnc03_s10_huawei.append(
                    add_resrec.format(mnc='003', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMSPO2',
                                      view_name=views)
                )

        elif TAC[0:2] == '32':
            for views in view_dns:
                create_naptrrecord_mnc02_s10_huawei.append(
                    add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMRJO3',
                                      view_name=views)
                )

                create_naptrrecord_mnc02_s10_huawei.append(
                    add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                      tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                      service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name='DMRJO4',
                                      view_name=views)
                )

        elif TAC[0:3] == '391' or TAC[0:3] == '393' or TAC[0:3] == '394' or TAC[0:3] == '396' \
                or TAC[0:3] == '398' or TAC[0:3] == '399' or TAC[0:3] == '395' or TAC[0:2] == '38':
            for views in view_dns:
                for mme in ['DMRCE1', 'DMRCE2', 'DMBLM1', 'DMBLM2']:
                    create_naptrrecord_mnc02_s10_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-mme:x-gn:x-s10', interface='gn', node_name=mme,
                                          view_name=views)
                    )

        counter_huawei += 1


def create_naptrrecord_s11_huawei(lista_tac_dec, lista_tac_hex):
    counter_huawei = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] in tac_mnc02:

            for views in view_dns:

                for saegw in saegw_rj:
                    create_naptrrecord_mnc02_s11_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-sgw:x-s11:x-s8-gtp:x-s5-gtp', interface='s11',
                                          node_name=saegw, view_name=views)
                    )

            if TAC[0:2] == '32':
                pass

            elif TAC[0:2] == '33':
                for views in view_dns:
                    create_naptrrecord_mnc02_s11_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='5',
                                          service='x-3gpp-sgw:x-s11:x-s5-gtp', interface='s11', node_name='GPBHE1',
                                          view_name=views)
                    )

            elif TAC[0:2] == '37':
                for views in view_dns:
                    create_naptrrecord_mnc02_s11_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='5',
                                          service='x-3gpp-sgw:x-s11:x-s5-gtp', interface='s11', node_name='GPSDR1',
                                          view_name=views)
                    )

            elif TAC[1:3] == '91' or TAC[1:3] == '93' or TAC[1:3] == '94' or TAC[1:3] == '95' or TAC[1:3] == '96' \
                    or TAC[1:3] == '98' or TAC[1:3] == '99':
                for views in view_dns:
                    create_naptrrecord_mnc02_s11_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='5',
                                          service='x-3gpp-sgw:x-s11:x-s5-gtp', interface='s11', node_name='GPBLM1',
                                          view_name=views)
                    )

            elif TAC[0:2] == '38':
                for views in view_dns:
                    create_naptrrecord_mnc02_s11_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='5',
                                          service='x-3gpp-sgw:x-s11:x-s5-gtp', interface='s11', node_name='GPRCE1',
                                          view_name=views)
                    )

            elif TAC[1:3] == '92' or TAC[1:3] == '97':
                for views in view_dns:
                    create_naptrrecord_mnc02_s11_huawei.append(
                        add_resrec.format(mnc='002', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='5',
                                          service='x-3gpp-sgw:x-s11:x-s5-gtp', interface='s11',
                                          node_name='GPMNS1', view_name=views)
                    )

        elif TAC[0:2] in tac_mnc03:
            for views in view_dns:
                for saegw in saegw_sp:
                    create_naptrrecord_mnc03_s11_huawei.append(
                        add_resrec.format(mnc='003', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-sgw:x-s11:x-s8-gtp:x-s5-gtp', interface='s11', node_name=saegw,
                                          view_name=views)
                    )


        elif TAC[0:2] in tac_mnc04:
            for views in view_dns:
                for saegw in saegw_sp:
                    create_naptrrecord_mnc04_s11_huawei.append(
                        add_resrec.format(mnc='004', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='10',
                                          service='x-3gpp-sgw:x-s11:x-s8-gtp:x-s5-gtp', interface='s11',
                                          node_name=saegw, view_name=views)
                    )

            if TAC[0:2] == '36':
                for views in view_dns:
                    create_naptrrecord_mnc04_s11_huawei.append(
                        add_resrec.format(mnc='004', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='5',
                                          service='x-3gpp-sgw:x-s11:x-s5-gtp', interface='s11', node_name='GPBSA1',
                                          view_name=views)
                    )

            else:
                for views in view_dns:
                    create_naptrrecord_mnc04_s11_huawei.append(
                        add_resrec.format(mnc='004', tac_lb=lista_tac_hex[counter_huawei][2:],
                                          tac_hb=lista_tac_hex[counter_huawei][0:2], order='5',
                                          service='x-3gpp-sgw:x-s11:x-s5-gtp', interface='s11', node_name='GPCTA1',
                                          view_name=views)
                    )

        counter_huawei += 1
