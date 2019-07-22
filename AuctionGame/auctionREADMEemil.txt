Hi Dennis,

For running the game all you have to do is run the server first having changed the variables "bot" to true/false depending on if you're playing with bots or with humans, and then change the number of players to the relevant amount. After this you simply connect the clients, input your name and everything else will work.

All variables that a person that would like to use the games are at the very top just under the import statements seperate from the rest of the code and comments beside them telling them what they do. For server it's number of players, bot or not, and server IP / localhost. Only server/localhost for the clients.

One thing to be aware of is in the clients I imported the print function from python 3, because I really wanted the "end = ..." argument in the print function. So all print functions in the client need brackets around them.

Currently in the bot I made the sleep statement before bidding 1 second, also because when I ran the server on localhost that makes it a lot faster so 0.4 wasn't enough on my computer either. You can either just keep it on 1, and then I don't believe there could be any problems no matter how fast your computer or internet is.

The comments are a bit messy right now as there are your old comments, commented out code and then my new comments but I think it should be readable. 

All the best, and if you have any questions of course just ask away.