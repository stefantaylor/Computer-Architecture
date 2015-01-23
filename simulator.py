#CAR Assignment 1
#Stefan Taylor
#s1006260
import sys

def dynamic(inputfile): #Method for dynamic Branch Prediction. Not working as intended
	print('Dynamic Branch Prediction')
	print(inputfile)
	f = open(inputfile, 'r')
	line = "starto!"
	mispredictions = 0
	total = 0
	table = []
	i = 0
	j = 0
	k = 0
	l = 0
	while line != "":
		line = f.readline()
		found = 0
		if line != "":
			total += 1
			hexaddress = line[2:8]
			binaddress = bin(int(hexaddress, 16))[2:].zfill(48)
			for count in range(0, len(table)):
				if binaddress not in table[count]:
					found = 0
				else:
					found = 1
					if table[count][48:] == "00":
						branchprediction = 0
						i+=1
						if branchprediction != line[9]:
							mispredictions += 1
							table[count] = table[count][0:48] + "01"
						break
						
					elif table[count][48:] == "01":
						branchprediction = 0
						j+=1
						if branchprediction != line[9]:
							mispredictions += 1
							table[count] = table[count][0:48] + "10"
							break
						else:
							table[count] = table[count][0:48] + "00"
							break
						
					elif table[count][48:] == "10":
						branchprediction = 1
						k+=1
						if branchprediction != line[9]:
							mispredictions += 1
							table[count] = table[count][0:48] + "01"
							break
						else:
							table[count] = table[count][0:48] + "11"
							break
						
					elif table[count][48:] == "11":
						branchprediction = 1
						l+=1
						if branchprediction != line[9]:
							mispredictions += 1
							table[count] = table[count][0:48] + "10"
						break
						
			if found == 0:
				table.append(binaddress + "00")
				branchprediction = 0
				if branchprediction != line[9]:
					mispredictions += 1
	
	print ("i:" + str(i) + " j:" + str(j) + " k:" + str(k) + " l:" + str(l))
	print (i+j+k)
	print (str(mispredictions) + " mispredictions")
	print (str(total) + " total")
	print("\nMisprediction Rate: " + str(float(mispredictions)/float(total)*100) + " %")
	print("Using file " + inputfile + "\n")


def staticTaken(inputfile): #Method Simulating Static Branch Prediction Assuming All Branches Taken
	print('\nStatic Branch Prediction: Assuming Taken')
	
	#Initialises Some Variables
	branchprediction = "1"
	mispredictions = 0
	total = 0
	f = open(inputfile, 'r')
	line = "starto!"

	#Loops through all the entries in the .out files line by line, looking at
	#whether they branched or not and counting the mispredictions. Assumes no
	#empty lines in the .out file
	while line != "":
		line = f.readline()
		if line != "":
			total +=1
			if branchprediction != line[9]:
				mispredictions += 1

	#Prints the Misprediction rate along with the file that was looked at
	print("\nMisprediction Rate: " + str(float(mispredictions)/float(total)*100) + " %")
	print("Using file " + inputfile + "\n")

def staticNotTaken(inputfile): #Method Simulating Static Branch Prediction Assuming No Branches Taken
	print('\nStatic Branch Prediction: Assuming Not Taken')
	
	#Initialises Some Variables
	branchprediction = "0"
	mispredictions = 0
	total = 0
	f = open(inputfile, 'r')
	line = "starto!"

	#Loops through all the entries in the .out files line by line, looking at
	#whether they branched or not and counting the mispredictions. Assumes no
	#empty lines in the .out file
	while line != "":
		line = f.readline()
		if line != "":
			total +=1
			if branchprediction != line[9]:
				mispredictions += 1

	#Prints the Misprediction rate along with the file that was looked at

	print("\nMisprediction Rate: " + str(float(mispredictions)/float(total)*100) + " %")
	print("Using file " + inputfile + "\n")

def staticProfiling(inputfile): #Not implemented
	print('Static Branch Prediction: Profiling')
	print('Sorry not implemented')
	#stuff

# Main

args=len(sys.argv)

if args == 1:
	print('Please provide a filename e.g. gcc_branch.out')

if args == 2:
	print('Please provide an additional argument describing which type of Branch Prediction you want,')
	print('s for a form of static branch prediction,')
	print('or d for dynamic branch prediction,')

elif args > 4:
	print('!!!Error: Too many arguments. Use:')
	print('s for a form of static branch prediction,')
	print('or d for dynamic branch prediction,')


elif args == 3:

	if sys.argv[2] == 'd':
		filename=sys.argv[1]
		dynamic(filename)

	elif sys.argv[2] == 's':
		print('Provide an additional argument describing which type of Static Branch Prediction you want')
		print('y for always taken')
		print('n for always not taken')
		print('p to use profiling')
	else:
		print('!!!Error: Check command line arguments. Use:')
		print('s for a form of static branch prediction,')
		print('or d for dynamic branch prediction,')

elif args == 4:
	if sys.argv[2] == 's':
		if sys.argv[3] == 'y':

			filename=sys.argv[1]
			staticTaken(filename)

		elif sys.argv[3] == 'n':

			filename=sys.argv[1]
			staticNotTaken(filename)


		elif sys.argv[3] == 'p':

			filename=sys.argv[1]
			staticProfiling(filename)

		else:
			print('!!!Error: Check second argument. Use:')
			print('y for always taken')
			print('n for always not taken')
			print('p to use profiling')
	else:
		print('!!!Error: Check command line arguments. Use:')
		print('s for a form of static branch prediction,')
		print('or d for dynamic branch prediction,')


# ----------------------------------------------------------------------------------------------- #

# ****************************   ___________   ___ _____  ____ ____   *************************** #
# ****************************  / ___/      | /  _]     |/    |    \  *************************** #
# **************************** (   \_|      |/  [_|   __|  o  |  _  | *************************** #
# ****************************  \__  |_|  |_|    _]  |_ |     |  |  | *************************** #
# ****************************  /  \ | |  | |   [_|   _]|  _  |  |  | *************************** #
# ****************************  \    | |  | |     |  |  |  |  |  |  | *************************** #
# ****************************   \___| |__| |_____|__|  |__|__|__|__| *************************** #

# ----------------------------------------------------------------------------------------------- #





