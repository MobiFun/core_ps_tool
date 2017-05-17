from support_variables import view_dns
from os import getcwd
import re


lista_auxiliar = []
lista_mme_codes = []

# Variables for DNS Huawei
create_a_record_s10_gn_huawei = []
create_naptrrecord_s10_gn_huawei = []

# Variables for DNS Ericsson
create_a_record_s10_gn_ericsson = []
create_naptrrecord_s10_gn_ericsson = []


def main_include_mme():
    pattern = re.compile(r'\s+')

    sgsn_name = raw_input('Digite o nome dos SGSN/MME: ')
    mme_codes = raw_input('Digite o mme code em hexadecimal de cada MME, separando os codigos de mesmo MMEs por ";" e '
                         'de diferentes MMEs por "," (C8;C9,C10;C11): ')
    ips_sgsns_range = raw_input(
        'Digite os IPs pertencentes as interfaces S10_Gn dos SGSN/MME respectivamente, separando por ","'
        ' (192.168.1.1,192.168.2.4): ')

    sgsn_name = re.sub(pattern, '', sgsn_name).upper()
    mme_codes = re.sub(pattern, '', mme_codes).upper()
    ips_sgsns_range = re.sub(pattern, '', ips_sgsns_range)

    for x in xrange(len(sgsn_name.split(','))):
        lista_auxiliar.append([sgsn_name.split(',')[x], mme_codes.split(',')[x],ips_sgsns_range.split(',')[x]])

    for x in xrange(len(sgsn_name.split(','))):
        lista_mme_codes.append(lista_auxiliar[x][1].split(';'))

    for x in xrange(len(lista_auxiliar)):
        for views in view_dns:
            create_a_record_s10_gn_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc002.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-gn.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_auxiliar[x][0], lista_auxiliar[x][2], views))
            create_a_record_s10_gn_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc003.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-gn.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_auxiliar[x][0], lista_auxiliar[x][2], views))
            create_a_record_s10_gn_huawei.append(
            'ADD RESREC: TYPE=A, ZONE="epc.mnc004.mcc724.3gppnetwork.org", DOMAIN="topoff.vip-gn.%s.node", IP="%s", VIEWNAME="%s";' % (
                lista_auxiliar[x][0], lista_auxiliar[x][2], views))

    for x in xrange(len(lista_auxiliar)):
        for values in lista_mme_codes[x]:
            for views in view_dns:
                create_naptrrecord_s10_gn_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc002.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-s10:x-gn", REPLACEMENT="topoff.vip-gn.%s.node.epc.mnc002.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                values, lista_auxiliar[x][0], views))
                create_naptrrecord_s10_gn_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc003.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-s10:x-gn", REPLACEMENT="topoff.vip-gn.%s.node.epc.mnc003.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                values, lista_auxiliar[x][0], views))
                create_naptrrecord_s10_gn_huawei.append(
            'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc004.mcc724.3gppnetwork.org", DOMAIN="mmec%s.mmegi8500.mme", ORDER=10, PREF=10, FLAGS=A, SERVICE="x-3gpp-mme:x-s10:x-gn", REPLACEMENT="topoff.vip-gn.%s.node.epc.mnc004.mcc724.3gppnetwork.org.", VIEWNAME="%s";' % (
                values, lista_auxiliar[x][0], views))

    for x in xrange(len(lista_auxiliar)):
        create_a_record_s10_gn_ericsson.append(
            'create arecord topoff.vip-gn.%s.node.epc.mnc002.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_auxiliar[x][0], lista_auxiliar[x][2]))
        create_a_record_s10_gn_ericsson.append(
            'create arecord topoff.vip-gn.%s.node.epc.mnc003.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_auxiliar[x][0], lista_auxiliar[x][2]))
        create_a_record_s10_gn_ericsson.append(
            'create arecord topoff.vip-gn.%s.node.epc.mnc004.mcc724.3gppnetwork.org. %s -set container=GPRS' % (
                lista_auxiliar[x][0], lista_auxiliar[x][2]))
    for x in xrange(len(lista_auxiliar)):
        for values in lista_mme_codes[x]:
            create_naptrrecord_s10_gn_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-s10:x-gn";regexp="";replacement=topoff.vip-gn.%s.node.epc.mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                values, lista_auxiliar[x][0]))
            create_naptrrecord_s10_gn_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-s10:x-gn";regexp="";replacement=topoff.vip-gn.%s.node.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                values, lista_auxiliar[x][0]))
            create_naptrrecord_s10_gn_ericsson.append(
            'create naptrrecord mmec%s.mmegi8500.mme.epc.mnc004.mcc724.3gppnetwork.org. -set order=10;preference=65525;flags="a";service="x-3gpp-mme:x-s10:x-gn";regexp="";replacement=topoff.vip-gn.%s.node.epc.mnc004.mcc724.3gppnetwork.org.;container=GPRS' % (
                values, lista_auxiliar[x][0]))
    nome_sgsn = ''

    for values in sgsn_name.split(','):
        nome_sgsn += values + ' '

    with open('Entradas_DNS_Ericsson_%s.txt' % (nome_sgsn), 'wb') as f:
        for values in create_a_record_s10_gn_ericsson:
            f.write(values + '\n')
        f.write('\n')

        for values in create_naptrrecord_s10_gn_ericsson:
            f.write(values + '\n')
        f.write('\n')

    with open('Entradas_DNS_Huawei_%s.txt' % (nome_sgsn), 'wb') as f:
        for values in create_a_record_s10_gn_huawei:
            f.write(values + '\n')
        f.write('\n')

        for values in create_naptrrecord_s10_gn_huawei:
            f.write(values + '\n')
        f.write('\n')

    print('Seu projeto foi criado no diretorio abaixo:')
    print(getcwd() + '\\' + 'Entradas_DNS_Ericsson_'+ nome_sgsn +'.txt'+ '\n')
    print(getcwd() + '\\' + 'Entradas_DNS_Huawei_'+ nome_sgsn +'.txt'+ '\n')

if __name__ == '__main__':
    main_include_mme()