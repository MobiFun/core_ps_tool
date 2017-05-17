from support_variables import *
import json

create_naptrrecord_f5 = []


def create_naptrrecord_s11_f5(lista_tac_dec, lista_tac_hex):
    counter_f5 = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] in tac_mnc02:

            for saegw in saegw_rj:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s8-gtp:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name=saegw
                    ),
                    'ttl': 300}
                )

            if TAC[0:2] == '32':
                pass

            elif TAC[0:2] == '33':
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 5,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name='GPBHE1'
                    ),
                    'ttl': 300}
                )

            elif TAC[0:2] == '37':
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 5,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name='GPSDR1'
                    ),
                    'ttl': 300}
                )

            elif TAC[1:3] == '91' or TAC[1:3] == '93' or TAC[1:3] == '94' or TAC[1:3] == '95' or TAC[1:3] == '96' \
                    or TAC[1:3] == '98' or TAC[1:3] == '99':
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 5,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name='GPBLM1'
                    ),
                    'ttl': 300}
                )

            elif TAC[0:2] == '38':
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 5,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name='GPRCE1'
                    ),
                    'ttl': 300}
                )

            elif TAC[1:3] == '92' or TAC[1:3] == '97':
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 5,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name='GPMNS1'
                    ),
                    'ttl': 300}
                )

        elif TAC[0:2] in tac_mnc03:

            for saegw in saegw_sp:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s8-gtp:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        node_name=saegw
                    ),
                    'ttl': 300}
                )

        elif TAC[0:2] in tac_mnc04:
            for saegw in saegw_sp:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s8-gtp:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        node_name=saegw
                    ),
                    'ttl': 300}
                )

            if TAC[0:2] == '36':
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 5,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        node_name='GPBSA1'
                    ),
                    'ttl': 300}
                )
            else:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 5,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                    'regexp': '""',
                    'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        node_name='GPCTA1'
                    ),
                    'ttl': 300}
                )

        counter_f5 += 1


def create_naptrrecord_s10_f5(lista_tac_dec, lista_tac_hex):
    counter_f5 = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] == '33' or TAC[0:2] == '37':
            for mme in ['DMBHE1', 'DMBHE2', 'DMSDR1', 'DMSDR2']:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

        elif TAC[0:2] == '34' or TAC[0:2] == '35' or TAC[0:2] == '36':
            for mme in ['DMBSA1', 'DMBSA2', 'DMCTA1', 'DMCTA2']:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc004.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

        elif TAC[0:3] == '392' or TAC[0:3] == '397':

            create_naptrrecord_f5.append({
                'action': 'add',
                'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                    tac_lb=lista_tac_hex[counter_f5][2:],
                    tac_hb=lista_tac_hex[counter_f5][0:2]
                ),
                'order': 10,
                'preference': 10,
                'flags': 'A',
                'service': 'x-3gpp-mme:x-gn:x-s10',
                'regexp': '""',
                'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                    node_name='DMMNS1'
                ),
                'ttl': 300}
            )

        elif TAC[0:2] == '31':
            for mme in ['DMSNE3', 'DMSNE4', 'DMSPO1', 'DMSPO2']:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc003.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

        elif TAC[0:2] == '32':
            for mme in ['DMRJO3', 'DMRJO4']:
                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

        elif TAC[0:3] == '391' or TAC[0:3] == '393' or TAC[0:3] == '394' or TAC[0:3] == '396' \
                or TAC[0:3] == '398' or TAC[0:3] == '399' or TAC[0:3] == '395' or TAC[0:2] == '38':

            for mme in ['DMRCE1', 'DMRCE2', 'DMBLM1', 'DMBLM2']:

                create_naptrrecord_f5.append({
                    'action': 'add',
                    'domain_name': 'tac-lb{tac_lb}.tac-hb{tac_hb}.tac.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        tac_lb=lista_tac_hex[counter_f5][2:],
                        tac_hb=lista_tac_hex[counter_f5][0:2]
                    ),
                    'order': 10,
                    'preference': 10,
                    'flags': 'A',
                    'service': 'x-3gpp-mme:x-gn:x-s10',
                    'regexp': '""',
                    'replacement': 'topoff.vip-gn.{node_name}.node.epc.mnc002.mcc724.3gppnetwork.org.'.format(
                        node_name=mme
                    ),
                    'ttl': 300}
                )

        counter_f5 += 1


def export_json_f5(project_name):
    if len(create_naptrrecord_f5) != 0:
        with open('{}_entradas_NAPTR.txt'.format(project_name), 'wb') as fout:
            for dicts in create_naptrrecord_f5:
                fout.write(json.dumps(dicts))
                fout.write('\n')
        with open('Fallback_{}_entradas_NAPTR.txt'.format(project_name), 'wb') as fout:
            for dicts in create_naptrrecord_f5:
                dicts['action'] = 'remove'
                fout.write(json.dumps(dicts))
                fout.write('\n')
