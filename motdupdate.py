#!/usr/bin/python3
#By Paul Hansen
#A simple example that showcases my python scripting abilities.

motdn = open('/etc/motd', 'r')
print("Current motd: ", motdn.read())
motdn.close

changeo=0

while changeo not in ('y','yes','n','no'):
    changeo= input("Do you want to update the message of the day? (yes/y/no/n): ")

if changeo in ("yes","y"):
    newhn=input("Specify a new message: ")
    motdnew = open('/etc/motd', 'w')
    motdnew.write(newhn)
    print("Update successful!")
    motdnew.close

elif changeo in ("no","n"):
    print("Cool")

else:
    print("This shouldn't happen...")
