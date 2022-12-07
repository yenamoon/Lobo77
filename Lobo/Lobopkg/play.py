import random as rd

class Lobo77: 
  
  game_deck = list(range(0,12))
  total = 0
  
  def __init__(self):
    self.player = []
    self.computer = []
  
  def total11n(total) :
    return total !=0 and total % 11 == 0

  def total77(total) :
    return total >= 77
  
  def start_deck(self):
    self.player = rd.sample(Lobo77.game_deck, 5)
    print('당신의 카드입니다.')
    print('나의 카드 = ' , self.player)
    print()
    self.computer = rd.sample(Lobo77.game_deck, 5)
    print('computer도 카드를 뽑았습니다.')
    print()
 
  def give(self) :
    try :
      give_deck = int(input('낼 카드를 선택하세요 : '))
      self.player.remove(give_deck)
    except :
      print()
      print('입력이 정확하지 않습니다')
      print('카드를 다시 선택해주세요')
      print()
      Lobo77.give(self)
    else :
      print('내가 낸 카드 :', give_deck)
      Lobo77.total += give_deck
      print()

  def draw(self) :
    print('내 카드를 한장 뽑습니다')
    new_deck = rd.choice(range(0,12))
    print('새로 뽑은 카드 : {}'.format(new_deck))
    self.player.append(new_deck)      
    print(self.player)
    print()

    #################################################
  def com_give(self) :
    give_deck = rd.choice(self.computer)
    self.computer.remove(give_deck)
    Lobo77.total += give_deck
    print('컴퓨터가 낸 카드 :', give_deck)
    print()
    
  def com_draw(self) :
    new_deck = rd.choice(range(0,12))
    self.computer.append(new_deck)          