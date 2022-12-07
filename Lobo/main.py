from Lobopkg.play import *

print('Lobo 77에 오신 여러분 환영합니다!!')
print('이제 카드 5장을 배분하겠습니다.')
print()

game = Lobo77()
game.start_deck()

while True :
    game.give()
    if Lobo77.total11n(Lobo77.total) ==  True :
      print('카드의 총합이 {}로 11의 배수 입니다'.format(Lobo77.total))
      print('당신의 패배')
      print('게임이 종료되었습니다')
      break
    elif Lobo77.total77(Lobo77.total) == True :
      print('카드의 총합이 {}로 77 이상 입니다'.format(Lobo77.total))
      break
    game.draw()
    game.com_give()
    if Lobo77.total11n(Lobo77.total) ==  True :
      print('카드의 총합이 {}로 11의 배수 입니다'.format(Lobo77.total))
      print('당신의 승리')
      print('게임이 종료되었습니다')
      break
    elif Lobo77.total77(Lobo77.total) == True :
      print('카드의 총합이 {}로 77 이상 입니다'.format(Lobo77.total))
      break
    game.com_draw()