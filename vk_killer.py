#!/usr/bin/env python2
import vk_api
import getpass
import random
import time
import os
import sys

os.system("clear")
print("Hello! I'm VK_API based app")
login = input("Login: ")
password = getpass.getpass("Password(Hidden!): ")

sess = vk_api.VkApi(login, password)
sess.auth()
vk = sess.get_api()

def sleepTime(t):
 print("I want to sleep...")
 toolbar_width = 50
 sys.stdout.write("[%s]" % ("-" * toolbar_width))
 sys.stdout.flush()
 sys.stdout.write("\b" * (toolbar_width+1))
 for i in range(toolbar_width):
  time.sleep(t)
  sys.stdout.write("#")
  sys.stdout.flush()
 print()
 print("I've sleeped enough! Let's continue!")
def message():
    users = input("Number of targets: ")
    userID = list()
    for i in range(int(users)):
     userID.append(input("Target user Domain (for example: iamivan or id12345678): "))
    msg = list()
    atc = list()
    n = input("Number of different messages: ")
    for i in range(int(n)):
     msg.append(input("message: "))
    isAtch = input("Use attachments? (y/n) ")
    if isAtch == 'y':
     for i in range(int(n)):
      atc.append(input("attachment id: "))
      
    threads = input("Threads: ")
    
    
    for i in range(int(threads)):
     if(i%6 == 0 and i != 0):
      sleepTime(0.18)
     if(i%19 == 0 and i != 0):
      sleepTime(0.5)
      
     rn = random.randint(0, int(n)-1)
     if int(n) == 1: rn = 0
     msg1 = str(msg[rn])
     atc1 = ''
     if isAtch == 'y':
      rn = random.randint(0, int(n)-1)
      if int(n) == 1: rn = 0
      atc1 = str(atc[rn])
     for j in range(int(users)):
      vk.messages.send(
         domain = userID[j],
         random_id = random.randint(10000000, 99999999),
         message = msg1,
         attachment = atc1
      )
     time.sleep(1)
     print("I've sent "+str(i+1)+" messages!")
message()
print("Done!")
