#!/usr/bin/python

#place this script in /usr/local/bin

import paramiko

#def ssh_command(ip, port, username, password, command='pwd; ls'):
def userMessage(message):
    message  = input("What do you want to send?")

def sshCommand(ip, port, username, password, command):

    paramiko.util.log_to_file("filename.log")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username, password)
    #stdin, stdout, stderr = client.exec_command(command)
    stdin,stdout,stderr = client.exec_command(command)
    #input = stdin.read()
    output = stdout.read()
    #output_error = stderr.read()

    print(output)

    # Close the connect
    client.close()

sshCommand(ip='192.168.1.64', port=22, username='pi', password='eqmcamemcc', command="python messagingserver.py")

