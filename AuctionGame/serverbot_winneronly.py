import select
import socket
import sys
import random
import time
import os
import platform

bot = True #This will change the interface and a few sleep statements of the server, it has two settings
#one for bot play and one for manual play
numbidders = 4 #change this for how many bots you want to play with
HOST = 'localhost' #change this to your own IP address if you want to use it over LAN/Wifi

if platform.system() == 'Windows':
  os.system('cls')
else:
  os.system('clear')
#if not bot:
#  print "Server initiated, waiting for players to connect.\n"
#else:
#  print "Server initiated, waiting for bots to connect.\n"

PORT = 50018              # Arbitrary non-privileged port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(7)
input = [server]
bidderids = []
neededtowin = 3 # how many items each player needs to win
itemtypes = ['Picasso', 'Van_Gogh', 'Rembrandt', 'Da_Vinci'] # four different types
maxbudget = 100 # budget per player
won = {}
listtosend = str(numbidders) + ' '
typearray = []
i = 0
#Generate itemsinauction and string containing number of bidders and 
#items in auction list to send to the client
while(i < 200):
  x = itemtypes[int((len(itemtypes))*random.random())]
  typearray.append(x)
  listtosend = listtosend + x + ' '
  i+= 1

# distribute list to send to everyone
bidderids = []
readybidders = []
flag1 = True
#Outer loop waits until every client has been told that the server is
#ready to receive bids

while(numbidders > len(readybidders)):
  inputready,outputready,exceptready = select.select(input,[],[])
  for s in inputready:
    if s == server:
      # print "In server case"
      client, address = server.accept()
      input.append(client)
    if((s != server) & (s!=sys.stdin)):
      data = s.recv(1024)
      # if not data: 
        # print "Have not received data from", str(s)
      indata = data.split(" ")
      # print ' '.join(indata)
      if(indata[0] in bidderids):
        #Waits until all bidders have connected, and then
        #starts telling clients that the server is ready to recieve bids
        if len(bidderids) == numbidders:
          if flag1:
            # if not bot:
            #  print "everyone has connected, let's go!\n"
            #else:
            #  print "everyone has connected, let the Bot Battles begin!"
            # time.sleep(2)
            flag1 = False
          if indata[0] in readybidders:
            pass
          else:
            #If first time telling client they are ready send list of names of players
            stringtosend = 'ready '
            for name in bidderids:
              stringtosend += name + ' '
            s.send(stringtosend)
            readybidders.append(indata[0])
        else:
          #Tell the client to wait if still waiting for people to connect
          s.send('wait ')
        #s.send("Not ready " + indata[0] )
      else:
        #If they just connected first time, send the string with
        #number of bidders and items in auction
        s.send(listtosend)
        bidderids.append(indata[0])
        #print indata[0], "joined the game"
		
won['Picasso'] = {name: 0 for name in bidderids}
won['Van_Gogh'] = {name: 0 for name in bidderids}
won['Rembrandt'] = {name: 0 for name in bidderids}
won['Da_Vinci'] = {name: 0 for name in bidderids}
moneyspent = {name: 0 for name in bidderids}
players = bidderids
doneflag = 0 # will be done only if someone wins or goes over budget with money spent
j = 0
while(0 == doneflag):
  if platform.system() == 'Windows':
    os.system('cls')
  else:
    os.system('clear')
  #generate list to decide when to tell people to hurry up
  start = time.time()
  hurried = [False for i in range(201)]
  hurried[20] = True
  for i in range(20, 201, 10):
    hurried[i] = True
  #print "Auction round", str(j+1) + ':'
  #print
  #if not bot:
    #if j != 0:
    #  print winnerid, "bought a", mytype, "for", bestbid
    #  print
    #print "Current standings are:\n"
    #for player in players:
    #  print player + ':', {'money': 100-moneyspent[player], 'Picasso': won['Picasso'][player], "Rembrandt": won['Rembrandt'][player], "Da_Vinci": won['Da_Vinci'][player], "Van_Gogh": won['Van_Gogh'][player]}
    #print
  mytype = typearray[j]
  #print "We are currently bidding for a", mytype + '.'
  #print
  bidderids = []
  bids = []
  flag2 = True
  #Keep checking for bids until all are received
  #And tell people to hurry up if it is not a bot round
  while(numbidders > len(bidderids)):
    inputready,outputready,exceptready = select.select(input,[],[])
    timePassed = int(time.time()-start)
    if hurried[timePassed]:
      hurried[timePassed] = False
      #for player in players:
      #  if not player in bidderids:
      #    print player + ',',
      #print("hurry up!")
    for s in inputready:
      if s == server:
        # print "In server case"
        client, address = server.accept()
        input.append(client)
      if((s != server) & (s!=sys.stdin)):
        data = s.recv(1024)
        #if not data: 
        #  print "Have not received data from", str(s)
        indata = data.split(" ")
        # print ' '.join(indata)
        #Tell the client to wait until all bids have been received
        if(indata[0] in bidderids):
          s.send('wait ')
          #s.send("Not ready " + indata[0] + " to tell you about move " + str(j+1) )
        else:
          x = int(indata[1])
          if (x > (maxbudget - moneyspent[indata[0]])):
            x = -1 # indata[0] is not allowed to bid over budget
          bids.append(x)
          bidderids.append(indata[0])
          s.send('bid received')
          #if not bot:
          #  print "received bid of", "from", indata[0]
          #else:
          #  print "received bid of", x, "from", indata[0]
          #  print
          # print "number of bids received is: ", len(bidderids)
  # Now have all the bids
  bestbid = max(bids)
  # print "Best bid for step ", j, " is ", bestbid
  # print "Here are the identifiers of the bidders " 
  # print bidderids
  # print "Here are the bids "
  # print bids
  #winnerid=bidderids[random.choice([x for x in range(len(bids)) if bids[x]==bestbid])]
  winnerid = bidderids[bids.index(bestbid)]
  won[mytype][winnerid]+= 1
  moneyspent[winnerid]+= bestbid
  #if bot:
    # time.sleep(1.5)
    #print
    #print winnerid, "bought a", mytype, "for", bestbid
    #print
    # time.sleep(2)
    #print
    #print "Current standings are:\n"
    #for player in players:
    #  print player + ':', {'money': 100-moneyspent[player], 'Picasso': won['Picasso'][player], "Rembrandt": won['Rembrandt'][player], "Da_Vinci": won['Da_Vinci'][player], "Van_Gogh": won['Van_Gogh'][player]}, "\n"
    #print
    # time.sleep(6)
  if (won[mytype][winnerid] >= neededtowin):
    doneflag = 1
    if platform.system() == 'Windows':
      os.system('cls')
    else:
      os.system('clear')
    outfile = open("outfile", "a")
    outfile.write(str(winnerid))
    #print  winnerid, "has won."
    #print "Please close all child processes and this one"
  # Now receive requests for results
  deletedindexes = [] # record which indexes are gone
  while(numbidders > len(deletedindexes)):
    inputready,outputready,exceptready = select.select(input,[],[])
    for s in inputready:
      if((s != server) & (s!=sys.stdin)):
        data = s.recv(1024)
        #if not data: 
        #  print "Have not received data from", str(s)
        indata = data.split(" ")
        # print ' '.join(indata)
        myindex = bidderids.index(indata[0])
        if(myindex not in deletedindexes):
          deletedindexes.append(myindex)
          # s.send(bidderids[myindex] + ' you have bought this item of type ' + mytype)
          #Sending this message will also by not being wait tell the client that it's ready to 
          #receive results
          if(doneflag == 1):
            s.send(winnerid + ' has bought ' + mytype + ' for ' + str(bestbid) + ' and won.')
          else:
            s.send(winnerid + ' has bought ' + mytype + ' for ' + str(bestbid))
        else:
          s.send('ready')
          #s.send("Not ready for next round yet " + indata[0])
  j+=1

time.sleep(4)