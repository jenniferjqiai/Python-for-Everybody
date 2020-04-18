# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.

s =input('Please enter score :')
try:
    score=float(s)   
    def computegrade(score):
       if 0.9 <= score < 1.0:
                print('A')
       elif score >= 0.8 and score < 0.9:
                print('B')
       elif score >= 0.7 and score < 0.8:
                print('C')
       elif score >= 0.6 and score < 0.7:
                print('D')
       elif score < 0.6:
                print('F')
       else:
                print('Bad score')
    computegrade(score)
except:
    print('Bad score')



