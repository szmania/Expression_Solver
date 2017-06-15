# Poker Hand Ranker

## Description
This applicaiton takes a hand of five cards and determines its rank amongst ten different ranks, 1 being the highest.

### Ranks are a follows
1. Royal Flush
Same as a Straight Flush (below) but with Ace high. For example, heartA-heartK-heartQheartJheart10
is a royal flush.
2. Straight Flush
Five cards of the same suit in sequence - such as clubJ-club10-club9-club8-club7. Optional: An
ace can be counted as low, so heart5-heart4-heart3-heart2-heartA is a straight flush, but its top
card is the five, not the ace, so it is the lowest type of straight flush. The cards cannot "turn the
corner": diamond4-diamond3-diamond2-diamondA-diamondK is not valid.
3. Four of a kind
Four cards of the same rank - such as four queens. The fifth card can be anything. This
combination is sometimes known as "quads", and in some parts of Europe it is called a "poker",
though this term for it is unknown in English.
4. Full House
This consists of three cards of one rank and two cards of another rank - for example three
sevens and two tens (colloquially known as "sevens full" or more specifically "sevens on tens").
5. Flush
Five cards of the same suit. For example, spadeK-spadeJ-spade9-spade3-spade2.
6. Straight
Five cards of mixed suits in sequence - for example spadeQ-diamondJ-heart10-spade9-club8.
Optional: Ace can count high or low in a straight, but not both at once, so A-K-Q-J-10 and 5-4-3-
2-A are valid straights, but 2-A-K-Q-J is not.
7. Three of a Kind
Three cards of the same rank plus two other cards. This combination is also known as Triplets or
Trips. Example 5-5-5-3-2.
8. Two Pairs
A pair is two cards of equal rank. In a hand with two pairs, the two pairs are of different ranks
(otherwise you would have four of a kind), and there is an odd card to make the hand up to five
cards. Example J-J-2-2-4.
9. Pair
A hand with two cards of equal rank and three other cards which do not match these or each
other. Example 6-6-4-3-2.
10. High Card
Five cards which do not form any of the combinations listed above. Example: A-J-9-5-3.


## Usage
### Card Types
All numbered cards are represented by their corresponding number.
"2" = 2, "3" = 3, "7" = 7, "10" =  10 etc...
All face cards are represented by the first letter in their name.
"A" = Ace, "K" = King, "Q" = Queen and "J" = Jack

### Card Suites
All card suites are represented by the first letter in the suite name.
"C" = Clubs, "D" = Diamonds, "H" = Hearts and "S" = Spades

### Arguments
`--card1 <type>,<suite>`

First card in hand, represented by a tuple. ie: 3,D ("Three of Diamonds")
	
`--card2 <type>,<suite>`

Second card in hand, represented by a tuple. ie: J,S ("Jack of Spades")
	
`--card3 <type>,<suite>`

Third card in hand, represented by a tuple. ie: Q,C ("Queen of Clubs")
	
`--card4 <type>,<suite>`

Fourth card in hand, represented by a tuple. ie: A,D ("Ace of Diamonds")
	
`--card5 <type>,<suite>`

Fifth card in hand, represented by a tuple. ie: 2,H ("Two of Hearts")

`--logFile <logging file>`
(Optional) File to output log to. ie: "log.log". Default is "rankHand.log".

`--logLevel <loglevel>`
(Optional) Logging level. ie: "WARN", "INFO", "DEBUG"
	
	
## Examples
### input 1:
`python rankHand.py --card1 A,C --card2 J,S --card3 J,C --card4 K,S --card5 K,C --log WARN`
### output 1:
`Hand is Two Pairs.`

`Rank of hand is 8.`

`Hand: A,C - J,S - J,C - K,S - K,C`
	
	
### input 2:
`python rankHand.py --card1 A,C --card2 J,S --card3 4,D --card4 6,S --card5 K,C`
### output 2:
`Hand is High Card.`

`Rank of hand is 10.`

`Hand: A,C - J,S - 4,D - 6,S - K,C`