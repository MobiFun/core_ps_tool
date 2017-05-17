# coding=utf-8
#####################################################
#                    Versao 3                       #
#                                                   #
#                 Data 25-01-2017                   #
#                                                   #
#            Autor: Leonardo Monteiro               #
#      E-mail: decastromonteiro@gmail.com           #
#                                                   #
#####################################################
try:
    import bigsuds
except:
    print("Install bigsuds library via pip, e.g. pip install bigsuds.")
    input()

import getpass
import json
import datetime
import re
from collections import namedtuple

domain_pattern = ".+?(?=\.epc)|.+?(?=\.mnc)"
zone_pattern = "\mnc.+|\epc.+"
list_to_string_pattern = r"\'|\,|\[|\]|"


def flush_configuration_naptr(b, view_name, naptr_records, naptr_records_delete):
    """This function is used to flush all NAPTR Records configuration to the BIG-IP ZoneRunner App.
       The objects inside naptr_records looks like this:

        {"service": "x-3gpp-mme:x-gn:x-s10",
        "domain_name": "tac-lb25.tac-hb8E.tac.epc.mnc004.mcc724.3gppnetwork.org.",
        "flags": "a", "preference": 10,
        "ttl": 300, "regexp": "''", "order": 10,
        "replacement": "topoff.vip-gn.DMBSA1.node.epc.mnc004.mcc724.3gppnetwork.org."},

        {"service": "x-3gpp-mme:x-gn:x-s10",
        "domain_name": "tac-lb25.tac-hb8E.tac.epc.mnc004.mcc724.3gppnetwork.org.",
        "flags": "a", "preference": 10, "ttl": 300, "regexp": "''", "order": 10,
        "replacement": "topoff.vip-gn.DMCTA1.node.epc.mnc004.mcc724.3gppnetwork.org."},

        {"service": "x-3gpp-sgw:x-s11:x-s5-gtp",
        "domain_name": "tac-lb1A.tac-hb7A.tac.epc.mnc004.mcc724.3gppnetwork.org.",
        "flags": "a", "preference": 10, "ttl": 300, "regexp": "''", "order": 10,
        "replacement": "topoff.vip-s11.GPCTA1.node.epc.mnc004.mcc724.3gppnetwork.org."}

       For more information go to devcentral.f5.com and search for iControl API.
    """

    # Add NAPTR Records

    if len(naptr_records) != 0:

        for records in naptr_records:
            b.Management.ResourceRecord.add_naptr(
                view_zones=[{"view_name": view_name, "zone_name": re.search(zone_pattern, records.get(
                    "domain_name")).group()}],
                naptr_records=[[records]],
            )
    # Delete NAPTR Records

    if len(naptr_records_delete) != 0:

        for records in naptr_records_delete:
            b.Management.ResourceRecord.delete_naptr(
                view_zones=[{"view_name": view_name, "zone_name": re.search(zone_pattern, records.get(
                    "domain_name")).group()}],
                naptr_records=[[records]],
            )


def flush_configuration_a(b, view_name, a_records, a_records_delete):
    """This function is used to flush all A Records configuration to the BIG-IP ZoneRunner App.
       The objects inside naptr_records looks like this:

        {"domain_name":"testp.tim.br.mnc003.mcc724.gprs.", "ip_address": "10.221.58.214", "ttl":300}
        {"domain_name":"testp.tim.br.mnc004.mcc724.gprs.", "ip_address": "10.221.58.214", "ttl":300}
        {"domain_name":"testp.tim.br.mnc002.mcc724.gprs.", "ip_address": "10.221.58.214", "ttl":300}

       For more information go to devcentral.f5.com and search for iControl API.
     """

    # Add A Records

    if len(a_records) != 0:

        for records in a_records:
            b.Management.ResourceRecord.add_a(
                view_zones=[{"view_name": view_name, "zone_name": re.search(zone_pattern, records.get(
                    "domain_name")).group()}],
                a_records=[[records]],
                sync_ptrs=["false"]
            )

    # Delete A Records

    if len(a_records_delete) != 0:

        for records in a_records_delete:
            b.Management.ResourceRecord.delete_a(
                view_zones=[{"view_name": view_name, "zone_name": re.search(zone_pattern, records.get(
                    "domain_name")).group()}],
                a_records=[[records]],
                sync_ptrs=["false"]
            )


def gather_dns_records(b, regex, view_name, zone_name, export):
    now = datetime.datetime.now()
    date = '{}-{}-{}_{}-{}-{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)
    records_data = []
    for rrs in b.Management.ResourceRecord.get_rrs(
            view_zones=[{"view_name": view_name, "zone_name": zone_name  # example: "mnc002.mcc724.3gppnetwork.org."
                         }]):
        if regex.strip() == "":
            if export.lower() == "s":
                with open(view_name + "_{}_{}.txt".format(zone_name, date), "wb") as f:
                    for records in rrs:
                        f.write(records + "\n")
                        records_data.append(records)
            else:
                for records in rrs:
                    records_data.append(records)
        else:
            if export.lower() == "s":
                with open(view_name + "_{}_{}.txt".format(zone_name, date), "wb") as f:
                    for records in rrs:
                        if regex.lower() in records or regex.upper() in records or regex in records:
                            f.write(records + "\n")
                            records_data.append(records)
            else:
                for records in rrs:
                    if regex.lower() in records or regex.upper() in records or regex in records:
                        records_data.append(records)
    return records_data


def extract_records(arquivo_input):
    RecordCollection = namedtuple('Records', 'a_records a_records_delete naptr_records naptr_records_delete arquivos')
    result = RecordCollection(a_records=[], a_records_delete=[], naptr_records=[], naptr_records_delete=[],
                              arquivos=[])
    for arquivo in arquivo_input:
        if arquivo.strip().lower().endswith('add.txt'):
            with open(arquivo, "r") as resrec:
                for lines in resrec:
                    if lines.strip():
                        if json.loads(lines).get("replacement"):
                            result.naptr_records.append(json.loads(lines))
                        else:
                            result.a_records.append(json.loads(lines))
        elif arquivo.strip().lower().endswith('remove.txt'):
            with open(arquivo, "r") as resrec:
                for lines in resrec:
                    if lines.strip():
                        if json.loads(lines).get("replacement"):
                            result.naptr_records_delete.append(json.loads(lines))
                        else:
                            result.a_records_delete.append(json.loads(lines))
        else:
            result.arquivos.append(arquivo)

    return result


def evolved_extract_records(arquivo_input):
    RecordCollection = namedtuple('Records', 'a_records a_records_delete naptr_records naptr_records_delete bad_entries')
    result = RecordCollection(a_records=[], a_records_delete=[], naptr_records=[], naptr_records_delete=[],
                              bad_entries=[])
    for arquivo in arquivo_input:
        with open(arquivo, "r") as resrec:
            for lines in resrec:
                if lines.strip():
                    lines = json.loads(lines)
                    if lines.get("replacement"):
                        if lines.pop("action").lower() == "add":
                            result.naptr_records.append(lines)
                        elif lines.pop("action").lower() == "remove":
                            result.naptr_records_delete.append(lines)
                        else:
                            result.bad_entries.append(lines)
                    else:
                        if lines.pop("action").lower() == "add":
                            result.a_records.append(lines)
                        elif lines.pop("action").lower() == "remove":
                            result.a_records_delete.append(lines)
                        else:
                            result.bad_entries.append(lines)

    return result


def main_cvna_f5_app_main():
    print("\nBem vindo a ferramenta de CVNA do BIG-IP F5\n"
          "Por favor, insira as infos abaixo para obter acesso ao BIG-IP:\n"
          )
    hostname = raw_input("Digite o IP do Big-IP: ")
    username = raw_input("Usuario: ")
    password = getpass.getpass('Senha: ')
    b = bigsuds.BIGIP(

        hostname=hostname.strip(),
        username=username.strip(),
        password=password.strip()
    )
    while True:
        print("\nEscolha uma das opcoes abaixo para prosseguir:")
        print("1: Consultar zona no DNS\n"
              "2: Criar/Remover Entradas no DNS\n"
              "3: Sair\n"
              )

        choose_action = raw_input("> ")
        if choose_action == "1":
            view_name = raw_input("Digite o nome da view que deseja consultar: ")
            zone_name = raw_input("Digite o nome da zona que deseja consultar: ")
            regex = raw_input("Digite um nome especifico que deseja consultar dentro da zona: ")
            export = raw_input("Deseja exportar as respostas para um arquivo? (s\\n): ")
            if export.lower() == "s":
                print("Consultando o DNS...")
                try:
                    gather_dns_records(b, regex, view_name, zone_name, export)
                    now = datetime.datetime.now()
                    date = '{}-{}-{}_{}-{}-{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)
                    print("Foi gerado o arquivo {}_{}".format(view_name, zone_name + "_{}".format(date)))
                except Exception as err:
                    print("Encontramos um erro. Reporte-o ao desenvolvedor (decastromonteiro@gmail.com).")
                    print(err)
                    raw_input()
            else:
                print("Seguem as entradas recuperadas:\n")
                print("\n")
                try:
                    result = gather_dns_records(b, regex, view_name, zone_name, export)
                    for r in result:
                        print(r + '\n')
                except Exception as err:
                    print("Encontramos um erro. Reporte-o ao desenvolvedor (decastromonteiro@gmail.com).")
                    print(err)
                    raw_input()

        elif choose_action == "2":

            view_name = raw_input("Escreva o nome da view que deseja configurar: ")
            arquivo_input = raw_input("Escreva os nomes dos arquivos de input, utilizando ponto e virgula (;) "
                                      "como separador: ").split(";")
            try:

                records = extract_records(arquivo_input)

                if records.arquivos:
                    print('O(s) arquivo(s) {} esta(o) fora do padrao estabelecido. e. (_add.txt, _remove.txt)'.format(
                        records.arquivos
                    ))
                elif (not records.a_records and not records.naptr_records) and \
                        (not records.a_records_delete and not records.naptr_records_delete):

                    print("Nao foi possivel extrair nenhuma configuracao dos arquivos: {}".format(
                        arquivo_input
                    ))
                    print("Verifique o conteudo dos arquivos e tente novamente.")
                    continue
                flush_configuration_naptr(b, view_name, records.naptr_records, records.naptr_records_delete)
                flush_configuration_a(b, view_name, records.a_records, records.a_records_delete)
                print("Configuracoes concluidas com sucesso!")
                group_of_domains = []
                group_of_domains_to_remove = []

                if records.a_records:
                    for i in xrange(len(records.a_records)):
                        domain = re.search(domain_pattern, [dicts.get("domain_name") for dicts in records.a_records][i])
                        group_of_domains.append(domain.group())

                if records.naptr_records:
                    for i in xrange(len(records.naptr_records)):
                        domain = re.search(domain_pattern,
                                           [dicts.get("domain_name") for dicts in records.naptr_records][i])
                        group_of_domains.append(domain.group())

                group_of_domains = set(group_of_domains)

                if records.a_records_delete:
                    for i in xrange(len(records.a_records_delete)):
                        domain = re.search(domain_pattern,
                                           [dicts.get("domain_name") for dicts in records.a_records_delete][i])
                        group_of_domains_to_remove.append(domain.group())

                if records.naptr_records_delete:
                    for i in xrange(len(records.naptr_records_delete)):
                        domain = re.search(domain_pattern,
                                           [dicts.get("domain_name") for dicts in records.naptr_records_delete][i])
                        group_of_domains_to_remove.append(domain.group())
                group_of_domains_to_remove = set(group_of_domains_to_remove)

                evidence_list = list()

                if group_of_domains:
                    print("\nVerificacao das entradas configuradas:\n")

                    for domain in group_of_domains:
                        new_entries = gather_dns_records(b, regex=domain, view_name=view_name, zone_name="",
                                                         export="")
                        if new_entries:
                            evidence_list.append("\nSeguem as entradas configuradas com domain '{}':\n".format(domain))
                            print("\nSeguem as entradas configuradas com domain '{}':\n".format(domain))
                            for entries in new_entries:
                                print(entries + '\n')
                                evidence_list.append(entries)
                        else:
                            evidence_list.append("Nao existem entradas com domain '{}'".format(domain))
                            print("Nao existem entradas com domain '{}'".format(domain))
                if group_of_domains_to_remove:
                    print("\nVerificacao das entradas removidas:\n")
                    for domain in group_of_domains_to_remove:
                        new_entries = gather_dns_records(b, regex=domain, view_name=view_name, zone_name="",
                                                         export="")

                        if new_entries:
                            evidence_list.append("\nSeguem as entradas configuradas com domain '{}':\n".format(domain))
                            print("\nSeguem as entradas configuradas com domain '{}':\n".format(domain))
                            for entries in new_entries:
                                print(entries + '\n')
                                evidence_list.append(entries)
                        else:
                            evidence_list.append("Nao existem entradas com domain '{}'".format(domain))
                            print("Nao existem entradas com domain '{}'".format(domain))

                now = datetime.datetime.now()
                date = '{}-{}-{}_{}-{}-{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)
                file_name = "log_{}_{}.log".format(date,
                                                   re.sub(list_to_string_pattern, "", str(arquivo_input)).replace(
                                                       " ", "_"
                                                   ))
                with open(file_name, 'wb') as f:
                    f.write("""Data: {}/{}/{}\nHora: {}:{}:{}\nUsuario: {}\nArquivos Utilizados: {}\n\n""".format(
                        now.day, now.month, now.year, now.hour, now.minute, now.second, username, arquivo_input)
                    )
                    for evidence in evidence_list:
                        f.write(evidence + '\n')
                print("\nFoi gerado o log {}.\n".format(file_name))
            except Exception as err:
                print("Encontramos um erro. Reporte-o ao desenvolvedor (decastromonteiro@gmail.com).")
                print(err)
                raw_input()

        elif choose_action == "3":
            print("Obrigado por utilizar a ferramenta de CVNA do BIG-IP F5!")
            raw_input()
            break


if __name__ == "__main__":
    main_cvna_f5_app_main()
