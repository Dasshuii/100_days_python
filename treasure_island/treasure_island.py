ascii = '''
                           .
                         .OO
                       .OOOO
                      .OOOO'
                      OOOO'          .-~~~~-.
                      OOO'          /   (o)(o)
              .OOOOOO `O .OOOOOOO. /      .. |
          .OOOOOOOOOOOO OOOOOOOOOO/\    \____/
        .OOOOOOOOOOOOOOOOOOOOOOOO/ \\   ,\_/
       .OOOOOOO%%OOOOOOOOOOOOO(#/\     /.
      .OOOOOO%%%OOOOOOOOOOOOOOO\ \\  \/OO.
     .OOOOO%%%%OOOOOOOOOOOOOOOOO\   \/OOOO.
     OOOOO%%%%OOOOOOOOOOOOOOOOOOO\_\/\OOOOO
     OOOOO%%%OOOOOOOOOOOOOOOOOOOOO\###)OOOO
     OOOOOO%%OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
     OOOOOOO%OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
     `OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
   .-~~\OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
  / _/  `\(#\OOOOOOOOOOOOOOOOOOOOOOOOOOOO'
 / / \  / `~~\OOOOOOOOOOOOOOOOOOOOOOOOOO'
|/'  `\//  \\ \OOOOOOOOOOOOOOOOOOOOOOOO'
       `-.__\_,\OOOOOOOOOOOOOOOOOOOOO'
      jgs  `OO\#)OOOOOOOOOOOOOOOOOOO'
             `OOOOOOOOO''OOOOOOOOO'
               `""""""'  `""""""'''

def main():
    print(ascii)
    print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
    cross_road = input('You\'re at a cross road. Where do you want to go? ').lower()
    if cross_road != 'left':
        print('Fall into a hole.\nGame Over.')
    else:
        lake = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across. ').lower()
        if lake != 'wait':
            print('Attacked by trout.\nGame Over.')
        else:
            door = input('You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose? ').lower()
            if door == 'red':
                print('Burned by fire.\nGame Over.')
            elif door == 'blue':
                print('Eaten by beasts.\nGame Over.')
            elif door == 'yellow':
                print('You Win!')
            else:
                print('Game Over.')


if __name__ == '__main__':
    main()