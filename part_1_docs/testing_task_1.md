### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # should be == not =
    if card.value = 1:
      return True
      #else should have : at the end
    else
      return False
   

# spelling error should be def and should have a comma after card1
  dif highest_card(self, card1 card2):
  #if statement should be indented
  if card1.value > card2.value:
    # should be return card1 as card is not being passed in
    return card
  else:
    return card2
  

# should be indented so its within the cardgame class
def cards_total(self, cards):
  # total should be total = 0 for it to start at 0
  total
  for card in cards:
    total += card.value
    # return should not be indented
    # of needs a space after and need + str(total) to convert to string
    return "You have a total of" + total
  
```
