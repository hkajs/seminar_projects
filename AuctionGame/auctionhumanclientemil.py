from __future__ import print_function #I added this because it made my life a lot easier when
#the 'end = ...' function was added in the print function that I didn't know a nice way to do
#in Python 2.7, so print statements must all have brackets in this version, no need in the server though
# Echo client program
import socket
import random
import time
import os
import platform


HOST = 'localhost'   # The remote host

# to act as a client
PORT = 50018              # The server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# APPLICATION

partnerid = -1 # no partner
numberbidders = 0 # will be given by server

# DO SOMETHING HERE
# you need to change this to do something much more clever
def determinebid(itemsinauction, partnerid, numberbidders, winnerarray, winneramount):
  #if you have no money automatically bid 0
  if myTypes['money'] == 0:
    return 0
  #Otherwise input bid and check that it's a number
  output = raw_input("Input bid: ").strip()
  while(not (len(output) > 0 and output.isdigit())):
    output = raw_input("Input bid: ")
  return int(output)

# DATA

mybidderid = raw_input("Input team / player name : ").strip()  # this is the only thing that distinguishes the clients 
while len(mybidderid) == 0 or ' ' in mybidderid:
  mybidderid = raw_input("You input an empty string or included a space in your name which is not allowed (_ or / are all allowed)\n for example Emil_And_Nischal is okay\nInput team / player name: ").strip()

moneyleft = 100 # should change over time
winnerarray = [] # who won each round
winneramount = [] # how much they paid

itemsinauction = []
myTypes = {'Picasso': 0, 'Rembrandt': 0, 'Van_Gogh': 0, 'Da_Vinci': 0, 'money': moneyleft}

# EXECUTION

# get list of items and types
getlistflag = 1
s.send(str(mybidderid))
while(getlistflag == 1):
  # print "Have sent data from ", str(mybidderid)
  data = s.recv(5024)
  x = data.split(" ")
  # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
  # Receives first how many players are in the game and then all 200 items in auction
  if(x[0] != "Not" and len(data) != 0):
    getlistflag = 0
    numbidders = int(x[0])
    itemsinauction = x[1:]
    for index in range(len(itemsinauction)-1, -1, -1):
      print (str(index+1) + '.', itemsinauction[index])
    print ('\n')
  else:
    time.sleep(2)

while True:
  s.send(str(mybidderid) + ' ')
  data = s.recv(5024)
  x = data.split(" ")
  #Wait until everyone has connected before bidding
  if (x[0] == 'wait'):
    continue
  #When everyone has connected the server knows all names
  #it can therefore transfer all the names after telling the client that it's ready
  players = []
  for player in range(1, numbidders + 1):
    players.append(x[player])
  break
#Create initial standings for each player after everyone connected
standings = {name: {'Picasso': 0, 'Van_Gogh': 0, 'Rembrandt': 0, 'Da_Vinci': 0, 'money': 100} for name in players}
# now do bids
continueflag = 1
j = 0
#Interface stuff, looks better if I clear the screen before writing all the info
#but I want to give people time to study the list of itemsinauction properly before
#they start the game. So I ask them when they're ready
raw_input("Hit any key to start the game: ")
if platform.system() == 'Windows':
  os.system('cls')
else:
  os.system('clear')
while(continueflag == 1):
  i = len(winnerarray)  
  print ("Auction round", str(j+1) + ':\n')
  print ("This is everyones standings:\n")
  for name in players:
      print (name + ':', standings[name])
  print()
  print()
  print ("item type: ", itemsinauction[:i])
  print ("Won by:    ", winnerarray[:i])
  print ("Bought for:", winneramount[:i])
  print()
  print()
  print ("next 20 items: ", end = '')
  for add in range(20):
    print (itemsinauction[i+add+1], end = ', ')
  print ('\n')
  print()
  print ("your current holdings are", standings[mybidderid], '\n')
  print ("Current item to be bid for is: " + itemsinauction[i])
  bidflag = 1
  bid = determinebid(itemsinauction, partnerid, numberbidders, winnerarray, winneramount)
  s.send(str(mybidderid) + " " + str(bid))
  while(bidflag == 1):
    # print "Have sent data from ", str(mybidderid)
    data = s.recv(5024)
    x = data.split(" ")
    # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
    if(x[0] != "Not"):
      bidflag = 0
    else:
      time.sleep(2)


  resultflag = 1
  while(resultflag == 1):
    s.send(str(mybidderid))
    # print "Have sent data from ", str(mybidderid)
    data = s.recv(5024)
    x = data.split(" ")
    #Wait for all bids to be received
    if (x[0] == 'wait'):
      continue
    # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
    if platform.system() == 'Windows':
      os.system('cls')
    else:
      os.system('clear')
    #Check if the server told client that game is finished
    if len(x) >= 7 and x[7] == 'won.':
      continueflag = 0
      resultflag = 0
      print(data)
      print()
      print('game over')
    #Else update standings, winnerarray etc.
    if(x[0] != "ready") and (continueflag == 1):
      resultflag = 0
      print (data)
      # print x
      winnerarray.append(x[0])
      winneramount.append(int(x[5]))
      standings[x[0]]['money'] -= int(x[5])
      standings[x[0]][x[3]] += 1
      if (x[1] == mybidderid):
        moneyleft -= int(x[5])
        myTypes[itemsinauction[j]] += 1
      # update moneyleft, winnerarray
    else:
      time.sleep(2)
  j+= 1
  for i in range(2):
    print()
