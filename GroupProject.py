print('How Well Do You Know PYTHON T/F Quiz')
score = 0
total_questions = 10

answer = input('Question 1: Information is often referred to as data? ')
if answer.lower() == 'true':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 2: A modern computer system consists of hardware and software? ')
if answer.lower() == 'true':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 3: Memory is a basic hardware component of a computer? ')
if answer.lower() == 'true':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 4: RAM stands for Randomized Algorithmic Memory? ')
if answer.lower() == 'false':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 5: HTTP stands for hypertext translate processor? ')
if answer.lower() == 'false':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 6: HTML stands for hypertext markup language? ')
if answer.lower() == 'true':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 7: Steve Jobs created Python? ')
if answer.lower() == 'false':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 8: Python was launched in the 90s? ')
if answer.lower() == 'true':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 9: Python can be used to build websites? ')
if answer.lower() == 'true':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('Question 10: Python was the first computer programming language? ')
if answer.lower() == 'false':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

print('END GAME You scored', score,)
mark = (score / total_questions) * 10
print('Score:', mark)

