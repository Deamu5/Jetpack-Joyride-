from colorama import *
RESET= '\x1b[0m'
class Person:
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	def travel(self):
		pass
	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self,cc):
		self.__x=cc
	@property
	def y(self):
		return self.__y
	@y.setter
	def y(self,cc):
		self.__y=cc
class Art:
	def __init__(self,grid):
		self.bullet= Fore.BLUE + '<' + RESET
		self.bullist=[]
		self.bullxco=[]
		self.bullyco=[]
		with open("dragon.txt") as fl_in:
		    lnes = fl_in.readlines()
		for i in range(5,5+len(lnes)):
			for j in range(1758,1758+len(lnes[i-5])):
				if lnes[i-5][j-1758] == '\t' or lnes[i-5][j-1758]=='\n':
					grid[i][j]=' '
				else:
				   	grid[i][j]=lnes[i-5][j-1758]

	def print(self,x,grid):
		with open("dragon.txt") as fl_in:
		    lnes = fl_in.readlines()
		if x<15:
			for i in range(x,x+len(lnes)):
				for j in range(1758,1758+len(lnes[i-x])):
					if lnes[i-x][j-1758] == '\t' or lnes[i-x][j-1758]=='\n':
						grid[i][j]=' '
					else:
					   	grid[i][j]=lnes[i-x][j-1758]
		elif x>15:
			for i in range(14,14+len(lnes)):
				for j in range(1758,1758+len(lnes[i-14])):
					if lnes[i-14][j-1758] == '\t' or lnes[i-14][j-1758]=='\n':
						grid[i][j]=' '
					else:
				   		grid[i][j]=lnes[i-14][j-1758]

	def cleardrag(self,grid):
		for i in range(1,29,1):
			for j in range(1757,1799,1):
				grid[i][j]=" "

	def fire(self,x,grid):
		dy=1757
		if x >=14:
			for i in range(14,28,4):
					grid[i][dy]="<"
					self.bullist.append("<")
					self.bullxco.append(i)
					self.bullyco.append(dy)
		if x<14:
			for i in range(x,x+14,4):
					grid[i][dy]="<"
					self.bullist.append("<")
					self.bullxco.append(i)
					self.bullyco.append(dy)
	def trav(self,grid):
		for i in range(len(self.bullist)):
			if self.bullist[i]!=0:
				grid[self.bullxco[i]][self.bullyco[i]]=" "
				grid[self.bullxco[i]][self.bullyco[i]-1]="<"
				self.bullyco[i]-=1
		
