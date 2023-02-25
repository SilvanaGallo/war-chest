# War Chest Lite

In order to model this game we need to consider different components:

- Board: With a size (n x n). Where each cell could contain a coin, and these cells could be regular, starting zones or neutral zones. In starting zones the players put their Control Markers when the board is initialized. Neutral zones are those that could be controlled for any player. Starting zones are marked with a special signal at the beginning but througout the game they behave like neutral zones. Regular zones allow the placement of different units.

- Players: There are 2 players (wolf and crow) that have 4 random unit types of the 8 possible. Each player has a bag of coins with a royalty unit, and 2 unit coins of each random selected units. Then, each player has C (4 or 6) control markers that have to been placed in neutral or starting zones in order to win the game. Another containers that are used by players are recruitment section (that contains the remaining unit coins), discard stack (that contains the used coins), and the hand (that is composed by 3 unit coins extracted from the bag in each play turn).

- Units: They are materialized by coins. Each coin belongs to a unit role and has a different behavior through actions and its strategy.

- Initiative: One player starts with this token, but it could be claimed by the other player during a "get initiative" action.

In my application model I have included a class to represent the board. It has a n size and a content that is a dictionay with a tuple key and a Unit (see hierarchy below) value. It seems better than a matrix implementation for me in order to simplify the access to different elements. If a cell is controlled, it has a ControlledMarker token in its content.

I have added a hierarchy in order to manage the unit types and movements. I create a Unit abstract class that represents the general methods and attributes and concrete classes for each type of unit with their specific behavior.

## Pending

Reestructure the code in order to add configuration classes and factories that simplifie the tasks
Maybe Units could be singletons in order to simplify
Verify if Royal is better implemented by wrapper functions

========================================================================================================

# Actions

## Initiative and forfeit

Initiative action is managed by the game logic (WarChestGame class) and Player class. WarChestGame class manages a index in order to know at anytime wich player needs to set their initiative, Player class has a boolean attribute to know if the player has or hasn't the initiative.

Initiative and Forfeit actions imply a coin discard process, without distinguishing its unit.

## Recruit process

I have implemented a dinamic function caller in order to select between methods when we encounter a royal or battlefield unit.
