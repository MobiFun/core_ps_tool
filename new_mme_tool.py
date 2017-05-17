import nokia_ericsson_new_mme_tool as nsn_ers_mme_tool
import huawei_new_mme_tool as huawei_mme_tool


def main_mme_tool():

    print('Welcome to the MME Tool for CORE-PS DNS!')
    print('You have to choose an option to begin.')

    try:
        while True:
            print('Choose one number:')
            print("1: Create Nokia or Ericsson SGSN/MME in DNS\n"
                  "2: Create Huawei SGSN/MME in DNS\n"
                  "3: Exit")

            choose_action = raw_input("> ")
            if choose_action == '1':
                nsn_ers_mme_tool.main_include_mme()
                continue
            elif choose_action == '2':
                huawei_mme_tool.main_include_mme()
                continue
            elif choose_action == '3':
                print('Bye!')
                break
    except:
        print("We've encountered an unexpected error. Please report this to decastromonteiro@gmail.com .")

if __name__ == '__main__':
    main_mme_tool()
