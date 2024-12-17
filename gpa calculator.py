import math
import time
import save
number_of_classes=8
points = 0
redo = 1
stop_game =0
print("hello")
print('welcome to Centennial gpa calculator')
print('it only supports the grade as decimal form not letter')
while  redo == 1:
    class1 = input('enter your first classes grade:')
    class2 = input('enter your second classes grade:')
    class3 = input('enter your third classes grade:')
    class4 = input('enter your fourth classes grade:')
    class5 = input('enter your fifth classes grade:')
    class6 = input('enter your sixth classes grade:')
    class7 = input('enter your seventh classes grade:')
    class8 = input('enter your eighth classes grade:')
    if class1 == '':
        print('your first class is blank please redo')
        class1 = input('enter your first classes grade')
    if class2 == '':
        print('your first class is blank please redo')
        class2 = input('enter your second classes grade')
    if class3 == '':
        print('your first class is blank please redo')
        class3 = input('enter your third classes grade')
    if class4 == '':
        print('your first class is blank please redo')
        class4 = input('enter your fourth classes grade')
    if class5 == '':
        print('your first class is blank please redo')
        class5 = input('enter your fifth classes grade')
    if class6 == '':
        print('your first class is blank please redo')
        class6 = input('enter your sixth classes grade')
    if class7 == '':
        print('your first class is blank please redo')
        class7 = input('enter your seventh classes grade')
    if class8 == '':
        print('your first class is blank please redo')
        class8 = input('enter your eighth classes grade')
    print("calculating now")
    time.sleep(2)
    class_sum = int(class1) + int(class2) + int(class3) + int(class4) + int(class5) + int(class6) + int(class7) + int(class8)
    gpa = class_sum / number_of_classes
    print(gpa)
    save_file = input('do you want to save to your computer:')
    if save_file == 'yes':
        file_name = input("what do you want to call your save file")
        text = input("what do you want in your text file")
        with open(file_name +".txt","w") as file:
            file.writelines(text +'\n'+ str(gpa))
    if gpa == 4.0:
        game = input('you have done good in class do you want to play a game')
        if game == "yes":
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
                            print('worked')
                if quit_game == 'n':
                    points = points + 1
    time.sleep(2)
    redo=0
    ask = input('redo?:')
    if ask == ('yes'):
        redo = 1
