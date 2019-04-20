Main Plot-point:
The user/character was breaking into this house to steal some cash from a known illicit arms dealer, and was ambushed by one or more of them while 
in the process.. he had help from an insider who knew the house and dealers, which gave him the the access to get inside in the first place, and
the clue for the way out in the basement.  Upon waking up in the starting room, the user now needs to just get out alive by any means necessary, as 
it's just a matter of time before the dealers/killers come back and finish him off.

The user can go from room to room and execute all the existing actions already coded..  Certain rooms will have the KEY items that he will store in 
his BACKPACK (inventory), and will need all of them to ultimately escape the place, via BASEMENT.

Starting Scene:
You wake up in a dark, unfamiliar room that smells of old cedar and stale air. You feel a slight pain and notice there's a bruise and some dried
blood on the back of your head.  Nearby you spot a small backpack on the ground and promptly pick it up, but there's nothing inside.
You mind is still hazy and you struggle to piece together what crazy events must have transpired that have now placed you in your current
situation.

Perhaps you fell... perhaps somebody knocked you out and left you in this strange room for some sinister purpose.. with no real answers and a 
growing sense of dread and urgency, you strap on the backpack in case it might be of some use, and look around the room, deciding on your next
move....

<display possible commands, etc>


Regarding each subsequent room:
Each room can have inconsequential items and actions to take, exactly from lab 12, like laugh, cry, scream, etc.
We can keep the action def functions already implemented to trigger the consequential KEY items (jump, dance, etc) reveal for the four components
the user needs to escape (joker, ace, king, and queen fuses) SEE Basement Scene below for details)

key item locations:
library - KoS fuse
kitchen - QoS fuse
billiardroom - Joker fuse
masterbedroom - AoS fuse

plot item locations:
bathroom - a note from somebody to the player crumpled in the trash telling him to not forget to close and lock the window after he slips in from outide
diningroom - a ledger that has a list of contacts and numerous illegal weapons with dollar amounts associated to them
bedroom - a note under the bed, written from same person who wrote the bathroom note telling user that his cut is 30% of the cash he finds in the house, no
less



Basement Scene:
You make your way down the half-rotted, creaky stairs leading to the basement.  The pale moonlight penetrating the weathered and streaked ground-level
windows provides just enough light for you identify your surroundings and effictively navigate through the labyrithe cellar room.  If only those windows 
were a little larger than size of a pet door, you could claim your freedom, you think to yourself.  In any case, you get to the end of the maze-like room,
and see a large steel-enforced door with 6 two-inch diameter rods securing the door to the granite wall. 

As you look around the room to uncover any clues to unlocking this behemoth of a barrier, you realize there are electric panels on each side of the walls
behind you.  The two walls have three panels each, and what appears to be a space for a fuse of some sort should be inserted.  Two of the panels already have
fuses already inserted.  One has a label of a Jack of Spades in the right most panel on one wall, and one has just an unlabeled fuse in the right-most panel
on the opposite wall.

<showInformation function to display the setup and orientation of the panels>
|****** Wall ********|                   |********* Wall **********|
|--------------------|-------------------|-------------------------|      
| [ unmarked fuse ]  |                   |         [ X ]           |
|--------------------| direction facing  |-------------------------|    
|       [ X ]        |      <----->      |         [ X ]           |
|--------------------|                   |-------------------------|
|       [ X ]        |                   | [ Jack of Spades fuse ] |
|--------------------|-------------------|-------------------------|

A moonbeam through a window illuminates a dusty crumpled piece of paper in the corner of one of the walls. 

<action> read paper
    The note reads: "Hey <user name input>, Murry told me that these bastards rewired the circuit to the transport door, so the fuses need to go in the right order for it to open.  
    I can't remember the whole configuration, but the Ace goes on the same wall with the Jack, the Joker and King are definitely not next to each other, and the Joker 
    and Ace are opposite of each other on the walls."

ANSWER LEGEND for puzzle:  Active Items = [Ace, King, Queen, Joker]  Inactive Items = [unmarked, Jack]
*********************************************************         
* || unlabeled ||                   || King || (slot 3) *
* ---------------                   ------------------- *
* || Joker || (slot 1)    <---->    || Ace || (slot 4)  *
* -----------                       ------------------- *
* || Queen || (slot 2)              || Jack ||          *
*********************************************************

Code logic:
nested if/else statements
variables: slot 1 slot 2 slot 3 slot 4
e.g. if item[0] = joker AND slot[0] = slot 1:
        if ....


Win conditions = make correct configuration in <= 3 attempts (each failed attempt can play unnerving sounds as the enemy or enemies are getting closer)
(Add cool sound effect of the steel door being unlocked and rods moving; sliding heavy metal sounds)

You rush through the opening to a lit path ahead, running almost uncontrollably, never even thinking of looking back, and can taste imminent freedom and relief as you reach the end of the tunnel,
which leads you up a staircase and into the nearby Starbuck's storeroom right down the street from your house!  

Lose conditon = any attemps > 3 (blood curdling scream sound effects of player and of maniacal laughter by the enemy)
