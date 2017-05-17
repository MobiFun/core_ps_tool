import create_tracking_area_tool as tracking_area_tool
import new_mme_tool as mme_tool
import saegw_pqr_tool as saegw
import migrate_tracking_area_tool as migrate_tac
import gb_iu_planning_tool as gb_iu_planning
import rnc_bsc_tool as rnc_tool
import cvna_app_f5_v4 as f5_app

print('Welcome to the CORE-PS Tool App!')
print('You have to choose an option to begin.')

# noinspection PyBroadException
try:
    while True:
        print('Choose one number:')
        print("1: Create Tracking Area Code in DNS and MME\n"
              "2: Create Gb Iu Planning\n"
              "3: Create RNC and BSC Projects from Gb Iu Planning\n"
              "4: Create new MME in DNS\n"
              "5: Create or Remove SAE-GW in DNS\n"
              "6: Migrate TACs from old MME to new MME\n"
              "7: CVNA F5 APP\n"
              "8: Exit")
        choose_action = raw_input("> ")
        if choose_action == '1':
            tracking_area_tool.main_create_tracking_area_tool()
            continue
        elif choose_action == '2':
            gb_iu_planning.main()
            continue
        elif choose_action == '3':
            rnc_tool.main()
            continue
        elif choose_action == '4':
            mme_tool.main_mme_tool()
            continue
        elif choose_action == '5':
            saegw.main_saegw_pqr_tool()
            continue
        elif choose_action == '6':
            migrate_tac.main_create_tracking_area_tool()
            continue
        elif choose_action == '7':
            f5_app.main_cvna_f5_app_main()
            continue
        elif choose_action == '8':
            print('Bye!')
            raw_input()
            break
except Exception, err:
    print Exception, err
    print("We've encountered an unexpected error. Please report this to decastromonteiro@gmail.com .")
    raw_input()
