#!/usr/bin/env python3

#place this script in /usr/local/bin

import paramiko
import os
from tkinter import *
from tkinter import filedialog
from tkinter import font

#root = Tk()
#root.title('Message over SSH')
#root.geometry("1200x600")

#create the main frame

#my_frame = Frame(root)
#my_frame.pack(pady=5)

#def ssh_command(ip, port, username, password, command='pwd; ls'):
def userMessage(message):
    message  = input("What do you want to send?")

def sshCommand(ip, port, username, password, command):

    #paramiko.util.log_to_file("filename.log")

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

#root.mainloop()

ip = input("What IP is your server? ")
port = input("What port do you want to connect to? ")
username = input("Machine username: ")
password = input("Machine password: ")

sshCommand(ip, port, username, password, command="python3 messagingserver.py")

#python3 messagingserver.py
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('192.168.1.64', port=22, username='pi', password='eqmcamemcc')

#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls -a")

#cd .local; cd lib; cd python3.5; cd site-packages;

