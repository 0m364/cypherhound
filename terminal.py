import os
import sys
import log
import help
import list
import util
import database

OPTIONS = ['set', 'run', 'export', 'list', 'raw', 'q', 'quit', 'exit', 'clear', 'cls', '?', 'stop', 'help', 'general', 'user', 'group', 'computer', 'regex', 'all']


class Completer:

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        response = None
        if state == 0:
            if text:
                self.matches = [
                    s
                    for s in self.options
                    if s and s.startswith(text)
                ]
            else:
                self.matches = self.options[:]
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response


def input_loop(user, pwd):
    user_config = ""
    group_config = ""
    computer_config = ""
    regex_config = ""
    while True:
        line = input(': ')
        if line == 'q' or line == 'quit' or line == 'exit' or line == 'stop':
            sys.exit(0)
        elif line == 'help' or line == '?' or line == '':
            help.print_help()
            continue
        elif line == 'clear' or line == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        s = line.split(" ")
        if s[0] not in OPTIONS:
            log.log_command_invalid(line)
            continue
        if s[0] == "set":
            if len(s) < 3:
                log.log_command_invalid(line)
                continue
            else:
                option = s[1]
                if not util.validate_set_option(option):
                    log.log_invalid_option(option)
                    continue
                else:
                    if option == "user":
                        user_in = line[9:]
                        user_config = util.validate_user_input(user_in)
                        log.log_successful_set("user", user_config)
                    elif option == "group":
                        group_in = line[10:]
                        group_config = util.validate_user_input(group_in)
                        log.log_successful_set("group", group_config)
                    elif option == "computer":
                        c_in = line[13:]
                        computer_config = util.validate_user_input(c_in)
                        log.log_successful_set("computer", computer_config)
                    elif option == "regex":
                        r_in = line[10:]
                        regex_config = r_in
                        log.log_successful_set("regex", regex_config)
                    else:
                        log.log_command_invalid(line)
                        continue
        elif s[0] == "run":
            if len(s) != 2:
                log.log_command_invalid(line)
                continue
            else:
                option = s[1]
                if not util.validate_run_option(option):
                    log.log_invalid_option(option)
                    continue
                else:
                    if option == "1":
                        d = database.Driver(user, pwd)
                        d.find_all_kerberoastable("", False)
                        d.close()
                    elif option == "2":
                        d = database.Driver(user, pwd)
                        d.find_user_rdp("", False)
                        d.close()
                    elif option == "3":
                        d = database.Driver(user, pwd)
                        d.find_group_rdp("", False)
                        d.close()
                    elif option == "4":
                        d = database.Driver(user, pwd)
                        d.find_unconstrained("", False)
                        d.close()
                    elif option == "5":
                        d = database.Driver(user, pwd)
                        d.find_unsupported("", False)
                        d.close()
                    elif option == "6":
                        d = database.Driver(user, pwd)
                        d.find_admin_groups("", False)
                        d.close()
                    elif option == "7":
                        d = database.Driver(user, pwd)
                        d.find_admin_users("", False)
                        d.close()
                    elif option == "8":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_admin_groups("", False)
                        d.close()
                    elif option == "9":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_admin_groups("", False)
                        d.close()
                    elif option == "10":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_admin_groups("", False)
                        d.close()
                    elif option == "11":
                        d = database.Driver(user, pwd)
                        d.find_sql_groups("", False)
                        d.close()
                    elif option == "12":
                        d = database.Driver(user, pwd)
                        d.find_sql_users("", False)
                        d.close()
                    elif option == "13":
                        d = database.Driver(user, pwd)
                        d.find_sql_computers("", False)
                        d.close()
                    elif option == "14":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_sql_groups("", False)
                        d.close()
                    elif option == "15":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_sql_groups("", False)
                        d.close()
                    elif option == "16":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_sql_groups("", False)
                        d.close()
                    elif option == "17":
                        d = database.Driver(user, pwd)
                        d.find_service_users("", False)
                        d.close()
                    elif option == "18":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_service_groups("", False)
                        d.close()
                    elif option == "19":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_service_groups("", False)
                        d.close()
                    elif option == "20":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_service_groups("", False)
                        d.close()
                    elif option == "21":
                        d = database.Driver(user, pwd)
                        d.find_web_users("", False)
                        d.close()
                    elif option == "22":
                        d = database.Driver(user, pwd)
                        d.find_web_groups("", False)
                        d.close()
                    elif option == "23":
                        d = database.Driver(user, pwd)
                        d.find_web_computers("", False)
                        d.close()
                    elif option == "24":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_web_groups("", False)
                        d.close()
                    elif option == "25":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_web_groups("", False)
                        d.close()
                    elif option == "26":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_web_groups("", False)
                        d.close()
                    elif option == "27":
                        d = database.Driver(user, pwd)
                        d.find_dev_users("", False)
                        d.close()
                    elif option == "28":
                        d = database.Driver(user, pwd)
                        d.find_dev_groups("", False)
                        d.close()
                    elif option == "29":
                        d = database.Driver(user, pwd)
                        d.find_dev_computers("", False)
                        d.close()
                    elif option == "30":
                        d = database.Driver(user, pwd)
                        d.find_prod_users("", False)
                        d.close()
                    elif option == "31":
                        d = database.Driver(user, pwd)
                        d.find_prod_groups("", False)
                        d.close()
                    elif option == "32":
                        d = database.Driver(user, pwd)
                        d.find_prod_computers("", False)
                        d.close()
                    elif option == "33":
                        d = database.Driver(user, pwd)
                        d.find_domain_admins("", False)
                        d.close()
                    elif option == "34":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_das("", False)
                        d.close()
                    elif option == "35":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_das("", False)
                        d.close()
                    elif option == "36":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_das("", False)
                        d.close()
                    elif option == "37":
                        d = database.Driver(user, pwd)
                        d.find_enterprise_admins("", False)
                        d.close()
                    elif option == "38":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_eas("", False)
                        d.close()
                    elif option == "39":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_eas("", False)
                        d.close()
                    elif option == "40":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_eas("", False)
                        d.close()
                    elif option == "41":
                        d = database.Driver(user, pwd)
                        d.find_sessions("", False)
                        d.close()
                    elif option == "42":
                        d = database.Driver(user, pwd)
                        d.find_asrep_roastable("", False)
                        d.close()
                    elif option == "43":
                        d = database.Driver(user, pwd)
                        d.find_highvalue_groups("", False)
                        d.close()
                    elif option == "44":
                        d = database.Driver(user, pwd)
                        d.find_highvalue_members("", False)
                        d.close()
                    elif option == "45":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_high_value("", False)
                        d.close()
                    elif option == "46":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_high_value("", False)
                        d.close()
                    elif option == "47":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_high_value("", False)
                        d.close()
                    elif option == "48":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_exchange_groups("", False)
                        d.close()
                    elif option == "49":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_exchange_groups("", False)
                        d.close()
                    elif option == "50":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_exchange_groups("", False)
                        d.close()
                    elif option == "51":
                        d = database.Driver(user, pwd)
                        d.find_user_localadmin("", False)
                        d.close()
                    elif option == "52":
                        d = database.Driver(user, pwd)
                        d.find_group_localadmin("", False)
                        d.close()
                    elif option == "53":
                        d = database.Driver(user, pwd)
                        d.find_computer_localadmin("", False)
                        d.close()
                    elif option == "54":
                        d = database.Driver(user, pwd)
                        d.find_user_laps("", False)
                        d.close()
                    elif option == "55":
                        d = database.Driver(user, pwd)
                        d.find_group_laps("", False)
                        d.close()                        
                    elif option == "56":
                        d = database.Driver(user, pwd)
                        d.find_computer_laps("", False)
                        d.close()
                    elif option == "57":
                        d = database.Driver(user, pwd)
                        d.find_user_sync_laps("", False)
                        d.close()
                    elif option == "58":
                        d = database.Driver(user, pwd)
                        d.find_group_sync_laps("", False)
                        d.close()                        
                    elif option == "59":
                        d = database.Driver(user, pwd)
                        d.find_computer_sync_laps("", False)
                        d.close()
                    elif option == "60":
                        d = database.Driver(user, pwd)
                        d.find_da_sessions("", False)
                        d.close()
                    elif option == "61":
                        d = database.Driver(user, pwd)
                        d.find_ea_sessions("", False)
                        d.close()
                    elif option == "62":
                        d = database.Driver(user, pwd)
                        d.find_all_users("", False)
                        d.close()
                    elif option == "63":
                        d = database.Driver(user, pwd)
                        d.find_all_groups("", False)
                        d.close()
                    elif option == "64":
                        d = database.Driver(user, pwd)
                        d.find_all_computers("", False)
                        d.close()
                    elif option == "65":
                        d = database.Driver(user, pwd)
                        d.find_all_enabled_computers("", False)
                        d.close()
                    elif option == "66":
                        d = database.Driver(user, pwd)
                        d.find_all_disabled_computers("", False)
                        d.close()
                    elif option == "67":
                        d = database.Driver(user, pwd)
                        d.find_all_dcs("", False)
                        d.close()
                    elif option == "68":
                        d = database.Driver(user, pwd)
                        d.find_all_dcs_oss("", False)
                        d.close()
                    elif option == "69":
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_dcs("", False)
                        d.close()
                    elif option == "70":
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_dcs("", False)
                        d.close()
                    elif option == "71":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_dcs("", False)
                        d.close()
                    elif option == "72":
                        d = database.Driver(user, pwd)
                        d.find_password_not_reqd("", False)
                        d.close()
                    elif option == "73":
                        d = database.Driver(user, pwd)
                        d.find_user_constrained("", False)
                        d.close()
                    elif option == "74":
                        d = database.Driver(user, pwd)
                        d.find_group_constrained("", False)
                        d.close()
                    elif option == "75":
                        d = database.Driver(user, pwd)
                        d.find_computer_constrained("", False)
                        d.close()
                    elif option == "76":
                        d = database.Driver(user, pwd)
                        d.find_gpos("", False)
                        d.close()
                    elif option == "77":
                        d = database.Driver(user, pwd)
                        d.find_domains("", False)
                        d.close()
                    elif option == "78":
                        d = database.Driver(user, pwd)
                        d.find_domain_trusts("", False)
                        d.close()
                    elif option == "79":
                        d = database.Driver(user, pwd)
                        d.find_laps_enabled("", False)
                        d.close()
                    elif option == "80":
                        d = database.Driver(user, pwd)
                        d.find_laps_disabled("", False)
                        d.close()
                    elif option == "81":
                        d = database.Driver(user, pwd)
                        d.find_description_pwds("", False)
                        d.close()
                    elif option == "82":
                        d = database.Driver(user, pwd)
                        d.find_highvalue_users("", False)
                        d.close()
                    elif option == "83":
                        d = database.Driver(user, pwd)
                        d.find_sensitive_users("", False)
                        d.close()
                    elif option == "84":
                        d = database.Driver(user, pwd)
                        d.find_user_admincount("", False)
                        d.close()
                    elif option == "85":
                        d = database.Driver(user, pwd)
                        d.find_group_admincount("", False)
                        d.close()
                    elif option == "86":
                        d = database.Driver(user, pwd)
                        d.find_computer_admincount("", False)
                        d.close()
                    elif option == "87":
                        d = database.Driver(user, pwd)
                        d.find_user_gmsa("", False)
                        d.close()
                    elif option == "88":
                        d = database.Driver(user, pwd)
                        d.find_group_gmsa("", False)
                        d.close()
                    elif option == "89":
                        d = database.Driver(user, pwd)
                        d.find_computer_gmsa("", False)
                        d.close()
                    elif option == "90":
                        d = database.Driver(user, pwd)
                        d.find_user_dcsync("", False)
                        d.close()
                    elif option == "91":
                        d = database.Driver(user, pwd)
                        d.find_group_dcsync("", False)
                        d.close()
                    elif option == "92":
                        d = database.Driver(user, pwd)
                        d.find_computer_dcsync("", False)
                        d.close()
                    elif option == "93":
                        d = database.Driver(user, pwd)
                        d.find_all_dcsync("", False)
                        d.close()
                    elif option == "94":
                        d = database.Driver(user, pwd)
                        d.find_user_force_change_pwd("", False)
                        d.close()
                    elif option == "95":
                        d = database.Driver(user, pwd)
                        d.find_group_force_change_pwd("", False)
                        d.close()
                    elif option == "96":
                        d = database.Driver(user, pwd)
                        d.find_computer_force_change_pwd("", False)
                        d.close()
                    elif option == "97":
                        d = database.Driver(user, pwd)
                        d.find_user_add_member("", False)
                        d.close()
                    elif option == "98":
                        d = database.Driver(user, pwd)
                        d.find_group_add_member("", False)
                        d.close()
                    elif option == "99":
                        d = database.Driver(user, pwd)
                        d.find_computer_add_member("", False)
                        d.close()
                    elif option == "100":
                        d = database.Driver(user, pwd)
                        d.find_user_add_self("", False)
                        d.close()
                    elif option == "101":
                        d = database.Driver(user, pwd)
                        d.find_group_add_self("", False)
                        d.close()
                    elif option == "102":
                        d = database.Driver(user, pwd)
                        d.find_computer_add_self("", False)
                        d.close()
                    elif option == "103":
                        d = database.Driver(user, pwd)
                        d.find_user_sql_admin("", False)
                        d.close()
                    elif option == "104":
                        d = database.Driver(user, pwd)
                        d.find_group_sql_admin("", False)
                        d.close()
                    elif option == "105":
                        d = database.Driver(user, pwd)
                        d.find_computer_sql_admin("", False)
                        d.close()
                    elif option == "106":
                        d = database.Driver(user, pwd)
                        d.find_user_ps_remote("", False)
                        d.close()
                    elif option == "107":
                        d = database.Driver(user, pwd)
                        d.find_group_ps_remote("", False)
                        d.close()
                    elif option == "108":
                        d = database.Driver(user, pwd)
                        d.find_computer_ps_remote("", False)
                        d.close()
                    elif option == "109":
                        d = database.Driver(user, pwd)
                        d.find_user_exec_dcom("", False)
                        d.close()
                    elif option == "110":
                        d = database.Driver(user, pwd)
                        d.find_group_exec_dcom("", False)
                        d.close()
                    elif option == "111":
                        d = database.Driver(user, pwd)
                        d.find_computer_exec_dcom("", False)
                        d.close()
                    elif option == "112":
                        d = database.Driver(user, pwd)
                        d.find_user_allowed_to_act("", False)
                        d.close()
                    elif option == "113":
                        d = database.Driver(user, pwd)
                        d.find_group_allowed_to_act("", False)
                        d.close()
                    elif option == "114":
                        d = database.Driver(user, pwd)
                        d.find_computer_allowed_to_act("", False)
                        d.close()
                    elif option == "115":
                        d = database.Driver(user, pwd)
                        d.find_user_owns("", False)
                        d.close()
                    elif option == "116":
                        d = database.Driver(user, pwd)
                        d.find_group_owns("", False)
                        d.close()
                    elif option == "117":
                        d = database.Driver(user, pwd)
                        d.find_computer_owns("", False)
                        d.close()
                    elif option == "118":
                        d = database.Driver(user, pwd)
                        d.find_user_all_extended("", False)
                        d.close()
                    elif option == "119":
                        d = database.Driver(user, pwd)
                        d.find_group_all_extended("", False)
                        d.close()
                    elif option == "120":
                        d = database.Driver(user, pwd)
                        d.find_computer_all_extended("", False)
                        d.close()
                    elif option == "121":
                        d = database.Driver(user, pwd)
                        d.find_user_member_of("", False)
                        d.close()
                    elif option == "122":
                        d = database.Driver(user, pwd)
                        d.find_group_member_of("", False)
                        d.close()
                    elif option == "123":
                        d = database.Driver(user, pwd)
                        d.find_computer_member_of("", False)
                        d.close()
                    elif option == "124":
                        d = database.Driver(user, pwd)
                        d.find_user_add_key_cred_link("", False)
                        d.close()
                    elif option == "125":
                        d = database.Driver(user, pwd)
                        d.find_group_add_key_cred_link("", False)
                        d.close()
                    elif option == "126":
                        d = database.Driver(user, pwd)
                        d.find_computer_add_key_cred_link("", False)
                        d.close()
                    elif option == "127":
                        d = database.Driver(user, pwd)
                        d.find_user_generic_all("", False)
                        d.close()
                    elif option == "128":
                        d = database.Driver(user, pwd)
                        d.find_group_generic_all("", False)
                        d.close()
                    elif option == "129":
                        d = database.Driver(user, pwd)
                        d.find_computer_generic_all("", False)
                        d.close()
                    elif option == "130":
                        d = database.Driver(user, pwd)
                        d.find_user_write_dacl("", False)
                        d.close()
                    elif option == "131":
                        d = database.Driver(user, pwd)
                        d.find_group_write_dacl("", False)
                        d.close()
                    elif option == "132":
                        d = database.Driver(user, pwd)
                        d.find_computer_write_dacl("", False)
                        d.close()
                    elif option == "133":
                        d = database.Driver(user, pwd)
                        d.find_user_write_owner("", False)
                        d.close()
                    elif option == "134":
                        d = database.Driver(user, pwd)
                        d.find_group_write_owner("", False)
                        d.close()
                    elif option == "135":
                        d = database.Driver(user, pwd)
                        d.find_computer_write_owner("", False)
                        d.close()
                    elif option == "136":
                        d = database.Driver(user, pwd)
                        d.find_user_generic_write("", False)
                        d.close()
                    elif option == "137":
                        d = database.Driver(user, pwd)
                        d.find_group_generic_write("", False)
                        d.close()
                    elif option == "138":
                        d = database.Driver(user, pwd)
                        d.find_computer_generic_write("", False)
                        d.close()
                    elif option == "139":
                        d = database.Driver(user, pwd)
                        d.find_service_groups("", False)
                        d.close()
                    elif option == "140":
                        d = database.Driver(user, pwd)
                        d.find_user_descriptions("", False)
                        d.close()
                    elif option == "141":
                        d = database.Driver(user, pwd)
                        d.find_group_descriptions("", False)
                        d.close()
                    elif option == "142":
                        d = database.Driver(user, pwd)
                        d.find_emails("", False)
                        d.close()
                    elif option == "143":
                        d = database.Driver(user, pwd)
                        d.find_ous("", False)
                        d.close()
                    elif option == "144":
                        d = database.Driver(user, pwd)
                        d.find_containers("", False)
                        d.close()
                    elif option == "145":
                        d = database.Driver(user, pwd)
                        d.find_domains("", False)
                        d.close()
                    elif option == "146":
                        d = database.Driver(user, pwd)
                        d.find_domains_flevel("", False)
                        d.close()
                    elif option == "147":
                        d = database.Driver(user, pwd)
                        d.find_ou_oc("", False)
                        d.close()
                    elif option == "148":
                        d = database.Driver(user, pwd)
                        d.find_container_oc("", False)
                        d.close()
                    elif option == "149":
                        d = database.Driver(user, pwd)
                        d.find_gpo_oc("", False)
                        d.close()
                    elif option == "150":
                        d = database.Driver(user, pwd)
                        d.find_all_gp_links("", False)
                        d.close()
                    elif option == "151":
                        d = database.Driver(user, pwd)
                        d.find_all_user_privs("", False)
                        d.close()
                    elif option == "152":
                        d = database.Driver(user, pwd)
                        d.find_all_group_privs("", False)
                        d.close()
                    elif option == "153":
                        d = database.Driver(user, pwd)
                        d.find_all_computer_privs("", False)
                        d.close()
                    elif option == "154":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_rdp_us("", False)
                            d.close()
                    elif option == "155":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_rdp_gd_us("", False)
                            d.close()
                    elif option == "156":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_localadmin_us("", False)
                            d.close()
                    elif option == "157":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_localadmin_gd_us("", False)
                            d.close()
                    elif option == "158":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sessions_us("", False)
                            d.close()
                    elif option == "159":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_laps_us("", False)
                            d.close()
                    elif option == "160":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sync_laps_us("", False)
                            d.close()                   
                    elif option == "161":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_gmsa_us("", False)
                            d.close()
                    elif option == "162":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_constrained_us("", False)
                            d.close()
                    elif option == "163":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_force_change_pwd_us("", False)
                            d.close()
                    elif option == "164":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_add_member_us("", False)
                            d.close()
                    elif option == "165":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_add_self_us("", False)
                            d.close()
                    elif option == "166":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sql_admin_us("", False)
                            d.close()
                    elif option == "167":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_ps_remote_us("", False)
                            d.close()
                    elif option == "168":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_exec_dcom_us("", False)
                            d.close()
                    elif option == "169":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_allowed_to_act_us("", False)
                            d.close()
                    elif option == "170":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_owns_us("", False)
                            d.close()
                    elif option == "171":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_extended_us("", False)
                            d.close()
                    elif option == "172":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_add_key_cred_link_us("", False)
                            d.close()
                    elif option == "173":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_generic_all_us("", False)
                            d.close()
                    elif option == "174":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_write_dacl_us("", False)
                            d.close()
                    elif option == "175":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_write_owner_us("", False)
                            d.close()
                    elif option == "176":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_generic_write_us("", False)
                            d.close()
                    elif option == "177":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_description_us("", False)
                            d.close()
                    elif option == "178":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_email_us("", False)
                            d.close()
                    elif option == "179":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_member_of_us("", False)
                            d.close()
                    elif option == "180":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_asrep_roastable_us("", False)
                            d.close()
                    elif option == "181":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_kerberoastable_us("", False)
                            d.close()
                    elif option == "182":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_us("", False)
                            d.close()
                    elif option == "183":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_gd_us("", False)
                            d.close()
                    elif option == "184":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_high_value_us("", False)
                            d.close()
                    elif option == "185":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_das_us("", False)
                            d.close()
                    elif option == "186":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_eas_us("", False)
                            d.close()
                    elif option == "187":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_dcs_us("", False)
                            d.close()
                    elif option == "188":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_exchange_groups_us("", False)
                            d.close()
                    elif option == "189":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_admin_groups_us("", False)
                            d.close()
                    elif option == "190":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_sql_groups_us("", False)
                            d.close()
                    elif option == "191":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_web_groups_us("", False)
                            d.close()
                    elif option == "192":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_service_groups_us("", False)
                            d.close()
                    elif option == "193":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_sp_to_us("", False)
                            d.close()
                    elif option == "194":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_rdp_gs("", False)
                            d.close()
                    elif option == "195":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_rdp_gd_gs("", False)
                            d.close()
                    elif option == "196":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_localadmin_gs("", False)
                            d.close()
                    elif option == "197":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_localadmin_gd_gs("", False)
                            d.close()
                    elif option == "198":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_laps_gs("", False)
                            d.close()
                    elif option == "199":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sync_laps_gs("", False)
                            d.close()
                    elif option == "200":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_gmsa_gs("", False)
                            d.close()
                    elif option == "201":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_constrained_gs("", False)
                            d.close()
                    elif option == "202":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_force_change_pwd_gs("", False)
                            d.close()
                    elif option == "203":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_add_member_gs("", False)
                            d.close()
                    elif option == "204":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_add_self_gs("", False)
                            d.close()
                    elif option == "205":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sql_admin_gs("", False)
                            d.close()
                    elif option == "206":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_ps_remote_gs("", False)
                            d.close()
                    elif option == "207":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_exec_dcom_gs("", False)
                            d.close()
                    elif option == "208":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_allowed_to_act_gs("", False)
                            d.close()
                    elif option == "209":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_owns_gs("", False)
                            d.close()
                    elif option == "210":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_extended_gs("", False)
                            d.close()
                    elif option == "211":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_add_key_cred_link_gs("", False)
                            d.close()
                    elif option == "212":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_generic_all_gs("", False)
                            d.close()
                    elif option == "213":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_write_dacl_gs("", False)
                            d.close()
                    elif option == "214":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_write_owner_gs("", False)
                            d.close()
                    elif option == "215":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_generic_write_gs("", False)
                            d.close()
                    elif option == "216":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_description_gs("", False)
                            d.close()
                    elif option == "217":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_member_of_gs("", False)
                            d.close()
                    elif option == "218":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_members_gs("", False)
                            d.close()
                    elif option == "219":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_gs("", False)
                            d.close()
                    elif option == "220":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_gd_gs("", False)
                            d.close()
                    elif option == "221":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_high_value_gs("", False)
                            d.close()
                    elif option == "222":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_das_gs("", False)
                            d.close()
                    elif option == "223":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_eas_gs("", False)
                            d.close()
                    elif option == "224":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_dcs_gs("", False)
                            d.close()
                    elif option == "225":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_exchange_groups_gs("", False)
                            d.close()
                    elif option == "226":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_admin_groups_gs("", False)
                            d.close()
                    elif option == "227":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_sql_groups_gs("", False)
                            d.close()
                    elif option == "228":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_web_groups_gs("", False)
                            d.close()
                    elif option == "229":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_service_groups_gs("", False)
                            d.close()
                    elif option == "230":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_sp_to_gs("", False)
                            d.close()
                    elif option == "231":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_localadmin_cs("", False)
                            d.close()
                    elif option == "232":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_localadmin_gd_cs("", False)
                            d.close()
                    elif option == "233":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_laps_cs("", False)
                            d.close()
                    elif option == "234":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sync_laps_cs("", False)
                            d.close()
                    elif option == "235":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_gmsa_cs("", False)
                            d.close()
                    elif option == "236":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_constrained_cs("", False)
                            d.close()
                    elif option == "237":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_force_change_pwd_cs("", False)
                            d.close()
                    elif option == "238":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_add_member_cs("", False)
                            d.close()
                    elif option == "239":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_add_self_cs("", False)
                            d.close()
                    elif option == "240":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sql_admin_cs("", False)
                            d.close()
                    elif option == "241":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_ps_remote_cs("", False)
                            d.close()
                    elif option == "242":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_exec_dcom_cs("", False)
                            d.close()
                    elif option == "243":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_allowed_to_act_cs("", False)
                            d.close()
                    elif option == "244":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_owns_cs("", False)
                            d.close()
                    elif option == "245":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_extended_cs("", False)
                            d.close()
                    elif option == "246":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_add_key_cred_link_cs("", False)
                            d.close()
                    elif option == "247":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_generic_all_cs("", False)
                            d.close()
                    elif option == "248":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_write_dacl_cs("", False)
                            d.close()
                    elif option == "249":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_write_owner_cs("", False)
                            d.close()
                    elif option == "250":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_generic_write_cs("", False)
                            d.close()
                    elif option == "251":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_member_of_cs("", False)
                            d.close()
                    elif option == "252":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_cs("", False)
                            d.close()
                    elif option == "253":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_gd_cs("", False)
                            d.close()
                    elif option == "254":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_high_value_cs("", False)
                            d.close()
                    elif option == "255":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_das_cs("", False)
                            d.close()
                    elif option == "256":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_eas_cs("", False)
                            d.close()
                    elif option == "257":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_dcs_cs("", False)
                            d.close()
                    elif option == "258":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_exchange_groups_cs("", False)
                            d.close()
                    elif option == "259":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_admin_groups_cs("", False)
                            d.close()
                    elif option == "260":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_sql_groups_cs("", False)
                            d.close()
                    elif option == "261":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_web_groups_cs("", False)
                            d.close()
                    elif option == "262":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_service_groups_cs("", False)
                            d.close()
                    elif option == "263":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_sp_to_cs("", False)
                            d.close()
                    elif option == "264":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_groups_r("", False)
                            d.close()
                    elif option == "265":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_users_r("", False)
                            d.close()
                    elif option == "266":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_computers_r("", False)
                            d.close()
                    elif option == "267":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_u_descriptions_r("", False)
                            d.close()
                    elif option == "268":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_g_descriptions_r("", False)
                            d.close()
                    elif option == "269":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_oss_r("", False)
                            d.close()
                    elif option == "270":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_gpos_r("", False)
                            d.close()
                    elif option == "271":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_containers_r("", False)
                            d.close()
                    elif option == "272":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_ous_r("", False)
                            d.close()
                    else:
                        log.log_command_invalid(line)
                        continue
        elif s[0] == "export":
            if len(s) < 3:
                log.log_command_invalid(line)
                continue
            else:
                option = s[1]
                fname = s[2]
                if not util.validate_run_option(option):
                    log.log_invalid_option(option)
                    continue
                else:
                    is_raw = False
                    if len(s) == 4:
                        c = s[3]
                        if util.validate_raw_command(c):
                            is_raw = True
                    if option == "1":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_kerberoastable(f, is_raw)
                        d.close()
                    elif option == "2":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_rdp(f, is_raw)
                        d.close()
                    elif option == "3":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_rdp(f, is_raw)
                        d.close()
                    elif option == "4":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_unconstrained(f, is_raw)
                        d.close()
                    elif option == "5":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_unsupported(f, is_raw)
                        d.close()
                    elif option == "6":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_admin_groups(f, is_raw)
                        d.close()
                    elif option == "7":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_admin_users(f, is_raw)
                        d.close()
                    elif option == "8":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_admin_groups(f, is_raw)
                        d.close()
                    elif option == "9":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_admin_groups(f, is_raw)
                        d.close()
                    elif option == "10":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_admin_groups(f, is_raw)
                        d.close()
                    elif option == "11":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_sql_groups(f, is_raw)
                        d.close()
                    elif option == "12":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_sql_users(f, is_raw)
                        d.close()
                    elif option == "13":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_sql_computers(f, is_raw)
                        d.close()
                    elif option == "14":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_sql_groups(f, is_raw)
                        d.close()
                    elif option == "15":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_sql_groups(f, is_raw)
                        d.close()
                    elif option == "16":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_sql_groups(f, is_raw)
                        d.close()
                    elif option == "17":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_service_users(f, is_raw)
                        d.close()
                    elif option == "18":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_service_groups(f, is_raw)
                        d.close()
                    elif option == "19":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_service_groups(f, is_raw)
                        d.close()
                    elif option == "20":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_service_groups(f, is_raw)
                        d.close()
                    elif option == "21":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_web_users(f, is_raw)
                        d.close()
                    elif option == "22":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_web_groups(f, is_raw)
                        d.close()
                    elif option == "23":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_web_computers(f, is_raw)
                        d.close()
                    elif option == "24":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_web_groups(f, is_raw)
                        d.close()
                    elif option == "25":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_web_groups(f, is_raw)
                        d.close()
                    elif option == "26":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_web_groups(f, is_raw)
                        d.close()
                    elif option == "27":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_dev_users(f, is_raw)
                        d.close()
                    elif option == "28":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_dev_groups(f, is_raw)
                        d.close()
                    elif option == "29":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_dev_computers(f, is_raw)
                        d.close()
                    elif option == "30":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_prod_users(f, is_raw)
                        d.close()
                    elif option == "31":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_prod_groups(f, is_raw)
                        d.close()
                    elif option == "32":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_prod_computers(f, is_raw)
                        d.close()
                    elif option == "33":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_domain_admins(f, is_raw)
                        d.close()
                    elif option == "34":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_das(f, is_raw)
                        d.close()
                    elif option == "35":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_das(f, is_raw)
                        d.close()
                    elif option == "36":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_das(f, is_raw)
                        d.close()
                    elif option == "37":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_enterprise_admins(f, is_raw)
                        d.close()
                    elif option == "38":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_eas(f, is_raw)
                        d.close()
                    elif option == "39":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_eas(f, is_raw)
                        d.close()
                    elif option == "40":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_eas(f, is_raw)
                        d.close()
                    elif option == "41":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_sessions(f, is_raw)
                        d.close()
                    elif option == "42":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_asrep_roastable(f, is_raw)
                        d.close()
                    elif option == "43":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_highvalue_groups(f, is_raw)
                        d.close()
                    elif option == "44":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_highvalue_members(f, is_raw)
                        d.close()
                    elif option == "45":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_high_value(f, is_raw)
                        d.close()
                    elif option == "46":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_high_value(f, is_raw)
                        d.close()
                    elif option == "47":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_high_value(f, is_raw)
                        d.close()
                    elif option == "48":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_exchange_groups(f, is_raw)
                        d.close()
                    elif option == "49":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_exchange_groups(f, is_raw)
                        d.close()
                    elif option == "50":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_exchange_groups(f, is_raw)
                        d.close()
                    elif option == "51":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_localadmin(f, is_raw)
                        d.close()
                    elif option == "52":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_localadmin(f, is_raw)
                        d.close()                        
                    elif option == "53":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_localadmin(f, is_raw)
                        d.close()
                    elif option == "54":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_laps(f, is_raw)
                        d.close()
                    elif option == "55":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_laps(f, is_raw)
                        d.close()                        
                    elif option == "56":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_laps(f, is_raw)
                    elif option == "57":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_sync_laps(f, is_raw)
                        d.close()
                    elif option == "58":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_sync_laps(f, is_raw)
                        d.close()                        
                    elif option == "59":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_sync_laps(f, is_raw)
                        d.close()
                    elif option == "60":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_da_sessions(f, is_raw)
                        d.close()
                    elif option == "61":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_ea_sessions(f, is_raw)
                        d.close()
                    elif option == "62":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_users(f, is_raw)
                        d.close()
                    elif option == "63":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_groups(f, is_raw)
                        d.close()
                    elif option == "64":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computers(f, is_raw)
                        d.close()
                    elif option == "65":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_enabled_computers(f, is_raw)
                        d.close()
                    elif option == "66":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_disabled_computers(f, is_raw)
                        d.close()
                    elif option == "67":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_dcs(f, is_raw)
                        d.close()
                    elif option == "68":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_dcs_oss(f, is_raw)
                        d.close()
                    elif option == "69":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_sp_to_dcs(f, is_raw)
                        d.close()
                    elif option == "70":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_sp_to_dcs(f, is_raw)
                        d.close()
                    elif option == "71":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_sp_to_dcs(f, is_raw)
                        d.close()
                    elif option == "72":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_password_not_reqd(f, is_raw)
                        d.close()
                    elif option == "73":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_constrained(f, is_raw)
                        d.close()
                    elif option == "74":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_constrained(f, is_raw)
                        d.close()
                    elif option == "75":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_constrained(f, is_raw)
                        d.close()
                    elif option == "76":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_gpos(f, is_raw)
                        d.close()
                    elif option == "77":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_domains(f, is_raw)
                        d.close()
                    elif option == "78":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_domain_trusts(f, is_raw)
                        d.close()
                    elif option == "79":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_laps_enabled(f, is_raw)
                        d.close()
                    elif option == "80":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_laps_disabled(f, is_raw)
                        d.close()
                    elif option == "81":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_description_pwds(f, is_raw)
                        d.close()
                    elif option == "82":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_highvalue_users(f, is_raw)
                        d.close()
                    elif option == "83":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_sensitive_users(f, is_raw)
                        d.close()
                    elif option == "84":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_admincount(f, is_raw)
                        d.close()
                    elif option == "85":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_admincount(f, is_raw)
                        d.close()
                    elif option == "86":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_admincount(f, is_raw)
                        d.close()
                    elif option == "87":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_gmsa(f, is_raw)
                        d.close()
                    elif option == "88":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_gmsa(f, is_raw)
                        d.close()
                    elif option == "89":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_gmsa(f, is_raw)
                        d.close()
                    elif option == "90":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_dcsync(f, is_raw)
                        d.close()
                    elif option == "91":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_dcsync(f, is_raw)
                        d.close()
                    elif option == "92":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_dcsync(f, is_raw)
                        d.close()
                    elif option == "93":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_dcsync(f, is_raw)
                        d.close()
                    elif option == "94":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_force_change_pwd(f, is_raw)
                        d.close()
                    elif option == "95":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_force_change_pwd(f, is_raw)
                        d.close()
                    elif option == "96":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_force_change_pwd(f, is_raw)
                        d.close()
                    elif option == "97":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_add_member(f, is_raw)
                        d.close()
                    elif option == "98":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_add_member(f, is_raw)
                        d.close()
                    elif option == "99":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_add_member(f, is_raw)
                        d.close()
                    elif option == "100":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_add_self(f, is_raw)
                        d.close()
                    elif option == "101":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_add_self(f, is_raw)
                        d.close()
                    elif option == "102":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_add_self(f, is_raw)
                        d.close()
                    elif option == "103":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_sql_admin(f, is_raw)
                        d.close()
                    elif option == "104":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_sql_admin(f, is_raw)
                        d.close()
                    elif option == "105":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_sql_admin(f, is_raw)
                        d.close()
                    elif option == "106":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_ps_remote(f, is_raw)
                        d.close()
                    elif option == "107":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_ps_remote(f, is_raw)
                        d.close()
                    elif option == "108":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_ps_remote(f, is_raw)
                        d.close()
                    elif option == "109":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_exec_dcom(f, is_raw)
                        d.close()
                    elif option == "110":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_exec_dcom(f, is_raw)
                        d.close()
                    elif option == "111":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_exec_dcom(f, is_raw)
                        d.close()
                    elif option == "112":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_allowed_to_act(f, is_raw)
                        d.close()
                    elif option == "113":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_allowed_to_act(f, is_raw)
                        d.close()
                    elif option == "114":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_allowed_to_act(f, is_raw)
                        d.close()
                    elif option == "115":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_owns(f, is_raw)
                        d.close()
                    elif option == "116":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_owns(f, is_raw)
                        d.close()
                    elif option == "117":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_owns(f, is_raw)
                        d.close()
                    elif option == "118":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_all_extended(f, is_raw)
                        d.close()
                    elif option == "119":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_all_extended(f, is_raw)
                        d.close()
                    elif option == "120":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_all_extended(f, is_raw)
                        d.close()
                    elif option == "121":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_member_of(f, is_raw)
                        d.close()
                    elif option == "122":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_member_of(f, is_raw)
                        d.close()
                    elif option == "123":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_member_of(f, is_raw)
                        d.close()
                    elif option == "124":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_add_key_cred_link(f, is_raw)
                        d.close()
                    elif option == "125":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_add_key_cred_link(f, is_raw)
                        d.close()
                    elif option == "126":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_add_key_cred_link(f, is_raw)
                        d.close()
                    elif option == "127":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_generic_all(f, is_raw)
                        d.close()
                    elif option == "128":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_generic_all(f, is_raw)
                        d.close()
                    elif option == "129":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_generic_all(f, is_raw)
                        d.close()
                    elif option == "130":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_write_dacl(f, is_raw)
                        d.close()
                    elif option == "131":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_write_dacl(f, is_raw)
                        d.close()
                    elif option == "132":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_write_dacl(f, is_raw)
                        d.close()
                    elif option == "133":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_write_owner(f, is_raw)
                        d.close()
                    elif option == "134":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_write_owner(f, is_raw)
                        d.close()
                    elif option == "135":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_write_owner(f, is_raw)
                        d.close()
                    elif option == "136":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_generic_write(f, is_raw)
                        d.close()
                    elif option == "137":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_generic_write(f, is_raw)
                        d.close()
                    elif option == "138":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_computer_generic_write(f, is_raw)
                        d.close()
                    elif option == "139":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_service_groups(f, is_raw)
                        d.close()
                    elif option == "140":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_user_descriptions(f, is_raw)
                        d.close()
                    elif option == "141":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_group_descriptions(f, is_raw)
                        d.close()
                    elif option == "142":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_emails(f, is_raw)
                        d.close()
                    elif option == "143":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_ous(f, is_raw)
                        d.close()
                    elif option == "144":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_containers(f, is_raw)
                        d.close()
                    elif option == "145":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_domains(f, is_raw)
                        d.close()
                    elif option == "146":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_domains_flevel(f, is_raw)
                        d.close()
                    elif option == "147":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_ou_oc(f, is_raw)
                        d.close()
                    elif option == "148":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_container_oc(f, is_raw)
                        d.close()
                    elif option == "149":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_gpo_oc(f, is_raw)
                        d.close()
                    elif option == "150":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_gp_links(f, is_raw)
                        d.close()
                    elif option == "151":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_user_privs(f, is_raw)
                        d.close()
                    elif option == "152":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_group_privs(f, is_raw)
                        d.close()
                    elif option == "153":
                        f = util.validate_export_command(fname)
                        d = database.Driver(user, pwd)
                        d.find_all_computer_privs(f, is_raw)
                        d.close()
                    elif option == "154":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_rdp_us(f, is_raw)
                            d.close()
                    elif option == "155":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_rdp_gd_us(f, is_raw)
                            d.close()
                    elif option == "156":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_localadmin_us(f, is_raw)
                            d.close()
                    elif option == "157":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_localadmin_gd_us(f, is_raw)
                            d.close()
                    elif option == "158":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sessions_us(f, is_raw)
                            d.close()
                    elif option == "159":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_laps_us(f, is_raw)
                            d.close()
                    elif option == "160":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sync_laps_us(f, is_raw)
                            d.close()
                    elif option == "161":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_gmsa_us(f, is_raw)
                            d.close()
                    elif option == "162":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_constrained_us(f, is_raw)
                            d.close()
                    elif option == "163":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_force_change_pwd_us(f, is_raw)
                            d.close()
                    elif option == "164":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_add_member_us(f, is_raw)
                            d.close()
                    elif option == "165":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_add_self_us(f, is_raw)
                            d.close()
                    elif option == "166":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sql_admin_us(f, is_raw)
                            d.close()
                    elif option == "167":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_ps_remote_us(f, is_raw)
                            d.close()
                    elif option == "168":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_exec_dcom_us(f, is_raw)
                            d.close()
                    elif option == "169":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_allowed_to_act_us(f, is_raw)
                            d.close()
                    elif option == "170":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_owns_us(f, is_raw)
                            d.close()
                    elif option == "171":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_extended_us(f, is_raw)
                            d.close()
                    elif option == "172":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_add_key_cred_link_us(f, is_raw)
                            d.close()
                    elif option == "173":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_generic_all_us(f, is_raw)
                            d.close()
                    elif option == "174":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_write_dacl_us(f, is_raw)
                            d.close()
                    elif option == "175":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_write_owner_us(f, is_raw)
                            d.close()
                    elif option == "176":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_generic_write_us(f, is_raw)
                            d.close()
                    elif option == "177":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_description_us(f, is_raw)
                            d.close()
                    elif option == "178":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_email_us(f, is_raw)
                            d.close()
                    elif option == "179":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_member_of_us(f, is_raw)
                            d.close()
                    elif option == "180":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_asrep_roastable_us(f, is_raw)
                            d.close()
                    elif option == "181":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_kerberoastable_us(f, is_raw)
                            d.close()
                    elif option == "182":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_us(f, is_raw)
                            d.close()
                    elif option == "183":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_gd_us(f, is_raw)
                            d.close()
                    elif option == "184":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_high_value_us(f, is_raw)
                            d.close()
                    elif option == "185":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_das_us(f, is_raw)
                            d.close()
                    elif option == "186":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_eas_us(f, is_raw)
                            d.close()
                    elif option == "187":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_dcs_us(f, is_raw)
                            d.close()
                    elif option == "188":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_exchange_groups_us(f, is_raw)
                            d.close()
                    elif option == "189":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_admin_groups_us(f, is_raw)
                            d.close()
                    elif option == "190":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_sql_groups_us(f, is_raw)
                            d.close()
                    elif option == "191":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_web_groups_us(f, is_raw)
                            d.close()
                    elif option == "192":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_sp_to_service_groups_us(f, is_raw)
                            d.close()
                    elif option == "193":
                        if not util.validate_user_config(user_config):
                            log.log_config_not_set("user")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_user_param(user_config)
                            d.find_all_sp_to_us(f, is_raw)
                            d.close()
                    elif option == "194":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_rdp_gs(f, is_raw)
                            d.close()
                    elif option == "195":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_rdp_gd_gs(f, is_raw)
                            d.close()
                    elif option == "196":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_localadmin_gs(f, is_raw)
                            d.close()
                    elif option == "197":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_localadmin_gd_gs(f, is_raw)
                            d.close()
                    elif option == "198":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_laps_gs(f, is_raw)
                            d.close()
                    elif option == "199":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sync_laps_gs(f, is_raw)
                            d.close()
                    elif option == "200":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_gmsa_gs(f, is_raw)
                            d.close()
                    elif option == "201":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_constrained_gs(f, is_raw)
                            d.close()
                    elif option == "202":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_force_change_pwd_gs(f, is_raw)
                            d.close()
                    elif option == "203":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_add_member_gs(f, is_raw)
                            d.close()
                    elif option == "204":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_add_self_gs(f, is_raw)
                            d.close()
                    elif option == "205":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sql_admin_gs(f, is_raw)
                            d.close()
                    elif option == "206":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_ps_remote_gs(f, is_raw)
                            d.close()
                    elif option == "207":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_exec_dcom_gs(f, is_raw)
                            d.close()
                    elif option == "208":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_allowed_to_act_gs(f, is_raw)
                            d.close()
                    elif option == "209":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_owns_gs(f, is_raw)
                            d.close()
                    elif option == "210":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_extended_gs(f, is_raw)
                            d.close()
                    elif option == "211":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_add_key_cred_link_gs(f, is_raw)
                            d.close()
                    elif option == "212":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_generic_all_gs(f, is_raw)
                            d.close()
                    elif option == "213":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_write_dacl_gs(f, is_raw)
                            d.close()
                    elif option == "214":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_write_owner_gs(f, is_raw)
                            d.close()
                    elif option == "215":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_generic_write_gs(f, is_raw)
                            d.close()
                    elif option == "216":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_description_gs(f, is_raw)
                            d.close()
                    elif option == "217":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_member_of_gs(f, is_raw)
                            d.close()
                    elif option == "218":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_members_gs(f, is_raw)
                            d.close()
                    elif option == "219":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_gs(f, is_raw)
                            d.close()
                    elif option == "220":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_gd_gs(f, is_raw)
                            d.close()
                    elif option == "221":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_high_value_gs(f, is_raw)
                            d.close()
                    elif option == "222":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_das_gs(f, is_raw)
                            d.close()
                    elif option == "223":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_eas_gs(f, is_raw)
                            d.close()
                    elif option == "224":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_dcs_gs(f, is_raw)
                            d.close()
                    elif option == "225":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_exchange_groups_gs(f, is_raw)
                            d.close()
                    elif option == "226":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_admin_groups_gs(f, is_raw)
                            d.close()
                    elif option == "227":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_sql_groups_gs(f, is_raw)
                            d.close()
                    elif option == "228":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_web_groups_gs(f, is_raw)
                            d.close()
                    elif option == "229":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_sp_to_service_groups_gs(f, is_raw)
                            d.close()
                    elif option == "230":
                        if not util.validate_group_config(group_config):
                            log.log_config_not_set("group")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_group_param(group_config)
                            d.find_all_sp_to_gs(f, is_raw)
                            d.close()
                    elif option == "231":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_localadmin_cs(f, is_raw)
                            d.close()
                    elif option == "232":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_localadmin_gd_cs(f, is_raw)
                            d.close()
                    elif option == "233":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_laps_cs(f, is_raw)
                            d.close()
                    elif option == "234":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sync_laps_cs(f, is_raw)
                            d.close()
                    elif option == "235":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_gmsa_cs(f, is_raw)
                            d.close()
                    elif option == "236":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_constrained_cs(f, is_raw)
                            d.close()
                    elif option == "237":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_force_change_pwd_cs(f, is_raw)
                            d.close()
                    elif option == "238":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_add_member_cs(f, is_raw)
                            d.close()
                    elif option == "239":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_add_self_cs(f, is_raw)
                            d.close()
                    elif option == "240":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sql_admin_cs(f, is_raw)
                            d.close()
                    elif option == "241":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_ps_remote_cs(f, is_raw)
                            d.close()
                    elif option == "242":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_exec_dcom_cs(f, is_raw)
                            d.close()
                    elif option == "243":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_allowed_to_act_cs(f, is_raw)
                            d.close()
                    elif option == "244":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_owns_cs(f, is_raw)
                            d.close()
                    elif option == "245":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_extended_cs(f, is_raw)
                            d.close()
                    elif option == "246":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_add_key_cred_link_cs(f, is_raw)
                            d.close()
                    elif option == "247":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_generic_all_cs(f, is_raw)
                            d.close()
                    elif option == "248":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_write_dacl_cs(f, is_raw)
                            d.close()
                    elif option == "249":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_write_owner_cs(f, is_raw)
                            d.close()
                    elif option == "250":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_generic_write_cs(f, is_raw)
                            d.close()
                    elif option == "251":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_member_of_cs(f, is_raw)
                            d.close()
                    elif option == "252":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_cs(f, is_raw)
                            d.close()
                    elif option == "253":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_gd_cs(f, is_raw)
                            d.close()
                    elif option == "254":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_high_value_cs(f, is_raw)
                            d.close()
                    elif option == "255":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_das_cs(f, is_raw)
                            d.close()
                    elif option == "256":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_eas_cs(f, is_raw)
                            d.close()
                    elif option == "257":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_dcs_cs(f, is_raw)
                            d.close()
                    elif option == "258":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_exchange_groups_cs(f, is_raw)
                            d.close()
                    elif option == "259":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_admin_groups_cs(f, is_raw)
                            d.close()
                    elif option == "260":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_sql_groups_cs(f, is_raw)
                            d.close()
                    elif option == "261":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_web_groups_cs(f, is_raw)
                            d.close()
                    elif option == "262":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_sp_to_service_groups_cs(f, is_raw)
                            d.close()
                    elif option == "263":
                        if not util.validate_computer_config(computer_config):
                            log.log_config_not_set("computer")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_computer_param(computer_config)
                            d.find_all_sp_to_cs(f, is_raw)
                            d.close()
                    elif option == "264":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_groups_r(f, is_raw)
                            d.close()
                    elif option == "265":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_users_r(f, is_raw)
                            d.close()
                    elif option == "266":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_computers_r(f, is_raw)
                            d.close()
                    elif option == "267":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_u_descriptions_r(f, is_raw)
                            d.close()
                    elif option == "268":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_g_descriptions_r(f, is_raw)
                            d.close()
                    elif option == "269":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_oss_r(f, is_raw)
                            d.close()
                    elif option == "270":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_gpos_r(f, is_raw)
                            d.close()
                    elif option == "271":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_containers_r(f, is_raw)
                            d.close()
                    elif option == "272":
                        if not util.validate_regex_config(regex_config):
                            log.log_config_not_set("regex")
                        else:
                            f = util.validate_export_command(fname)
                            d = database.Driver(user, pwd)
                            d.set_regex(regex_config)
                            d.find_ous_r(f, is_raw)
                            d.close()
                    else:
                        log.log_command_invalid(line)
                        continue
        elif s[0] == "list":
            if len(s) < 2:
                log.log_command_invalid(line)
                continue
            else:
                option = s[1]
                if not util.validate_list_command(option):
                    log.log_invalid_option(option)
                else:
                    if option == "general":
                        list.print_general_list()
                    elif option == "user":
                        list.print_user_list()
                    elif option == "group":
                        list.print_group_list()
                    elif option == "computer":
                        list.print_computer_list()
                    elif option == "regex":
                        list.print_regex_list()
                    elif option == "all":
                        list.print_all()
                    else:
                        log.log_command_invalid(line)
                        continue
        else:
            log.log_command_invalid(line)
            continue                        