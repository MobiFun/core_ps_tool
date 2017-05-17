# coding=utf-8
from support_variables import rmv_resrec, add_resrec, view_dns
from support_functions import find_between
import os


def main():
    print('Welcome to the SAE-GW Removal Tool!')
    file_input = raw_input('Please type in the path to the DNS export file: ')
    sae_gw = raw_input('Please type in the name of the SAE-GW you want to remove: ')

    base_folder = os.path.abspath(os.path.dirname(__file__))
    destination_folder = u'Projetos SAE-GW'
    full_path = os.path.join(base_folder, destination_folder)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    tac_data, apn_data, node_ip_s5, node_ip_s11 = gather_dns_records(file_input, sae_gw)

    tac_entries, fallback_tac_entries = create_dns_script_for_tac(tac_data, sae_gw)

    apn_entries, fallback_apn_entries = create_dns_script_for_apn(apn_data, sae_gw, node_ip_s5, node_ip_s11)

    export_configurations(tac_entries, apn_entries, os.path.join(full_path, 'Remover_Entradas_{}.txt'.format(sae_gw)))

    export_configurations(fallback_tac_entries, fallback_apn_entries,
                          os.path.join(full_path, 'FALLBACK_Remover_Entradas_{}.txt'.format(sae_gw)))

    print('Your projects were created within the folder {}'.format(full_path))


def gather_dns_records(file_input, sae_gw):
    all_tac_data = []
    apn_data = []
    node_ip_s5 = ''
    node_ip_s11 = ''
    with open(file_input) as fin:
        for lines in fin:
            lines = lines.strip()
            if lines.startswith('tac-lb'):
                if find_between(lines, 'topoff.vip-s11.', '.node.epc') == sae_gw.upper():
                    tac = {'tac-lb': find_between(lines, 'tac-lb', '.tac-hb'),
                           'tac-hb': find_between(lines, '.tac-hb', '.tac.epc'),
                           'mnc': find_between(lines, 'epc.mnc', '.mcc')
                           }
                    all_tac_data.append(tac)
            elif lines.startswith('topoff.vip-s5.{}'.format(sae_gw.upper())):
                node_ip_s5 = find_between(lines, '.3gppnetwork.org', '').strip()
            elif lines.startswith('topoff.vip-s11.{}'.format(sae_gw.upper())):
                node_ip_s11 = find_between(lines, '.3gppnetwork.org', '').strip()
            elif lines.startswith('timbrasil.br.55'):
                if find_between(lines, '""', '.tim.br').strip() == sae_gw.lower():
                    apn = {
                        'msisdn': find_between(lines, 'timbrasil.br.', '.mnc'),
                        'mnc': find_between(lines, '.mnc', '.mcc'),

                    }
                    apn_data.append(apn)
                elif find_between(lines, '""', '.tim.br').strip() == sae_gw.upper():
                    apn = {
                        'msisdn': find_between(lines, 'timbrasil.br.', '.mnc'),
                        'mnc': find_between(lines, '.mnc', '.mcc'),

                    }
                    apn_data.append(apn)

    return all_tac_data, apn_data, node_ip_s5, node_ip_s11


def create_dns_script_for_tac(tac_data, sae_gw):
    dns_entries = []
    fallback_dns_entries = []
    for views in view_dns:
        for dicts in tac_data:
            if sae_gw not in ['FNGRJO06', 'FNGSPO04']:
                dns_entries.append(rmv_resrec.format(mnc=dicts.get('mnc'),
                                                     tac_lb=dicts.get('tac-lb'),
                                                     tac_hb=dicts.get('tac-hb'),
                                                     order='10',
                                                     view_name=views,
                                                     service='x-3gpp-sgw:x-s11:x-s5-gtp',
                                                     interface='s11',
                                                     node_name=sae_gw.upper()
                                                     )
                                   )
                fallback_dns_entries.append(add_resrec.format(mnc=dicts.get('mnc'),
                                                              tac_lb=dicts.get('tac-lb'),
                                                              tac_hb=dicts.get('tac-hb'),
                                                              order='10',
                                                              view_name=views,
                                                              service='x-3gpp-sgw:x-s11:x-s5-gtp',
                                                              interface='s11',
                                                              node_name=sae_gw.upper()
                                                              )
                                            )

            else:
                if sae_gw.upper() == 'FNGRJO06':
                    if dicts.get('mnc') == '002':
                        dns_entries.append(rmv_resrec.format(mnc=dicts.get('mnc'),
                                                             tac_lb=dicts.get('tac-lb'),
                                                             tac_hb=dicts.get('tac-hb'),
                                                             order='10',
                                                             view_name=views,
                                                             service='x-3gpp-sgw:x-s11:x-s5-gtp',
                                                             interface='s11',
                                                             node_name=sae_gw.upper()
                                                             )
                                           )
                        fallback_dns_entries.append(add_resrec.format(mnc=dicts.get('mnc'),
                                                                      tac_lb=dicts.get('tac-lb'),
                                                                      tac_hb=dicts.get('tac-hb'),
                                                                      order='10',
                                                                      view_name=views,
                                                                      service='x-3gpp-sgw:x-s11:x-s5-gtp',
                                                                      interface='s11',
                                                                      node_name=sae_gw.upper()
                                                                      )
                                                    )

                else:
                    if dicts.get('mnc') != '002':
                        dns_entries.append(rmv_resrec.format(mnc=dicts.get('mnc'),
                                                             tac_lb=dicts.get('tac-lb'),
                                                             tac_hb=dicts.get('tac-hb'),
                                                             order='10',
                                                             view_name=views,
                                                             service='x-3gpp-sgw:x-s11:x-s5-gtp',
                                                             interface='s11',
                                                             node_name=sae_gw.upper()
                                                             )
                                           )
                        fallback_dns_entries.append(add_resrec.format(mnc=dicts.get('mnc'),
                                                                      tac_lb=dicts.get('tac-lb'),
                                                                      tac_hb=dicts.get('tac-hb'),
                                                                      order='10',
                                                                      view_name=views,
                                                                      service='x-3gpp-sgw:x-s11:x-s5-gtp',
                                                                      interface='s11',
                                                                      node_name=sae_gw.upper()
                                                                      )
                                                    )

    return set(dns_entries), set(fallback_dns_entries)


def create_dns_script_for_apn(apn_data, sae_gw, node_ip_s5, node_ip_s11):
    rmv_apn_naptr = 'RMV RESREC: TYPE=NAPTR, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
                    'DOMAIN="{apn}.apn", NAPTRSWITCH=ON, ORDER=10, PREF=10, VIEWNAME="{view_name}", ' \
                    'FLAGS=A, SERVICE="x-3gpp-pgw:x-s5-gtp:x-gn", ' \
                    'REPLACEMENT="topoff.vip-s5.{node_name}.node.epc.mnc{mnc}.mcc724.3gppnetwork.org.";'

    rmv_apn_msisdn = 'RMV RESREC: TYPE=NAPTR, ZONE="mnc{mnc}.mcc724.gprs", ' \
                     'DOMAIN="timbrasil.br.{msisdn}", NAPTRSWITCH=ON, ORDER=10, PREF=10, VIEWNAME="{view_name}", ' \
                     'FLAGS=A, SERVICE="x-3gpp-ggsn:x-gn:x-gp", ' \
                     'REPLACEMENT="{node_name}.tim.br.mnc{mnc}.mcc724.gprs.";'

    add_apn_naptr = 'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
                    'DOMAIN="{apn}.apn", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-pgw:x-s5-gtp:x-gn", ' \
                    'REPLACEMENT="topoff.vip-s5.{node_name}.node.epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
                    'VIEWNAME="{view_name}";'

    add_apn_msisdn = 'ADD RESREC: TYPE=NAPTR, ZONE="mnc{mnc}.mcc724.gprs", ' \
                     'DOMAIN="timbrasil.br.{msisdn}", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-ggsn:x-gn:x-gp", ' \
                     'REPLACEMENT="{node_name}.tim.br.mnc{mnc}.mcc724.gprs", ' \
                     'VIEWNAME="{view_name}";'

    rmv_apn_a = 'RMV RESREC: TYPE=A, ZONE="mnc{mnc}.mcc724.gprs", DOMAIN="{apn}", ' \
                'IP="{node_ip}", VIEWNAME="{view_name}";'

    add_apn_a = 'ADD RESREC: TYPE=A, ZONE="mnc{mnc}.mcc724.gprs", DOMAIN="{domain}", IP="{node_ip}", ' \
                'VIEWNAME="{view_name}";'
    rmv_node_a = 'RMV RESREC: TYPE=A, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", DOMAIN="{domain}", ' \
                 'IP="{node_ip}", VIEWNAME="{view_name}";'

    add_node_a = 'ADD RESREC: TYPE=A, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", DOMAIN="{domain}", IP="{node_ip}", ' \
                 'VIEWNAME="{view_name}";'
    dns_entries = []
    fallback_dns_entries = []
    if sae_gw.startswith('FNGS') or sae_gw.startswith('GPBSA') or sae_gw.startswith('GPCTA') or sae_gw.startswith(
            'GPS'):
        for views in [view_dns[1], view_dns[3]]:
            for mnc in ['002', '003', '004']:
                dns_entries.append(rmv_apn_a.format(mnc=mnc,
                                                    apn='timbrasil.br',
                                                    node_ip=node_ip_s5,
                                                    view_name=views)
                                   )
                dns_entries.append(rmv_apn_a.format(mnc=mnc,
                                                    apn='{}.tim.br'.format(sae_gw.lower()),
                                                    node_ip=node_ip_s5,
                                                    view_name=views)
                                   )
                dns_entries.append(rmv_node_a.format(mnc=mnc,
                                                     domain='topoff.vip-s5.{}.node'.format(sae_gw.upper(), mnc=mnc),
                                                     node_ip=node_ip_s5,
                                                     view_name=views
                                                     )
                                   )
                dns_entries.append(rmv_node_a.format(mnc=mnc,
                                                     domain='topoff.vip-s11.{}.node'.format(sae_gw.upper(), mnc=mnc),
                                                     node_ip=node_ip_s11,
                                                     view_name=views
                                                     )
                                   )
                dns_entries.append(rmv_apn_naptr.format(mnc=mnc,
                                                        apn='timbrasil.br',
                                                        view_name=views,
                                                        node_name=sae_gw.upper())
                                   )
                dns_entries.append(rmv_apn_naptr.format(mnc=mnc,
                                                        apn='{}.tim.br'.format(sae_gw.lower()),
                                                        view_name=views,
                                                        node_name=sae_gw.upper())
                                   )
                fallback_dns_entries.append(add_apn_a.format(mnc=mnc,
                                                             domain='timbrasil.br',
                                                             node_ip=node_ip_s5,
                                                             view_name=views)
                                            )
                fallback_dns_entries.append(add_apn_a.format(mnc=mnc,
                                                             domain='{}.tim.br'.format(sae_gw.lower()),
                                                             node_ip=node_ip_s5,
                                                             view_name=views)
                                            )
                fallback_dns_entries.append(add_node_a.format(mnc=mnc,
                                                              domain='topoff.vip-s5.{}.node'.format(sae_gw.upper(),
                                                                                                    mnc=mnc),
                                                              node_ip=node_ip_s5,
                                                              view_name=views)
                                            )
                fallback_dns_entries.append(add_node_a.format(mnc=mnc,
                                                              domain='topoff.vip-s11.{}.node'.format(sae_gw.upper(),
                                                                                                     mnc=mnc),
                                                              node_ip=node_ip_s11,
                                                              view_name=views)
                                            )
                fallback_dns_entries.append(add_apn_naptr.format(mnc=mnc,
                                                                 apn='timbrasil.br',
                                                                 view_name=views,
                                                                 node_name=sae_gw.upper())
                                            )
                fallback_dns_entries.append(add_apn_naptr.format(mnc=mnc,
                                                                 apn='{}.tim.br'.format(sae_gw.lower()),
                                                                 view_name=views,
                                                                 node_name=sae_gw.upper())
                                            )
            for apn in apn_data:
                dns_entries.append(rmv_apn_msisdn.format(mnc=apn.get('mnc'),
                                                         msisdn=apn.get('msisdn'),
                                                         view_name=views,
                                                         node_name=sae_gw.lower())
                                   )
                fallback_dns_entries.append(add_apn_msisdn.format(mnc=apn.get('mnc'),
                                                                  msisdn=apn.get('msisdn'),
                                                                  view_name=views,
                                                                  node_name=sae_gw.lower())
                                            )
    else:
        for views in [view_dns[0], view_dns[2]]:
            for mnc in ['002', '003', '004']:
                dns_entries.append(rmv_apn_a.format(mnc=mnc,
                                                    apn='timbrasil.br',
                                                    node_ip=node_ip_s5,
                                                    view_name=views)
                                   )
                dns_entries.append(rmv_apn_a.format(mnc=mnc,
                                                    apn='{}.tim.br'.format(sae_gw.lower()),
                                                    node_ip=node_ip_s5,
                                                    view_name=views)
                                   )
                dns_entries.append(rmv_node_a.format(mnc=mnc,
                                                     domain='topoff.vip-s5.{}.node'.format(sae_gw.upper(), mnc=mnc),
                                                     node_ip=node_ip_s5,
                                                     view_name=views
                                                     )
                                   )
                dns_entries.append(rmv_node_a.format(mnc=mnc,
                                                     domain='topoff.vip-s11.{}.node'.format(sae_gw.upper(), mnc=mnc),
                                                     node_ip=node_ip_s11,
                                                     view_name=views
                                                     )
                                   )
                dns_entries.append(rmv_apn_naptr.format(mnc=mnc,
                                                        apn='timbrasil.br',
                                                        view_name=views,
                                                        node_name=sae_gw.upper())
                                   )
                dns_entries.append(rmv_apn_naptr.format(mnc=mnc,
                                                        apn='{}.tim.br'.format(sae_gw.lower()),
                                                        view_name=views,
                                                        node_name=sae_gw.upper())
                                   )
                fallback_dns_entries.append(add_apn_a.format(mnc=mnc,
                                                             domain='timbrasil.br',
                                                             node_ip=node_ip_s5,
                                                             view_name=views)
                                            )
                fallback_dns_entries.append(add_apn_a.format(mnc=mnc,
                                                             domain='{}.tim.br'.format(sae_gw.lower()),
                                                             node_ip=node_ip_s5,
                                                             view_name=views)
                                            )
                fallback_dns_entries.append(add_node_a.format(mnc=mnc,
                                                              domain='topoff.vip-s5.{}.node'.format(sae_gw.upper(),
                                                                                                    mnc=mnc),
                                                              node_ip=node_ip_s5,
                                                              view_name=views)
                                            )
                fallback_dns_entries.append(add_node_a.format(mnc=mnc,
                                                              domain='topoff.vip-s11.{}.node'.format(sae_gw.upper(),
                                                                                                     mnc=mnc),
                                                              node_ip=node_ip_s11,
                                                              view_name=views)
                                            )
                fallback_dns_entries.append(add_apn_naptr.format(mnc=mnc,
                                                                 apn='timbrasil.br',
                                                                 view_name=views,
                                                                 node_name=sae_gw.upper())
                                            )
                fallback_dns_entries.append(add_apn_naptr.format(mnc=mnc,
                                                                 apn='{}.tim.br'.format(sae_gw.lower()),
                                                                 view_name=views,
                                                                 node_name=sae_gw.upper())
                                            )
            for apn in apn_data:
                dns_entries.append(rmv_apn_msisdn.format(mnc=apn.get('mnc'),
                                                         msisdn=apn.get('msisdn'),
                                                         view_name=views,
                                                         node_name=sae_gw.lower())
                                   )
                fallback_dns_entries.append(add_apn_msisdn.format(mnc=apn.get('mnc'),
                                                                  msisdn=apn.get('msisdn'),
                                                                  view_name=views,
                                                                  node_name=sae_gw.lower())
                                            )
    return dns_entries, fallback_dns_entries


def export_configurations(tac_entries, apn_entries, file_output):
    with open(file_output, 'w') as fout:
        fout.write('/* Entradas das TACs para o SAE-GW */\n')
        for entries in tac_entries:
            fout.write(entries + '\n')
        fout.write('\n/* Entradas das APNs para o SAE-GW */\n')
        for entries in apn_entries:
            fout.write(entries + '\n')
        fout.write('\nSAV CFG:;')


if __name__ == '__main__':
    main()
