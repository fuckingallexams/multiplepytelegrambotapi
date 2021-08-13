# coding=utf-8
import sys,time,threading,os
import bot_group_config as b_g_c

windows_proxychains_socks = w_p_s = '''proxychains -f p8081.conf '''
linux_torsocks_socks = l_t_s = '''torsocks '''
runbot_command = '''python {name} {api_token}'''

def run_bot(name,api_token):
    os.system(windows_proxychains_socks + runbot_command.format(name=name,api_token=api_token))

#print(b_g_c.c)
for k,v in b_g_c.c.items():
    #print(k)
    #print(v)
    v["o1"] = threading.Thread(target=run_bot, args=("bot_group.py",v["api_token"],))
    v["o1"].start()
    
for k,v in b_g_c.c.items():
    #print(k)
    #print(v)
    v["o1"].join()
