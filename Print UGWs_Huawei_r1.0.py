# coding=utf-8
import paramiko
import os


# -----------------------------------------------------------------------------
# inicia uma sessão SSH
def ssh_session_UGW(UGW_name, UGW_ip):
    print "Conectando ao " + UGW_name

    if UGW_name == 'GPRJO3' or UGW_name == 'GPRJO4' or UGW_name == 'GPSPO3' or UGW_name == 'GPSNE1':
        UGW_senha = 'CNEPS@tim02'
    else:
        UGW_senha = 'CNEPS@tim01'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(UGW_ip, username='F8019834', password=str(UGW_senha))
    except paramiko.SSHException:
        print "Connection Failed"
        quit()

    resposta = "[" + UGW_name + "] "
    resp = ""

    chan = ssh.invoke_shell()
    # time.sleep(3)
    while resp != ">":
        resp = chan.recv(1)
    resp = ""

    # Send command
    chan.send('system-view\n')
    while resposta[-8:] != "[" + UGW_name + "]":
        resp = chan.recv(1)
        resposta = resposta + resp
    resposta = "[" + UGW_name + "] "
    resp = ""

    # Send command
    print "     printing: display current-configuration"
    chan.send('display current-configuration\n')
    while resposta[-8:] != "[" + UGW_name + "]":
        resp = chan.recv(1)
        resposta = resposta + resp
        if resposta[-9:-5] == "More":
            chan.send(' ')
    f = open('./Prints_UGW/' + UGW_name + '_print.txt', 'wb')
    f.write(resposta)
    f.close()

    resposta = "[" + UGW_name + "] "
    resp = ""

    # Send command
    chan.send('quit\n')
    while resposta[-8:] != "<" + UGW_name + ">":
        resp = chan.recv(1)
        resposta = resposta + resp

    resposta = "[" + UGW_name + "] "
    resp = ""

    # remover os ---- MORE ---- dos prints
    f = open('./Prints_UGW/' + UGW_name + '_print.txt')
    lines = f.readlines()
    f.close()
    novo_arq = ""
    for line in lines:
        if line[0:68] == '  ---- More ----[42D                                          [42D':
            line = line.replace('  ---- More ----[42D                                          [42D', '')
        novo_arq += line
    f = open('./Prints_UGW/' + UGW_name + '_print.txt', 'wb')
    f.write(novo_arq)
    f.close()

    print "     Concluido."
    print

    ssh.close()
    return ()


# -----------------------------------------------------------------





#                      #
##                    ##
### Função principal ###
##                    ##
#                      #



###### Definir quais bases de FNGs vão ser atualizados


lista_UGWs = {'GPBHE1': '10.207.102.244',
              'GPBLM1': '10.207.99.244',
              'GPBSA1': '10.207.100.244',
              'GPCTA1': '10.207.101.244',
              'GPMNS1': '10.207.104.244',
              'GPRCE1': '10.207.98.244',
              'GPRJO3': '10.207.105.244',
              'GPRJO4': '10.207.106.244',
              'GPSDR1': '10.207.103.244',
              'GPSNE1': '10.207.107.244',
              'GPSPO3': '10.207.108.244'}

# lista_UGWs={'GPRJO3':'10.207.105.244'}




# --------------------------------
# Coleta dos prints nos UGWs
print
print("Coletando dados dos UGWs:")
print
if not os.path.exists('Prints_UGW'): os.mkdir('Prints_UGW')

UGWs = raw_input("UGWs separados por ';' (ex.: GPBSA1;GPBHE1) ou <vazio> para todos? ")
if UGWs == "":
    UGWs = "GPBHE1;GPBLM1;GPBSA1;GPCTA1;GPMNS1;GPRCE1;GPRJO3;GPRJO4;GPSDR1;GPSNE1;GPSPO3"
UGWs = UGWs.split(';')

try:
    for UGW in UGWs:
        ssh_session_UGW(UGW, lista_UGWs[UGW])
except:
    print(u'Falhou conexão com ' + UGWs)
    print
confirma = raw_input("Tecle algo para terminar...")

# --------------------------------
