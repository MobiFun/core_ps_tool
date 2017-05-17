from support_variables import view_dns
from os import getcwd

# Variables for DNS Huawei
create_a_record_s10_huawei = []
create_a_record_gn_huawei = []
create_naptrrecord_gn_huawei = []
create_naptrrecord_s10_huawei = []
lista_de_inputs_gn_huawei = []
lista_de_inputs_s10_huawei = []

# Variables for DNS Ericsson
create_a_record_s10_ericsson = []
create_a_record_gn_ericsson = []
create_naptrrecord_gn_ericsson = []
create_naptrrecord_s10_ericsson = []
lista_de_inputs_s10_ericsson = []
lista_de_inputs_gn_ericsson = []

def main_include_mme():
    sgsn_name = raw_input('Digite o nome dos SGSN/MME: ')
    mme_code = raw_input('Digite o mme code em hexadecimal de cada MME, separando por "," (C8,C9): ')
    ips_sgsns_range = raw_input(
        'Digite os IPs pertencentes as interfaces S10 e Gn dos SGSN/MME respectivamente, separando por ";"'
        ' (192.168.1.1,192.168.1.2;192.168.2.3,192.168.2.4): ')

    sgsns = sgsn_name.upper().strip().split(',')
    mme_codes = mme_code.upper().strip().split(',')

    aux_dict = {}

    ips_sgsn = ips_sgsns_range.strip().split(';')

    for x in xrange(len(sgsns)):
        aux_dict[sgsns[x]] = ips_sgsn[x].split(',')

    for x in xrange(len(sgsns)):
        lista_de_inputs_gn_ericsson.append([sgsns[x], mme_codes[x], aux_dict.get(sgsns[x])[1]])
        lista_de_inputs_s10_ericsson.append([sgsns[x], mme_codes[x], aux_dict.get(sgsns[x])[0]])
        for view in view_dns:
            lista_de_inputs_gn_huawei.append([sgsns[x], mme_codes[x], aux_dict.get(sgsns[x])[1], view])
            lista_de_inputs_s10_huawei.append([sgsns[x], mme_codes[x], aux_dict.get(sgsns[x])[0], view])

    # Script para DNS Huawei

    for x in xrange(len(lista_de_inputs_s10_huawei)):
        create_a_record_s10_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc002.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-s10.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_de_inputs_s10_huawei[x][0], lista_de_inputs_s10_huawei[x][2], lista_de_inputs_s10_huawei[x][3]))
        create_a_record_s10_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc003.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-s10.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_de_inputs_s10_huawei[x][0], lista_de_inputs_s10_huawei[x][2], lista_de_inputs_s10_huawei[x][3]))
        create_a_record_s10_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc004.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-s10.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_de_inputs_s10_huawei[x][0], lista_de_inputs_s10_huawei[x][2], lista_de_inputs_s10_huawei[x][3]))

        create_naptrrecord_s10_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc002.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-s10", REPLACEMENT="topoff.vip-s10.%s.node.epc.mnc002.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                lista_de_inputs_s10_huawei[x][1], lista_de_inputs_s10_huawei[x][0], lista_de_inputs_s10_huawei[x][3]))
        create_naptrrecord_s10_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc003.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-s10", REPLACEMENT="topoff.vip-s10.%s.node.epc.mnc003.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                lista_de_inputs_s10_huawei[x][1], lista_de_inputs_s10_huawei[x][0], lista_de_inputs_s10_huawei[x][3]))
        create_naptrrecord_s10_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc004.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-s10", REPLACEMENT="topoff.vip-s10.%s.node.epc.mnc004.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                lista_de_inputs_s10_huawei[x][1], lista_de_inputs_s10_huawei[x][0], lista_de_inputs_s10_huawei[x][3]))

    for x in xrange(len(lista_de_inputs_gn_huawei)):
        create_a_record_gn_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc002.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-gn.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_de_inputs_gn_huawei[x][0], lista_de_inputs_gn_huawei[x][2], lista_de_inputs_gn_huawei[x][3]))
        create_a_record_gn_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc004.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-gn.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_de_inputs_gn_huawei[x][0], lista_de_inputs_gn_huawei[x][2], lista_de_inputs_gn_huawei[x][3]))
        create_a_record_gn_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc003.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-gn.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_de_inputs_gn_huawei[x][0], lista_de_inputs_gn_huawei[x][2], lista_de_inputs_gn_huawei[x][3]))
        create_naptrrecord_gn_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc002.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-gn", REPLACEMENT="topoff.vip-gn.%s.node.epc.mnc002.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                lista_de_inputs_gn_huawei[x][1], lista_de_inputs_gn_huawei[x][0], lista_de_inputs_gn_huawei[x][3]))
        create_naptrrecord_gn_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc003.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-gn", REPLACEMENT="topoff.vip-gn.%s.node.epc.mnc003.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                lista_de_inputs_gn_huawei[x][1], lista_de_inputs_gn_huawei[x][0], lista_de_inputs_gn_huawei[x][3]))
        create_naptrrecord_gn_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc004.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-gn", REPLACEMENT="topoff.vip-gn.%s.node.epc.mnc004.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                lista_de_inputs_gn_huawei[x][1], lista_de_inputs_gn_huawei[x][0], lista_de_inputs_gn_huawei[x][3]))

    nome_sgsn = ''

    for values in sgsns:
        nome_sgsn += values + ' '

    with open('Entradas_DNS_Huawei_%s.txt' % (nome_sgsn), 'wb') as f:
        for values in create_a_record_s10_huawei:
            f.write(values + '\n')
        f.write('\n')

        for values in create_a_record_gn_huawei:
            f.write(values + '\n')
        f.write('\n')

        for values in create_naptrrecord_gn_huawei:
            f.write(values + '\n')
        f.write('\n')

        for values in create_naptrrecord_s10_huawei:
            f.write(values + '\n')
        f.write('\n')

    # Script para DNS Ericsson

    for x in xrange(len(lista_de_inputs_s10_ericsson)):
        create_a_record_s10_ericsson.append(
            'create arecord topoff.vip-s10.%s.node.epc.mnc002.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_de_inputs_s10_ericsson[x][0], lista_de_inputs_s10_ericsson[x][2]))
        create_a_record_s10_ericsson.append(
            'create arecord topoff.vip-s10.%s.node.epc.mnc003.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_de_inputs_s10_ericsson[x][0], lista_de_inputs_s10_ericsson[x][2]))
        create_a_record_s10_ericsson.append(
            'create arecord topoff.vip-s10.%s.node.epc.mnc004.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_de_inputs_s10_ericsson[x][0], lista_de_inputs_s10_ericsson[x][2]))

        create_naptrrecord_s10_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-s10";regexp="";replacement=topoff.vip-s10.%s.node.epc.mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                lista_de_inputs_s10_ericsson[x][1], lista_de_inputs_s10_ericsson[x][0]))
        create_naptrrecord_s10_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-s10";regexp="";replacement=topoff.vip-s10.%s.node.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                lista_de_inputs_s10_ericsson[x][1], lista_de_inputs_s10_ericsson[x][0]))
        create_naptrrecord_s10_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc004.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-s10";regexp="";replacement=topoff.vip-s10.%s.node.epc.mnc004.mcc724.3gppnetwork.org.;container=GPRS' % (
                lista_de_inputs_s10_ericsson[x][1], lista_de_inputs_s10_ericsson[x][0]))

    for x in xrange(len(lista_de_inputs_gn_ericsson)):
        create_a_record_gn_ericsson.append(
            'create arecord topoff.vip-gn.%s.node.epc.mnc002.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_de_inputs_gn_ericsson[x][0], lista_de_inputs_gn_ericsson[x][2]))
        create_a_record_gn_ericsson.append(
            'create arecord topoff.vip-gn.%s.node.epc.mnc003.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_de_inputs_gn_ericsson[x][0], lista_de_inputs_gn_ericsson[x][2]))
        create_a_record_gn_ericsson.append(
            'create arecord topoff.vip-gn.%s.node.epc.mnc004.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_de_inputs_gn_ericsson[x][0], lista_de_inputs_gn_ericsson[x][2]))

        create_naptrrecord_gn_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-gn";regexp="";replacement=topoff.vip-gn.%s.node.epc.mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                lista_de_inputs_gn_ericsson[x][1], lista_de_inputs_gn_ericsson[x][0]))
        create_naptrrecord_gn_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-gn";regexp="";replacement=topoff.vip-gn.%s.node.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                lista_de_inputs_gn_ericsson[x][1], lista_de_inputs_gn_ericsson[x][0]))
        create_naptrrecord_gn_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc004.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-gn";regexp="";replacement=topoff.vip-gn.%s.node.epc.mnc004.mcc724.3gppnetwork.org.;container=GPRS' % (
                lista_de_inputs_gn_ericsson[x][1], lista_de_inputs_gn_ericsson[x][0]))

    with open('Entradas_DNS_Ericsson_%s.txt' % (nome_sgsn), 'wb') as f:
        for values in create_a_record_s10_ericsson:
            f.write(values + '\n')
        f.write('\n')

        for values in create_a_record_gn_ericsson:
            f.write(values + '\n')
        f.write('\n')

        for values in create_naptrrecord_gn_ericsson:
            f.write(values + '\n')
        f.write('\n')

        for values in create_naptrrecord_s10_ericsson:
            f.write(values + '\n')
        f.write('\n')

    print('Seu projeto foi criado no diretorio abaixo:')
    print(getcwd() + '\\' + 'Entradas_DNS_Ericsson_'+ nome_sgsn +'.txt'+ '\n')
    print(getcwd() + '\\' + 'Entradas_DNS_Huawei_'+ nome_sgsn +'.txt'+ '\n')

if __name__ == '__main__':
    main_include_mme()