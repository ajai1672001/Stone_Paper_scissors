import random
letters = ['stone',  'paper', 'scissor' ]
player=0
while True:
	com= random.randint(0,len(letters)-1)
	print(f'Enter your choice \n 1. stone \n 2.paper \n3. scissor\n 4. exit game')
	user=int(input())
	if(user>3):
		print('Bye')
		break
	print(f'Computer: {letters[com-1]}\n User :{letters[user-1]}')
		
	if(com==user):
		print("match draw \n do your quit this game press q or Q")
		if(input().lower()=='q'):
			print("Bye")
			break
	elif(com==1 and user== 3):
		print("Computer win")
	elif(com==2 and user==1):
		print("Computer win")
	elif(com==3 and user==2):
		print("Computer win")
	elif(user==1 and com== 3):
		print("User win")
	elif(user==2 and com==1):
		print("User win")
	elif(user==3 and com==2):
		print("User win")
	print('='*10)
