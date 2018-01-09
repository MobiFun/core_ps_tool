check_config = ['gsh check_config', 'gsh activate_config_pending']  # Ericsson SGSN/MME Configuration

view_dns = ['REGIAO.A.NORTE', 'REGIAO.A.SUL', 'REGIAO.A.NORTE2', 'REGIAO.A.SUL2']  # Old views from Huawei DNS

saegw_rj = ['GPRJO3', 'GPRJO4']
saegw_sp = ['GPSNE1', 'GPSPO3']

tac_mnc02 = ['32', '33', '37', '38', '39']

tac_mnc03 = ['31']

tac_mnc04 = ['34', '35', '36']

mnc_select = {'1': '003',
              '2': '002',
              '3': '002',
              '4': '004',
              '5': '004',
              '6': '004',
              '7': '002',
              '8': '002',
              '9': '002',
              }

lai_vlr = {
    # Sao Paulo (1x)
    'ZSNE01': '551184138800',
    'ZSNE03': '55 1185238800',
    'ZSNE04': '551184136000',
    'ZSNE07': '551981799000',
    'ZSNE08': '551184137200',
    'ZSNE10': '551181133000',
    'ZSPO02': '551185239000',
    'ZSPO05': '551181138500',
    'ZSPO09': '551181132800',
    # Rio de Janeiro (2x)
    'ZRJO04': '552182745000',
    'ZRJO05': '552182740000',
    'ZRJO06': '552182365100',
    # Minas Gerais (3x)
    'ZCEM01': '553193099000',
    'ZCEM02': '553175450000',
    'ZCEM03': '553191930500',
    'ZBHE04': '553191930400',
    'ZBHE05': '553191938700',
    # Parana (4x)
    'ZFNS03': '554799133900',
    'ZFNS04': '554896660000',
    'ZCTA05': '554199132500',
    'ZCTA07': '554195049000',
    # Rio Grande do Sul (5x)
    'ZPAE02': '555183070000',
    'ZPAE03': '555181138600',
    # Goias / Brasilia (6x)
    'ZGNA01': '556281138800',
    'ZBSA01': '556181138800',
    'ZBSA04': '556181136000',
    # Bahia (7x)
    'ZSDR04': '557191930000',
    'ZSDR02': '557191934000',
    'ZSDR06': '557191931800',
    # Area 8x
    'ZRCE03': '558199239000',
    'ZRCE09': '558398190000',
    'ZRCE10': '558198761700',
    'ZNTL02': '558499239000',
    'ZFLA04': '558599235600',
    # Area 9x
    'ZITZ01': '559981060000',
    'ZBVA01': '559581148500',
    'ZMPA01': '559681228800',
    'ZSLS02': '559881500800',
    'ZSLS03': '559881119000',
    'ZBLM04': '559189100000',
    'ZBLM05': '559189518200',
    # Manaus (92 e 97)
    'ZMNS01': '559281117800',
    'ZMNS02': '559281116000'
}

# TODO Complete srvcc_msc Dictionary
srvcc_msc = {'11': ['ZSNE08'],
             '12': ['ZSNE07'],
             '13': ['ZSNE07'],
             '14': ['ZSNE03'],
             '15': ['ZSNE03'],
             '16': ['ZSPO02'],
             '17': ['ZSPO05'],
             '18': ['ZSNE10'],
             '19': ['ZSNE10'],
             '21': ['ZRJO04', 'ZRJO05', 'ZRJO06'],
             '22': ['ZRJO04', 'ZRJO05', 'ZRJO06'],
             '24': ['ZRJO04', 'ZRJO05', 'ZRJO06'],
             '27': ['ZRJO04', 'ZRJO05', 'ZRJO06'],
             '28': ['ZRJO04', 'ZRJO05', 'ZRJO06'],
             '31': ['ZBHE05'],
             '32': ['ZBHE05'],
             '33': ['ZCEM03'],
             '34': ['ZBHE05'],
             '35': ['ZBHE05'],
             '37': ['ZCEM03'],
             '38': ['ZBHE05'],
             '41': ['ZCTA07'],
             '42': ['ZCTA07'],
             '43': ['ZCTA07'],
             '44': ['ZCTA07'],
             '45': ['ZCTA07'],
             '46': ['ZCTA07'],
             '47': ['ZFNS04'],
             '48': ['ZFNS04'],
             '49': ['ZFNS04'],
             '51': ['ZPAE03'],
             '53': ['ZPAE02'],
             '54': ['ZPAE03'],
             '55': ['ZPAE02'],
             '61': ['ZBSA04', 'ZGNA01'],
             '62': ['ZBSA04', 'ZGNA01'],
             '63': ['ZBSA04', 'ZGNA01'],
             '64': ['ZBSA04', 'ZGNA01'],
             '65': ['ZBSA04', 'ZGNA01'],
             '66': ['ZBSA04', 'ZGNA01'],
             '67': ['ZBSA04', 'ZGNA01'],
             '68': ['ZBSA04', 'ZGNA01'],
             '69': ['ZBSA04', 'ZGNA01'],
             '71': ['ZSDR04'],
             '73': ['ZSDR06'],
             '74': ['ZSDR04'],
             '75': ['ZSDR04'],
             '77': ['ZSDR06'],
             '79': ['ZSDR04'],
             '81': ['ZRCE10', 'ZFLA05'],
             '82': ['ZRCE10', 'ZFLA05'],
             '83': ['ZRCE10', 'ZFLA05'],
             '84': ['ZRCE10', 'ZFLA05'],
             '85': ['ZRCE10', 'ZFLA05'],
             '86': ['ZRCE10', 'ZFLA05'],
             '87': ['ZRCE10', 'ZFLA05'],
             '88': ['ZRCE10', 'ZFLA05'],
             '89': ['ZRCE10', 'ZFLA05'],
             '91': ['ZBLM05'],
             '92': ['ZMNS02'],
             '93': ['ZBLM05'],
             '94': ['ZBLM05'],
             '95': ['ZBVA01'],
             '96': ['ZMPA01'],
             '97': ['ZMNS02'],
             '98': ['ZSLS03'],
             '99': ['ZSLS03']
             }

vlr_anf = {'11': 'ZSNE08',
           '12': 'ZSNE07',
           '13': 'ZSNE07',
           '14': 'ZSNE03',
           '15': 'ZSNE03',
           '16': 'ZSPO02',
           '17': 'ZSPO05',
           '18': 'ZSNE10',
           '19': 'ZSNE10',
           '21': 'ZRJO04',
           '22': 'ZRJO06',
           '24': 'ZRJO05',
           '27': 'ZRJO06',
           '28': 'ZRJO04',
           '31': 'ZBHE05',
           '32': 'ZBHE05',
           '33': 'ZCEM03',
           '34': 'ZBHE05',
           '35': 'ZBHE05',
           '37': 'ZCEM03',
           '38': 'ZBHE05',
           '41': 'ZCTA07',
           '42': 'ZCTA07',
           '43': 'ZCTA07',
           '44': 'ZCTA07',
           '45': 'ZCTA07',
           '46': 'ZCTA07',
           '47': 'ZFNS04',
           '48': 'ZFNS04',
           '49': 'ZFNS04',
           '51': 'ZPAE03',
           '53': 'ZPAE02',
           '54': 'ZPAE03',
           '55': 'ZPAE02',
           '61': 'ZBSA04',
           '62': 'ZGNA01',
           '63': 'ZBSA04',
           '64': 'ZGNA01',
           '65': 'ZGNA01',
           '66': 'ZBSA04',
           '67': 'ZGNA01',
           '68': 'ZBSA04',
           '69': 'ZBSA04',
           '71': 'ZSDR04',
           '73': 'ZSDR06',
           '74': 'ZSDR04',
           '75': 'ZSDR04',
           '77': 'ZSDR06',
           '79': 'ZSDR04',
           '81': 'ZRCE10',
           '82': 'ZRCE10',
           '83': 'ZRCE10',
           '84': 'ZRCE10',
           '85': 'ZFLA05',
           '86': 'ZFLA04',
           '87': 'ZRCE10',
           '88': 'ZFLA05',
           '89': 'ZFLA04',
           '91': 'ZBLM05',
           '92': 'ZMNS02',
           '93': 'ZBLM05',
           '94': 'ZBLM05',
           '95': 'ZBVA01',
           '96': 'ZMPA01',
           '97': 'ZMNS02',
           '98': 'ZSLS03',
           '99': 'ZSLS03'
           }

bayface = {
    'DMBHE1': {'0': ['5', '10', '11'], '1': ['0', '10', '11']},
    'DMSDR1': {'0': ['5', '10', '11'], '1': ['0', '10', '11']},
    'DMBLM1': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10']},
    'DMRCE1': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMCTA1': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMBSA1': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMMNS1': [],  # DMMNS1 uses ECU boards, the scripts are not ready to treat such boards
    'DMBHE2': {'0': ['1', '4', '10'], '1': ['1', '4', '10']},
    'DMSDR2': {'0': ['1', '4', '10'], '1': ['1', '4', '10']},
    'DMBLM2': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '10']},
    'DMRCE2': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMCTA2': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10']},
    'DMBSA2': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10']},
    'DMSNE3': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMSNE4': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMSPO1': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMSPO2': {'0': ['1', '4', '5', '10', '11'], '1': ['0', '1', '4', '10', '11']},
    'DMRJO3': {'0': ['1', '4', '10'], '1': ['0', '1', '10']},
    'DMRJO4': {'0': ['1', '4', '10'], '1': ['0', '1', '10']}
}

nsei_start_number = {
    'DMBHE1': ['1', '2'],
    'DMSDR1': ['3', '4'],
    'DMRCE1': ['1', '2'],
    'DMBLM1': ['3', '4'],
    'DMCTA1': ['1', '2'],
    'DMBSA1': ['3', '4'],
    'DMMNS1': ['1', '2'],
    'DMBHE2': ['5', '6'],
    'DMSDR2': ['7', '8'],
    'DMRCE2': ['5', '6'],
    'DMBLM2': ['7', '8'],
    'DMCTA2': ['5', '6'],
    'DMBSA2': ['7', '8'],
    'DMSNE3': ['1', '2'],
    'DMSNE4': ['3', '4'],
    'DMSPO1': ['5', '6'],
    'DMSPO2': ['7', '8'],
    'DMRJO3': ['1', '2'],
    'DMRJO4': ['3', '4']
}

slsm_map = {
    1: 'B0000',
    2: 'B0001',
    3: 'B0011',
    4: 'B0011',
    5: 'B0111',
    6: 'B0111',
    7: 'B0111',
    8: 'B0111',
    9: 'B1111',
    10: 'B1111',
    11: 'B1111',
    12: 'B1111',
    13: 'B1111',
    14: 'B1111',
    15: 'B1111',
    16: 'B1111'
}

add_resrec = 'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
             'DOMAIN="tac-lb{tac_lb}.tac-hb{tac_hb}.tac", ORDER={order}, PREF=10, FLAGS=A, SERVICE="{service}", ' \
             'REPLACEMENT="topoff.vip-{interface}.{node_name}.node.epc.mnc{mnc}.mcc724.3gppnetwork.org.", ' \
             'VIEWNAME="{view_name}";'

rmv_resrec = 'RMV RESREC: TYPE=NAPTR, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
             'DOMAIN="tac-lb{tac_lb}.tac-hb{tac_hb}.tac", NAPTRSWITCH=ON, ORDER={order}, PREF=10, ' \
             'VIEWNAME="{view_name}", FLAGS=A, SERVICE="{service}", ' \
             'REPLACEMENT="topoff.vip-{interface}.{node_name}.node.epc.mnc{mnc}.mcc724.3gppnetwork.org.";'

add_apn_resrec_naptr_s5s8 = 'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
                            'DOMAIN="{apn}.apn", ORDER=10, PREF=10, FLAGS=A, ' \
                            'SERVICE="x-3gpp-pgw:x-s5-gtp:x-gn", ' \
                            'REPLACEMENT="topoff.vip-s5.{node_name}.node.epc.mnc' \
                            '{replacement_mnc}.mcc724.3gppnetwork.org.", ' \
                            'VIEWNAME="{view_name}";'

add_apn_resrec_a_s5s8 = 'ADD RESREC: TYPE=A, ZONE="mnc{mnc}.mcc724.gprs", DOMAIN="{domain_name}", IP="{node_ip}", ' \
                        'VIEWNAME="{view_name}";'

add_node_resrec_a = 'ADD RESREC: TYPE=A, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
                    'DOMAIN="topoff.vip-{interface}.{node_name}.node", IP="{node_ip}", ' \
                    'VIEWNAME="{view_name}";'

add_node_resrec_naptr_s11 = 'ADD RESREC: TYPE=NAPTR, ZONE="epc.mnc{mnc}.mcc724.3gppnetwork.org", ' \
                            'DOMAIN="{node_name}.node", ORDER=10, PREF=10, FLAGS=A, ' \
                            'SERVICE="x-3gpp-sgw:x-s11:x-s5-gtp", ' \
                            'REPLACEMENT="topoff.vip-s11.{node_name}.node.epc.mnc{replacement_mnc}.' \
                            'mcc724.3gppnetwork.org.", ' \
                            'VIEWNAME="{view_name}";'

add_m3de = 'ADD M3DE: DEX={DEX}, LEX={LEX}, DPC="{DPC}", DET={DET}, DEN="{RNC_Name}";'

add_m3lks = 'ADD M3LKS: LSX={LSX}, DEX={DEX}, WM={DET}, TM={Share_Type}, LSN="{RNC_Name}", SLSM={SLSM};'

add_m3rt = 'ADD M3RT: RTX={RTX}, DEX={DEX}, LSX={LSX}, RTN="{RNC_Name}";'

add_m3lnk = 'ADD M3LNK: LNK={LNK}, VPNNAME="SIG", IPT=IPV4, LOCIPV41="{LOCIPV41}", ' \
            'LOCIPV42="{LOCIPV42}", LOCPORT={LOCPORT}, PEERIPV41="{PEERIPV41}", ' \
            'PEERIPV42="{PEERIPV42}", PEERPORT={PEERPORT}, CS=S, LSX={LSX}, CONSTHD=80, CONETHD=40, SCTPINDX=0, LKN="{RNC_Name}";'

add_sccpdpc = 'ADD SCCPDPC: DPX={DPX}, OPX={OPX}, DPC="{DPC}", LDP=NOUSE, DPN="{RNC_Name}";'

add_sccpssn = 'ADD SCCPSSN: SSNX={SSNX}, SSN={SSN}, NI=NATB, DPC="{DPC}", OPC="{OPC}", SSNNAME="{RNC_Name}";'

add_rnc = 'ADD RNC: RNCX={RNCX}, RNCN="{RNC_Name}", RNCMCC="{RNCMCC}", RNCMNC="{RNCMNC}", RNCID={RNCINDEX}, ' \
          'NI={NI}, SPC="{DPC}", IMS=YES, IU-FLEX={Iu_Flex}, RANSHR={RanSharing}, UESBI=NO, RNCVER=R7, OTS={DT}, ' \
          'R7QOS={R7_QOS}, RABQOS={RAB_QOS}, ALTBRTYPE=VALUERANGE, CHGSYMTOASYMBI=NO, SGSNBUF=NO;'

add_rnc_r7 = 'ADD RNC: RNCX={RNCX}, RNCN="{RNC_Name}", RNCMCC="{RNCMCC}", RNCMNC="{RNCMNC}",' \
             ' RNCID={RNCINDEX}, NI={NI}, SPC="{DPC}", IMS=YES, IU-FLEX={Iu_Flex}, RANSHR={RanSharing}, RNCVER=R7, ' \
             'OTS={DT}, R7QOS={R7_QOS}, RABQOS={RAB_QOS}, ALTBRTYPE=VALUERANGE, CHGSYMTOASYMBI=NO, SGSNBUF=NO;'

add_iupaging = 'ADD IUPAGING: LAI="{LAI}", RAC="{RAC}", RNCINDEX={RNCX};'

add_rac_cname = 'ADD RESREC: TYPE=CNAME, ZONE="MNC{MNC}.MCC724.GPRS", VIEWNAME="{view_name}", ' \
                'DOMAINCNAME="RAC00{RAC}.LAC{LAC}.MNC{MNC}.MCC724.GPRS.", ' \
                'ORIGINALDOMAINNAME="{SGSN}.MNC{MNC}.MCC724.GPRS.";'

add_nri_cname = 'ADD RESREC: TYPE=CNAME, ZONE="MNC{MNC}.MCC724.GPRS", VIEWNAME="{view_name}", ' \
                'DOMAINCNAME="NRI00{NRI}.RAC00{RAC}.LAC{LAC}.MNC{MNC}.MCC724.GPRS.", ' \
                'ORIGINALDOMAINNAME="{SGSN}.MNC{MNC}.MCC724.GPRS.";'

rmv_rac_cname = 'RMV RESREC: TYPE=CNAME, ZONE="MNC{MNC}.MCC724.GPRS", VIEWNAME="{view_name}", ' \
                'DOMAINCNAME="RAC00{RAC}.LAC{LAC}.MNC{MNC}.MCC724.GPRS.";'

rmv_nri_cname = 'RMV RESREC: TYPE=CNAME, ZONE="MNC{MNC}.MCC724.GPRS", VIEWNAME="{view_name}", ' \
                'DOMAINCNAME="NRI00{NRI}.RAC00{RAC}.LAC{LAC}.MNC{MNC}.MCC724.GPRS.";'

add_nse = 'ADD NSE: OTHERNODE="{BSC_Name}", NSEI={nsei}, SRN={srn}, SN={sn}, ' \
          'BSSID={nsei}, PFC=YES, BT={tx}, CT={NSE_Type}, GB-FLEX={GB_Flex};'

add_gbiplocendpt = 'ADD GBIPLOCENDPT: SRN={srn}, SN={sn}, NSEI={nsei}, IPT=IPV4, ' \
                   'LIPV4="{LIPV4}", LUP={LOCALPORT}, DESC="{BSC_Name}";'

rmv_nse = 'RMV NSE: OTHERNODE="{BSC_Name}";'

rmv_gbiplocendpt = 'RMV GBIPLOCENDPT: NSEI={nsei}, IPT=IPV4, LIPV4="{LIPV4}", LUP={LOCALPORT};'
