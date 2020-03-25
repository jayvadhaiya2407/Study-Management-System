#Study Managment System.......

#Importing Moduls
import datetime


#Getting Current Time
def get_time():
	return datetime.datetime.now()

#Creating Main Menu	
def main_menu():
	print()
	print("!-----------------------------!")
	print("\tSUBJECTS")
	print("!-----------------------------!")
	print("\t1. ACP")
	print("\t2. DBMS")
	print("\t3. DM")
	print("\t4. DHTML")
	print("!-----------------------------!")
	ch = int(input("Enter Subject Number :\n"))
	return ch
	
#Creatingn Sub Menu
def sub_menu():
	print()
	print("!-------------------------!")
	print("\tA. Prectical")
	print("\tB. Theorical")
	print("!-------------------------!")
	ch = input("Enter Your Choice :\n")
	return ch
	
#Creating Menu
def menu():
	print()
	print("!------------------------------!")
	print("\t1. Insert Data")
	print("\t2. Display Data")
	print("\t3. Exit")
	print("!------------------------------!")
	ch = int(input("Enter Your Choice :\n"))
	return ch
	
#Creating Main Function
def main():
	while True:
		choice = menu()
		if choice == 1:
			s_choice = main_menu()

			if s_choice == 1:
				t_choice = sub_menu()
				
				if t_choice.upper() == 'A':
					fp = open("acp_prectical.txt","a+")
					dt = get_time()
					data = input("Enter Your Data :\t")
					fp.write(str(dt))
					fp.write(' :- ')
					fp.write(data)
					fp.write('\n')			
				else:
					fp = open("acp_theory.txt","a+")
					dt = get_time()
					data = input("Enter Your Data :\t")
					fp.write(str(dt))
					fp.write(' :- ')
					fp.write(data)				
					fp.write('\n')
					
			elif s_choice == 2:
				t_choice = sub_menu()
				if t_choice.upper() == 'A':
					fp = open("dbms_prectical.txt","a+")
					dt = get_time()
					data = input("Enter Your Data :\t")
					fp.write(str(dt))
					fp.write(' :- ')
					fp.write(data)
					fp.write('\n')
				else:
					fp = open("dbms_theory.txt","a+")
					dt = get_time()
					data = input("Enter Your Data :\t")
					fp.write(str(dt))
					fp.write(' :- ')
					fp.write(data)
					fp.write('\n')
				
			elif s_choice == 3:
				fp = open("dm.txt","a+")
				dt = get_time()
				data = input("Enter Your Data :\t")
				fp.write(str(dt))
				fp.write(' :- ')
				fp.write(data)
				fp.write('\n')
				
			elif s_choice == 4:
				t_choice = sub_menu()
				if t_choice.upper() == 'A':
					fp = open("dhtml_prectical.txt","a+")
					dt = get_time()
					data = input("Enter Your Data :\t")
					fp.write(str(dt))
					fp.write(' :- ')
					fp.write(data)
					fp.write('\n')
				else:
					fp = open("dhtml_theory.txt","a+")
					dt = get_time()
					data = input("Enter Your Data :\t")
					fp.write(str(dt))
					fp.write(' :- ')
					fp.write(data)
					fp.write('\n')
			else:
				print("Something Went Wrong!!")
		
		#Displaying Data From The File
		elif choice == 2:
			s_choice = main_menu()

			if s_choice == 1:
				t_choice = sub_menu()
				
				if t_choice.upper() == 'A':
					fp = open("acp_prectical.txt","r")
					for line in fp:
						print(line)
				
				else:
					fp = open("acp_theory.txt","r")
					for line in fp:
						print(line)				
				
			elif s_choice == 2:
				t_choice = sub_menu()
				if t_choice.upper() == 'A':
					fp = open("dbms_prectical.txt","r")
					for line in fp:
						print(line)
				
				else:
					fp = open("dbms_theory.txt","r")
					for line in fp:
						print(line)
				
			elif s_choice == 3:
				fp = open("dm.txt","r")
				for line in fp:
						print(line)
										
			elif s_choice == 4:
				t_choice = sub_menu()
				if t_choice.upper() == 'A':
					fp = open("dhtml_prectical.txt","r")
					for line in fp:
						print(line)
				
				else:
					fp = open("dhtml_theory.txt","r")
					for line in fp:
						print(line)
			else:
				print("Something Went Wrong!!")
		else:
			break
			
			
#Starting Of The Programe
main()