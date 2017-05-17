# coding=utf-8
'''
Versao 2

Data 24-01-2017
'''
try:
    import bigsuds
except:
    print("Install bigsuds library via pip, e.g. pip install bigsuds.")
    input()

import getpass
import json
import datetime
import re

a_records = []
a_records_delete = []
naptr_records = []
naptr_records_delete = []
domain_pattern = ".+?(?=\.epc)|.+?(?=\.mnc)"
zone_pattern = "\.mnc.+|\.epc.+"


def flush_configuration_naptr(b, view_name):
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

    if len(naptr_records) != 0:

        mnc_02_org = [dicts for dicts in naptr_records
                      if dicts.get("domain_name").endswith("mnc002.mcc724.3gppnetwork.org.")]
        mnc_03_org = [dicts for dicts in naptr_records
                      if dicts.get("domain_name").endswith("mnc003.mcc724.3gppnetwork.org.")]
        mnc_04_org = [dicts for dicts in naptr_records
                      if dicts.get("domain_name").endswith("mnc004.mcc724.3gppnetwork.org.")]

        mnc_02 = [dicts for dicts in naptr_records
                  if dicts.get("domain_name").endswith("mnc002.mcc724.gprs.")]
        mnc_03 = [dicts for dicts in naptr_records
                  if dicts.get("domain_name").endswith("mnc003.mcc724.gprs.")]
        mnc_04 = [dicts for dicts in naptr_records
                  if dicts.get("domain_name").endswith("mnc004.mcc724.gprs.")]

        if len(mnc_02_org) != 0:
            b.Management.ResourceRecord.add_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc002.mcc724.3gppnetwork.org."}],
                naptr_records=[mnc_02_org]
            )
        if len(mnc_03_org) != 0:
            b.Management.ResourceRecord.add_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc003.mcc724.3gppnetwork.org."}],
                naptr_records=[mnc_03_org]
            )

        if len(mnc_04_org) != 0:
            b.Management.ResourceRecord.add_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc004.mcc724.3gppnetwork.org."}],
                naptr_records=[mnc_04_org]
            )

        if len(mnc_02) != 0:
            b.Management.ResourceRecord.add_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "mnc002.mcc724.gprs."}],
                naptr_records=[mnc_02]
            )
        if len(mnc_03) != 0:
            b.Management.ResourceRecord.add_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "mnc003.mcc724.gprs."}],
                naptr_records=[mnc_03]
            )

        if len(mnc_04) != 0:
            b.Management.ResourceRecord.add_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "mnc004.mcc724.gprs."}],
                naptr_records=[mnc_04]
            )

    if len(naptr_records_delete) != 0:

        mnc_02_org_delete = [dicts for dicts in naptr_records_delete
                             if dicts.get("domain_name").endswith("mnc002.mcc724.3gppnetwork.org.")]
        mnc_03_org_delete = [dicts for dicts in naptr_records_delete
                             if dicts.get("domain_name").endswith("mnc003.mcc724.3gppnetwork.org.")]
        mnc_04_org_delete = [dicts for dicts in naptr_records_delete
                             if dicts.get("domain_name").endswith("mnc004.mcc724.3gppnetwork.org.")]

        mnc_02_delete = [dicts for dicts in naptr_records_delete
                         if dicts.get("domain_name").endswith("mnc002.mcc724.gprs.")]
        mnc_03_delete = [dicts for dicts in naptr_records_delete
                         if dicts.get("domain_name").endswith("mnc003.mcc724.gprs.")]
        mnc_04_delete = [dicts for dicts in naptr_records_delete
                         if dicts.get("domain_name").endswith("mnc004.mcc724.gprs.")]

        if len(mnc_02_org_delete) != 0:
            b.Management.ResourceRecord.delete_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc002.mcc724.3gppnetwork.org."}],
                naptr_records=[mnc_02_org_delete]
            )
        if len(mnc_03_org_delete) != 0:
            b.Management.ResourceRecord.delete_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc003.mcc724.3gppnetwork.org."}],
                naptr_records=[mnc_03_org_delete]
            )

        if len(mnc_04_org_delete) != 0:
            b.Management.ResourceRecord.delete_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc004.mcc724.3gppnetwork.org."}],
                naptr_records=[mnc_04_org_delete]
            )

        if len(mnc_02_delete) != 0:
            b.Management.ResourceRecord.delete_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "mnc002.mcc724.gprs."}],
                naptr_records=[mnc_02_delete]
            )
        if len(mnc_03_delete) != 0:
            b.Management.ResourceRecord.delete_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "mnc003.mcc724.gprs."}],
                naptr_records=[mnc_03_delete]
            )

        if len(mnc_04_delete) != 0:
            b.Management.ResourceRecord.delete_naptr(
                view_zones=[{"view_name": view_name, "zone_name": "mnc004.mcc724.gprs."}],
                naptr_records=[mnc_04_delete]
            )


def flush_configuration_a(b, view_name):
    """This function is used to flush all A Records configuration to the BIG-IP ZoneRunner App.
       The objects inside naptr_records looks like this:

        {"domain_name":"testp.tim.br.mnc003.mcc724.gprs.", "ip_address": "10.221.58.214", "ttl":300}
        {"domain_name":"testp.tim.br.mnc004.mcc724.gprs.", "ip_address": "10.221.58.214", "ttl":300}
        {"domain_name":"testp.tim.br.mnc002.mcc724.gprs.", "ip_address": "10.221.58.214", "ttl":300}

       For more information go to devcentral.f5.com and search for iControl API.
     """

    if len(a_records) != 0:

        mnc_02_org = [dicts for dicts in a_records
                      if dicts.get("domain_name").endswith("mnc002.mcc724.3gppnetwork.org.")]
        mnc_03_org = [dicts for dicts in a_records
                      if dicts.get("domain_name").endswith("mnc003.mcc724.3gppnetwork.org.")]
        mnc_04_org = [dicts for dicts in a_records
                      if dicts.get("domain_name").endswith("mnc004.mcc724.3gppnetwork.org.")]

        mnc_02 = [dicts for dicts in a_records
                  if dicts.get("domain_name").endswith("mnc002.mcc724.gprs.")]
        mnc_03 = [dicts for dicts in a_records
                  if dicts.get("domain_name").endswith("mnc003.mcc724.gprs.")]
        mnc_04 = [dicts for dicts in a_records
                  if dicts.get("domain_name").endswith("mnc004.mcc724.gprs.")]
        if len(mnc_02) != 0:
            b.Management.ResourceRecord.add_a(
                view_zones=[{"view_name": view_name, "zone_name": "mnc002.mcc724.gprs."}],
                a_records=[mnc_02],
                sync_ptrs=["false"]
            )
        if len(mnc_03) != 0:
            b.Management.ResourceRecord.add_a(
                view_zones=[{"view_name": view_name, "zone_name": "mnc003.mcc724.gprs."}],
                a_records=[mnc_03],
                sync_ptrs=["false"]
            )
        if len(mnc_04) != 0:
            b.Management.ResourceRecord.add_a(
                view_zones=[{"view_name": view_name, "zone_name": "mnc004.mcc724.gprs."}],
                a_records=[mnc_04],
                sync_ptrs=["false"]
            )
        if len(mnc_02_org) != 0:
            b.Management.ResourceRecord.add_a(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc002.mcc724.3gppnetwork.org."}],
                a_records=[mnc_02_org],
                sync_ptrs=["false"]
            )
        if len(mnc_03_org) != 0:
            b.Management.ResourceRecord.add_a(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc003.mcc724.3gppnetwork.org."}],
                a_records=[mnc_03_org],
                sync_ptrs=["false"]
            )
        if len(mnc_04_org) != 0:
            b.Management.ResourceRecord.add_a(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc004.mcc724.3gppnetwork.org."}],
                a_records=[mnc_04_org],
                sync_ptrs=["false"]
            )

    # Delete A Records

    if len(a_records_delete) != 0:

        mnc_02_org_delete = [dicts for dicts in a_records_delete
                             if dicts.get("domain_name").endswith("mnc002.mcc724.3gppnetwork.org.")]
        mnc_03_org_delete = [dicts for dicts in a_records_delete
                             if dicts.get("domain_name").endswith("mnc003.mcc724.3gppnetwork.org.")]
        mnc_04_org_delete = [dicts for dicts in a_records_delete
                             if dicts.get("domain_name").endswith("mnc004.mcc724.3gppnetwork.org.")]

        mnc_02_delete = [dicts for dicts in a_records_delete
                         if dicts.get("domain_name").endswith("mnc002.mcc724.gprs.")]
        mnc_03_delete = [dicts for dicts in a_records_delete
                         if dicts.get("domain_name").endswith("mnc003.mcc724.gprs.")]
        mnc_04_delete = [dicts for dicts in a_records_delete
                         if dicts.get("domain_name").endswith("mnc004.mcc724.gprs.")]

        if len(mnc_02_delete) != 0:
            b.Management.ResourceRecord.delete_a(
                view_zones=[{"view_name": view_name, "zone_name": "mnc002.mcc724.gprs."}],
                a_records=[mnc_02_delete],
                sync_ptrs=["false"]
            )
        if len(mnc_03_delete) != 0:
            b.Management.ResourceRecord.delete_a(
                view_zones=[{"view_name": view_name, "zone_name": "mnc003.mcc724.gprs."}],
                a_records=[mnc_03_delete],
                sync_ptrs=["false"]
            )

        if len(mnc_04_delete) != 0:
            b.Management.ResourceRecord.delete_a(
                view_zones=[{"view_name": view_name, "zone_name": "mnc004.mcc724.gprs."}],
                a_records=[mnc_04_delete],
                sync_ptrs=["false"]
            )
        if len(mnc_02_org_delete) != 0:
            b.Management.ResourceRecord.delete_a(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc002.mcc724.3gppnetwork.org."}],
                a_records=[mnc_02_org_delete],
                sync_ptrs=["false"]
            )
        if len(mnc_03_org_delete) != 0:
            b.Management.ResourceRecord.delete_a(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc003.mcc724.3gppnetwork.org."}],
                a_records=[mnc_03_org_delete],
                sync_ptrs=["false"]
            )
        if len(mnc_04_org_delete) != 0:
            b.Management.ResourceRecord.delete_a(
                view_zones=[{"view_name": view_name, "zone_name": "epc.mnc004.mcc724.3gppnetwork.org."}],
                a_records=[mnc_04_org_delete],
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
                        if regex.lower() in records or regex.upper() in records:
                            f.write(records + "\n")
                            records_data.append(records)
            else:
                for records in rrs:
                    if regex.lower() in records or regex.upper() in records:
                        records_data.append(records)
    return records_data


def extract_records(arquivo_input):
    global a_records
    global a_records_delete
    global naptr_records
    global naptr_records_delete
    arquivos = []
    for arquivo in arquivo_input:
        try:
            if arquivo.lower().endswith('add.txt'):
                with open(arquivo, "r") as resrec:
                    for lines in resrec:
                        if lines.strip():
                            if json.loads(lines).get("replacement"):
                                naptr_records.append(json.loads(lines))
                            else:
                                a_records.append(json.loads(lines))
            elif arquivo.lower().endswith('remove.txt'):
                with open(arquivo, "r") as resrec:
                    for lines in resrec:
                        if lines.strip():
                            if json.loads(lines).get("replacement"):
                                naptr_records_delete.append(json.loads(lines))
                            else:
                                a_records_delete.append(json.loads(lines))
            else:
                arquivos.append(arquivo)
        except Exception, e:
            return arquivos, e



def main_cvna_f5_app_main():
    global a_records
    global a_records_delete
    global naptr_records
    global naptr_records_delete

    print("\nBem vindo a ferramenta de CVNA do BIG-IP F5\n"
          "Por favor, insira as infos abaixo para obter acesso ao BIG-IP:\n"
          )
    hostname = raw_input("Digite o IP do Big-IP: ")
    username = raw_input("Usuario: ")
    password = getpass.getpass('Senha: ')
    b = bigsuds.BIGIP(

        hostname=hostname,
        username=username,
        password=password
    )
    while True:
        print("\nEscolha uma das opções abaixo para prosseguir:")
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
                        print(r+'\n')
                except Exception as err:
                    print("Encontramos um erro. Reporte-o ao desenvolvedor (decastromonteiro@gmail.com).")
                    print(err)
                    raw_input()

        elif choose_action == "2":

            view_name = raw_input("Escreva o nome da view que deseja configurar: ")
            arquivo_input = raw_input("Escreva os nomes dos arquivos de input, utilizando ponto e virgula (;) "
                                      "como separador: ").split(";")
            try:
                extract_records(arquivo_input)
                if (not a_records and not naptr_records) and (not a_records_delete and not naptr_records_delete):
                    print("Não foi possível extrair nenhuma configuração dos arquivos: {}".format(
                        arquivo_input
                    ))
                    print("Verifique o conteúdo dos arquivos e tente novamente.")
                    continue
                flush_configuration_naptr(b, view_name)
                flush_configuration_a(b, view_name)
                print("Configuracoes concluidas com sucesso!")
                group_of_domains = []
                group_of_domains_to_remove = []

                if a_records:
                    for i in xrange(len(a_records)):
                        domain = re.search(domain_pattern, [dicts.get("domain_name") for dicts in a_records][i])
                        group_of_domains.append(domain.group())
                    group_of_domains = set(group_of_domains)
                elif naptr_records:
                    for i in xrange(len(naptr_records)):
                        domain = re.search(domain_pattern, [dicts.get("domain_name") for dicts in naptr_records][i])
                        group_of_domains.append(domain.group())
                    group_of_domains = set(group_of_domains)

                if a_records_delete:
                    for i in xrange(len(a_records_delete)):
                        domain = re.search(domain_pattern, [dicts.get("domain_name") for dicts in a_records_delete][i])
                        group_of_domains_to_remove.append(domain.group())
                    group_of_domains_to_remove = set(group_of_domains_to_remove)
                elif naptr_records_delete:
                    for i in xrange(len(naptr_records_delete)):
                        domain = re.search(domain_pattern, [dicts.get("domain_name") for dicts in naptr_records_delete][i])
                        group_of_domains_to_remove.append(domain.group())
                    group_of_domains_to_remove = set(group_of_domains_to_remove)

                for domain in group_of_domains:
                    new_entries = gather_dns_records(b, regex=domain, view_name=view_name, zone_name="",
                                                     export="")
                    if new_entries:
                        print("\nSeguem as entradas configuradas com domain '{}':\n".format(domain))
                        for entries in new_entries:
                            print(entries + '\n')
                    else:
                        print("Nao existem entradas com domain '{}'".format(domain))

                for domain in group_of_domains_to_remove:
                    new_entries = gather_dns_records(b, regex=domain, view_name=view_name, zone_name="",
                                                     export="")
                    if new_entries:
                        print("\nSeguem as entradas configuradas com domain '{}':\n".format(domain))
                        for entries in new_entries:
                            print(entries + '\n')
                    else:
                        print("Nao existem entradas com domain '{}'".format(domain))

            except Exception as err:
                print("Encontramos um erro. Reporte-o ao desenvolvedor (decastromonteiro@gmail.com).")
                print(err)
                raw_input()

            a_records = []
            a_records_delete = []
            naptr_records = []
            naptr_records_delete = []

        elif choose_action == "3":
            print("Obrigado por utilizar a ferramenta de CVNA do BIG-IP F5!")
            raw_input()
            break


if __name__ == "__main__":
    main_cvna_f5_app_main()
