from support_variables import vlr_anf, tac_mnc02, tac_mnc03

# MNC02 Variables
delete_tac_naptrrecord_mnc02 = []
create_naptrrecord_mnc02_s11 = []
create_naptrrecord_mnc02_s10 = []

create_ga_mnc02 = []
create_ga_ta_range_mnc02 = []
create_la_mnc02 = []
create_msc_la_mnc02 = []

# MNC03 Variables
delete_tac_naptrrecord_mnc03 = []
create_naptrrecord_mnc03_s11 = []
create_naptrrecord_mnc03_s10 = []

create_ga_mnc03 = []
create_ga_ta_range_mnc03 = []
create_la_mnc03 = []
create_msc_la_mnc03 = []

# MNC04 Variables
delete_tac_naptrrecord_mnc04 = []
create_naptrrecord_mnc04_s11 = []
create_naptrrecord_mnc04_s10 = []


def create_naptrrecord_s10_ericsson(lista_tac_dec, lista_tac_hex):
    counter_ericsson = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] == '33' or TAC[0:2] == '37':
            create_naptrrecord_mnc02_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-gn:x-s10";regexp="";replacement=topoff.vip-gn.DMBHE1.node.epc.'
                'mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc02_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-gn:x-s10";regexp="";replacement=topoff.vip-gn.DMSDR1.node.epc.'
                'mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        elif TAC[0:2] == '34' or TAC[0:2] == '35' or TAC[0:2] == '36':
            create_naptrrecord_mnc04_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc004.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-gn:x-s10";regexp="";replacement=topoff.vip-gn.DMBSA1.node.epc.'
                'mnc004.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc04_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc004.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-gn:x-s10";regexp="";replacement=topoff.vip-gn.DMCTA1.node.epc.'
                'mnc004.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        elif TAC[0:3] == '392' or TAC[0:3] == '397':
            create_naptrrecord_mnc02_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-gn:x-s10";regexp="";replacement=topoff.vip-gn.DMMNS1.node.epc.'
                'mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        elif TAC[0:3] == '311' or TAC[0:3] == '312' or TAC[0:3] == '316' or TAC[0:3] == '317' or TAC[0:3] == '318':
            create_naptrrecord_mnc03_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-s10";regexp="";replacement=topoff.vip-s10.DSPO07.node.epc.mnc003'
                '.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        elif TAC[0:2] == '32':
            create_naptrrecord_mnc02_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-s10";regexp="";replacement=topoff.vip-s10.DMRJO2.node.epc.mnc002'
                '.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        elif TAC[0:3] == '313' or TAC[0:3] == '314' or TAC[0:3] == '315' or TAC[0:3] == '319':

            create_naptrrecord_mnc03_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-s10";regexp="";replacement=topoff.vip-s10.DMRJO2.node.epc.mnc003'
                '.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        elif TAC[0:3] == '391' or TAC[0:3] == '393' or TAC[0:3] == '394' \
                or TAC[0:3] == '396' or TAC[0:3] == '398' or TAC[0:3] == '399' or TAC[0:3] == '395' \
                or TAC[0:2] == '38':

            create_naptrrecord_mnc02_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-gn:x-s10";regexp="";replacement=topoff.vip-gn.DMRCE1.node.epc.'
                'mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc02_s10.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-mme:x-gn:x-s10";regexp="";replacement=topoff.vip-gn.DMBLM1.node.epc.'
                'mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        counter_ericsson += 1


def create_naptrrecord_s11_ericsson(lista_tac_dec, lista_tac_hex):
    counter_ericsson = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] in tac_mnc02:

            # delete_tac_naptrrecord_mnc02.append('delete naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724
            # .3gppnetwork.org. -where container=GPRS' %(lista_tac_hex[counter_ericsson][4:],
            # lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc02_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s8-gtp";regexp="";replacement=topoff.vip-s11.GPRJO2.node'
                '.epc.mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc02_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGRJO05.node'
                '.epc.mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc02_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc002.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGRJO06.node'
                '.epc.mnc002.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        elif TAC[0:2] in tac_mnc03:
            # delete_tac_naptrrecord_mnc03.append('delete naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.
            # 3gppnetwork.org. -where container=GPRS' %(lista_tac_hex[counter_ericsson][4:],
            # lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s8-gtp";regexp="";replacement=topoff.vip-s11.GPSPO2.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGSNE03.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGSNE04.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGSNE05.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGSPO03.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGSPO04.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGSPO05.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))
            create_naptrrecord_mnc03_s11.append(
                'create naptrrecord tac-lb%s.tac-hb%s.tac.epc.mnc003.mcc724.3gppnetwork.org. -set order=10;preference='
                '65525;flags="a";service="x-3gpp-sgw:x-s11:x-s5-gtp";regexp="";replacement=topoff.vip-s11.FNGSNE01.node'
                '.epc.mnc003.mcc724.3gppnetwork.org.;container=GPRS' % (
                    lista_tac_hex[counter_ericsson][4:], lista_tac_hex[counter_ericsson][2:4]))

        counter_ericsson += 1


def create_inputs_mme_ericsson(lista_lac_dec, lista_tac_dec):
    counter_ericsson = 0
    for TAC in lista_tac_dec:
        if TAC[0:2] == '32':
            create_ga_mnc02.append('gsh create_ga -gan GA%s' % (lista_lac_dec[counter_ericsson]))
            create_ga_ta_range_mnc02.append(
                'gsh create_ga_ta_range -gan GA%s   -tan TA%s  -mcc 724 -mnc 02 -first %s  -last %s' % (
                    lista_lac_dec[counter_ericsson], lista_tac_dec[counter_ericsson], lista_tac_dec[counter_ericsson],
                    lista_tac_dec[counter_ericsson]))
            create_la_mnc02.append(
                'gsh create_la -mcc 724 -mnc 02 -lac %s  -gan GA%s  -defsgsmsc %s.MNC02.MCC724.3GPPNETWORK.ORG' % (
                    lista_lac_dec[counter_ericsson], lista_lac_dec[counter_ericsson],
                    vlr_anf.get(lista_lac_dec[counter_ericsson][-2:])))
            create_msc_la_mnc02.append(
                'gsh create_msc_la -msc %s.MNC02.MCC724.3GPPNETWORK.ORG -mcc 724 -mnc 02 -lac %s' % (
                    vlr_anf.get(lista_lac_dec[counter_ericsson][-2:]), lista_lac_dec[counter_ericsson]))

        elif TAC[0:2] in tac_mnc03:
            create_ga_mnc03.append('gsh create_ga -gan GA%s' % (lista_lac_dec[counter_ericsson]))
            create_ga_ta_range_mnc03.append(
                'gsh create_ga_ta_range -gan GA%s   -tan TA%s  -mcc 724 -mnc 03 -first %s  -last %s' % (
                    lista_lac_dec[counter_ericsson], lista_tac_dec[counter_ericsson], lista_tac_dec[counter_ericsson],
                    lista_tac_dec[counter_ericsson]))
            create_la_mnc03.append(
                'gsh create_la -mcc 724 -mnc 03 -lac %s  -gan GA%s  -defsgsmsc %s.MNC03.MCC724.3GPPNETWORK.ORG' % (
                    lista_lac_dec[counter_ericsson], lista_lac_dec[counter_ericsson],
                    vlr_anf.get(lista_lac_dec[counter_ericsson][-2:])))
            create_msc_la_mnc03.append(
                'gsh create_msc_la -msc %s.MNC03.MCC724.3GPPNETWORK.ORG -mcc 724 -mnc 03 -lac %s' % (
                    vlr_anf.get(lista_lac_dec[counter_ericsson][-2:]), lista_lac_dec[counter_ericsson]))

        counter_ericsson += 1
