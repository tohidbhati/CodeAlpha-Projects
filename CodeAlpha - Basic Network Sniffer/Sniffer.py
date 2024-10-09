#Importing the Important Libraries for tool 
import pyfiglet
from scapy.all import *
from prettytable import PrettyTable

# Adding Basic Introduction And Instruction For Using The Tool

banner = pyfiglet.figlet_format("Sniffer")
print(banner)
print("WELCOME TO BASIC PACKET SNIFFER...............")
print("This Tool Will Capture The Network Traffic (Infinitely) until the user stops it !!!!!!")
print("Disclaimer: This Tool is Just For Educational and Learning Purposes, and There Should")
print("be no misuse of this tool....")
print("Hope You Will Use it Fairly.....")
print("----------------------------------------------------------------------------------------------")
print("For Start Sniffing Press [1]")
print("For Exit Press [0]")
print("For Stopping the Process Press [Ctrl + C]")

num = int(input("Enter The Value: "))
if num == 1:
    table = PrettyTable()
    table.field_names = ["Source IP", "Destination IP", "Protocol", "Length"]    #<--- Helps In Maintaining The Table Format of all the sniffed data

    def packet_callback(packet):            #<---- Will Sniff the packets 
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            protocol = packet[IP].proto
            length = len(packet)
            table.add_row([ip_src, ip_dst, protocol, length])
            print(table)

    try:
        sniff(prn=packet_callback, count=0)  # count=0 for infinite sniffing
    except KeyboardInterrupt:
        print("\nSniffer stopped by user.")
elif num == 0:                                          #<-------- Exit If [0] is pressed
    print("Exiting the tool.")
    exit()
else:                                        #<---------- If User Gives Another Values Other than specified 
    print("Please Give the Correct Value !!!!")
