import time
points = 0
stop_game = 0
print('this are the rules and how to play')
print('it will ask  do you quit and if you put yes then the game stops')
print('if you press anything else then it will earn you points and if you press n then you earn points')
time.sleep(2)
print('the game starts now')
while stop_game == 0:
    quit_game= input('do you quit')
    if quit_game == 'yes':
        stop_game = 1
        print(points)
        save_game = input('do you want to save you game points:')
        if save_game == 'yes':
            file_name_game = input('what do you want to name your save file')
            with open(file_name_game +'.txt', 'w') as file:
                file.writelines('points' +'\n'+ str(points))
    if quit_game == 'n':
        points = points + 1
                            