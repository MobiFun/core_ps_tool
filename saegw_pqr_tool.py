from support_variables import view_dns, add_apn_resrec_a_s5s8, add_apn_resrec_naptr_s5s8, add_node_resrec_a, \
    add_node_resrec_naptr_s11

from os import getcwd, mkdir, path
from re import compile, sub
import json
import datetime
import remove_sae_gw

# Huawei Variables

create_arecord_s11 = []
create_arecord_s5s8 = []
create_apn_arecord_s5 = []
create_naptrrecord_apn_timbrasil = []
create_naptrrecord_apn = []
create_naptrrecord_node = []

# F5 Variables

create_arecords_f5 = []
create_naptrrecord_f5 = []

# TIM MNC LIST

mnc_list = ["002", "003", "004"]


def apn_naptrrecord_s5s8(views, apn, node):
    global create_naptrrecord_apn_timbrasil
    global create_naptrrecord_apn

    for mnc in mnc_list:
        for replacement_mnc in mnc_list:
            if apn == "timbrasil.br":
                create_naptrrecord_apn_timbrasil.append(
                    add_apn_resrec_naptr_s5s8.format(mnc=mnc, apn=apn, node_name=node,
                                                     replacement_mnc=replacement_mnc,
                                                     view_name=views)
                )
            else:
                create_naptrrecord_apn.append(add_apn_resrec_naptr_s5s8.format(mnc=mnc, apn=apn, node_name=node,
                                                                               replacement_mnc=replacement_mnc,
                                                                               view_name=views)
                                              )


def apn_naptrrecord_s5s8_f5(apn, node):
    global create_naptrrecord_f5

    for mnc in mnc_list:
        for replacement_mnc in mnc_list:
            create_naptrrecord_f5.append({
                'domain_name': '{apn}.apn.epc.mnc{mnc}.mcc724.3gppnetwork.org.'.format(
                    apn=apn,
                    mnc=mnc
                ),
                'order': 10,
                'preference': 10,
                'flags': 'a',
                'service': 'x-3gpp-pgw:x-s5-gtp:x-gn',
                'regexp': '""',
                'replacement': 'topoff.vip-s5.{node_name}.node.epc.mnc{replacement_mnc}.mcc724.3gppnetwork.org.'.format(
                    node_name=node, replacement_mnc=replacement_mnc
                ),
                'ttl': 300}
            )


def naptrrecord_node(views, node):
    global create_naptrrecord_node

    for mnc in mnc_list:
        for replacement_mnc in mnc_list:
            create_naptrrecord_node.append(add_node_resrec_naptr_s11.format(mnc=mnc, node_name=node,
                                                                            replacement_mnc=replacement_mnc,
                                                                            view_name=views))


def naptrrecord_node_f5(node):
    global create_naptrrecord_f5

    for mnc in mnc_list:
        for replacement_mnc in mnc_list:
            create_naptrrecord_f5.append({
                'domain_name': '{node_name}.node.epc.mnc{mnc}.mcc724.3gppnetwork.org.'.format(
                    node_name=node,
                    mnc=mnc
                ),
                'order': 10,
                'preference': 10,
                'flags': 'a',
                'service': 'x-3gpp-sgw:x-s11:x-s5-gtp',
                'regexp': '""',
                'replacement': 'topoff.vip-s11.{node_name}.node.epc.mnc{replacement_mnc}.'
                               'mcc724.3gppnetwork.org.'.format(
                    node_name=node, replacement_mnc=replacement_mnc
                ),
                'ttl': 300}
            )


def apn_arecord_s5(views, apn, ip):
    global create_apn_arecord_s5

    for mnc in mnc_list:
        create_apn_arecord_s5.append(add_apn_resrec_a_s5s8.format(mnc=mnc, domain_name=apn, node_ip=ip, view_name=views)
                                     )


def apn_arecord_s5_f5(apn, ip):
    global create_arecords_f5

    for mnc in mnc_list:
        create_arecords_f5.append({'domain_name': apn + '.mnc{mnc}.mcc724.gprs.'.format(mnc=mnc),
                                   'ip_address': ip,
                                   'ttl': 300})


def node_arecord(views, interface, node, ip):
    global create_arecord_s11
    global create_arecord_s5s8

    if interface == 's11':
        for mnc in mnc_list:
            create_arecord_s11.append(add_node_resrec_a.format(mnc=mnc, interface=interface, node_name=node,
                                                               node_ip=ip, view_name=views)
                                      )
    elif interface == 's5':
        for mnc in mnc_list:
            create_arecord_s5s8.append(add_node_resrec_a.format(mnc=mnc, interface=interface, node_name=node,
                                                                node_ip=ip, view_name=views)
                                       )


def node_arecord_f5(interface, node, ip):
    global create_arecords_f5

    for mnc in mnc_list:
        create_arecords_f5.append({'domain_name': 'topoff.vip-{interface}.{node_name}.node'.format(
            interface=interface, node_name=node) + '.mnc{mnc}.mcc724.3gppnetwork.org.'.format(mnc=mnc),
                                   'ip_address': ip,
                                   'ttl': 300})


def export_json_f5(project_name, paths):
    global create_arecords_f5
    global create_naptrrecord_f5

    if len(create_arecords_f5) != 0:
        with open(path.join(paths, '{}_entradas_A.txt'.format(project_name)), 'wb') as mnc02:
            for dicts in create_arecords_f5:
                mnc02.write(json.dumps(dicts))
                mnc02.write('\n')

    if len(create_naptrrecord_f5) != 0:
        with open(path.join(paths, '{}_entradas_NAPTR.txt'.format(project_name)), 'wb') as mnc02:
            for dicts in create_naptrrecord_f5:
                mnc02.write(json.dumps(dicts))
                mnc02.write('\n')


def export_huawei_config(project_name, paths):
    with open(path.join(paths, project_name + '.txt'), 'wb') as f:
        f.write('# Configuracoes de ARECORD para interfaces S11 e S5S8\n\n')
        for values in create_arecord_s11:
            f.write(values + '\n')
        for values in create_arecord_s5s8:
            f.write(values + '\n')
        f.write('\n# Configuracoes NAPTRRECORD para HANDOVER S-GW\n\n')
        for values in create_naptrrecord_node:
            f.write(values + '\n')
        f.write('\n# Configuracoes de NAPTRRECORD para APN de teste\n\n')
        for values in create_naptrrecord_apn:
            f.write(values + '\n')
        f.write('\n# Configuracoes de NAPTRRECORD para APN timbrasil.br\n\n')
        for values in create_naptrrecord_apn_timbrasil:
            f.write(values + '\n')
        f.write('\n# Configuracoes de ARECORD para APN de teste\n\n')
        for values in create_apn_arecord_s5:
            f.write(values + '\n')
        f.write('\nSAV CFG:;\n')


# noinspection PyBroadException
def main_saegw_pqr_tool():
    global create_arecord_s11
    global create_arecord_s5s8
    global create_apn_arecord_s5
    global create_naptrrecord_apn_timbrasil
    global create_naptrrecord_apn
    global create_naptrrecord_node

    global create_arecords_f5
    global create_naptrrecord_f5

    pattern = compile(r'\s+')

    print(u'Welcome to the SAE-GW Tool!')
    while True:
        print(u'Choose one of the options below to start: ')
        print(u'1: Create SAE-GW')
        print(u'2: Remove SAE-GW')
        print(u'3: Exit')
        choice = raw_input('> ').strip()

        if choice == '1':
            (node, s11, s5s8) = raw_input(
                'Enter with the loopbacks of node name, s11 and s5s8 interfaces separated by commas '
                '(fngrjo01,10.221.37.10,189.40.116.32): ').split(',')

            node = sub(pattern, '', node)
            s11 = sub(pattern, '', s11)
            s5s8 = sub(pattern, '', s5s8)

            for views in view_dns:
                node_arecord(views=views, interface="s11", node=node.upper(), ip=s11)
                node_arecord(views=views, interface="s5", node=node.upper(), ip=s5s8)
                apn_arecord_s5(views=views, apn=node.lower() + ".tim.br", ip=s5s8)
                apn_naptrrecord_s5s8(views=views, apn=node.lower() + ".tim.br", node=node.upper())
                naptrrecord_node(views=views, node=node.upper())

            node_arecord_f5(interface="s11", node=node.upper(), ip=s11)
            node_arecord_f5(interface="s5", node=node.upper(), ip=s5s8)
            apn_arecord_s5_f5(apn=node.lower() + ".tim.br", ip=s5s8)
            apn_naptrrecord_s5s8_f5(apn=node.lower() + ".tim.br", node=node.upper())
            apn_naptrrecord_s5s8_f5(apn="timbrasil.br", node=node.upper())
            naptrrecord_node_f5(node=node.upper())

            if node.upper().startswith('FNGS') or node.upper().startswith('GPBSA') or node.upper().startswith('GPCTA') \
                    or node.upper().startswith('GPS'):

                views = view_dns[1]
                apn_naptrrecord_s5s8(views=views, apn="timbrasil.br", node=node.upper())

            else:
                views = view_dns[0]
                apn_naptrrecord_s5s8(views=views, apn="timbrasil.br", node=node.upper())

            project_name = 'Preparacao_PQR_%s' % node.upper()

            new_dir_huawei = getcwd() + '\\' + 'Huawei_' + node.upper() + '_{:%d_%m_%Y}'.format(datetime.datetime.now())
            try:
                mkdir(new_dir_huawei)
                export_huawei_config(project_name=project_name, paths=new_dir_huawei)
            except Exception as err:
                export_huawei_config(project_name=project_name, paths=new_dir_huawei)
            print('Seu projeto para o DNS Huawei foi criado no diretorio abaixo:')
            print(new_dir_huawei + '\n')

            new_dir_f5 = getcwd() + '\\' + 'F5_' + node.upper() + '_{:%d_%m_%Y}'.format(datetime.datetime.now())
            try:
                mkdir(new_dir_f5)
                export_json_f5(project_name=project_name, paths=new_dir_f5)
            except Exception as err:
                export_json_f5(project_name=project_name, paths=new_dir_f5)
            print('Seu projeto para o DNS F5 foi criado no diretorio abaixo:')
            print(new_dir_f5 + '\n')

            yes_or_no = raw_input('Deseja criar mais projetos de preparacao de SAE-GW para PQR 4G? (S ou N): ')
            if yes_or_no == 'S' or yes_or_no == 's':

                create_arecord_s11 = []
                create_arecord_s5s8 = []
                create_apn_arecord_s5 = []
                create_naptrrecord_apn_timbrasil = []
                create_naptrrecord_apn = []
                create_naptrrecord_node = []
                create_arecords_f5 = []
                create_naptrrecord_f5 = []

                continue

            elif yes_or_no == 'N' or yes_or_no == 'n':

                break

        elif choice == '2':
            remove_sae_gw.main()

        elif choice == '3':
            print('Thank you for using the SAE-GW Tool!')
            break


if __name__ == '__main__':
    main_saegw_pqr_tool()
