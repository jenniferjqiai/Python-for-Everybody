# Score grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

score = input('Enter score: ')
try:
    score = float(score)
    if 0.9 <= score < 1.0:
        print('A')
    elif score >=0.8 and score <0.9:
        print('B')
    elif score >=0.7 and score <0.8:
        print('C')
    elif score >=0.6 and score <0.7:
        print('D')
    elif score < 0.6:
        print('F')
    else :
        print('Bad score')
except:
    print('Bad Score')

