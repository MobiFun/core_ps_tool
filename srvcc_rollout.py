import json
from support_variables import mnc_select, srvcc_msc


def srvcc_entries(lac_list):
    create_naptrrecord_f5 = list()
    for lac in lac_list:
        for msc in srvcc_msc.get(lac[-2:]):
            mnc = mnc_select.get(lac[-2:-1])
            create_naptrrecord_f5.append({
                'action': 'add',
                'domain_name': 'lac{LAC}.lac.epc.mnc{mnc}.mcc724.3gppnetwork.org.'.format(
                    LAC=format(int(lac), '04x').upper(),
                    mnc=mnc
                ),
                'order': 10,
                'preference': 10,
                'flags': 'A',
                'service': 'x-3gpp-msc:x-sv',
                'regexp': '""',
                'replacement': 'topoff.vip-sv.{node_name}.node.epc.mnc{mnc}.mcc724.3gppnetwork.org.'.format(
                    node_name=msc,
                    mnc=mnc
                ),
                'ttl': 300}
            )
    result = [json.dumps(a) for a in create_naptrrecord_f5]
    return result


def create_lac_list(f):
    lac_list = list()
    with open(f, 'r') as fin:
        for line in fin:
            lac_list.append(line.strip())

    return lac_list


def export_config(a, result):
    with open(a, 'wb') as fout:
        for line in result:
            fout.write(line + '\n')


def main():
    f = raw_input("Arquivo de LACs: ")
    a = raw_input("Nome do Projeto: ")

    lac_list = create_lac_list(f)
    result = srvcc_entries(lac_list)
    export_config(a, result)


if __name__ == "__main__":
    main()
