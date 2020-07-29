from objects import Person
import os
from colorama import *
RESET= '\x1b[0m'
force=1
gid=[100]*100
class Mando(Person):
	def __init__(self,x,y,name):   
		Person.__init__(self,x,y)
		self.__shape = [["*"," ","*"],[" ","|"," "],["-"," ","-"]]
		self.__life=100
		self.__coins=0
		self.__coinchar='$'	
		self.__hbeam='%'
		self.__vbeam='#'
		self.__dbeam='@'
		self.__name=name
		self.__bullet='>'
		self.__dragbull='<'
		self.__bullist= []
		self.__bullxc=[]
		self.__bullyc=[]
		self.__bosslife=20

	# global force	
	def initial_pos(self,grid):
		for i in range(26,29,1):
			for j in range(0,3,1):
				grid[i][j]=self.__shape[i-26][j]
	def clear_mando(self,x,y,grid):
		if y>697:
			for i in range(x-2,x+4):
				for j in range(y-2,y+4):
					if grid[i][j]!='=':
						grid[i][j]=" "
		if x<=26 and  x!=1:
		 	for i in range(x-1,x+3,1):
		 		for j in range(y-1,y+3,1):
			 			grid[i][j]=" "
		if x<=26:
			for i in range(x,x+3,1):
				for j in range(y,y+3,1):
					grid[i][j]=" "
	@property	
	def life(self):
		return self.__life
	@life.setter
	def life(self,lif):
		self.__life=lif
	@property
	def coinchar(self):
		return self.__coinchar
	@coinchar.setter
	def coinchar(self,cchar):
		self.__coinchar=cchar	
	@property
	def coins(self):
		return self.__coins
	@coins.setter
	def coins(self,cc):
		self.__coins=cc	
	@property
	def hbeam(self):
		return self.__hbeam
	@hbeam.setter
	def hbeam(self,cc):
		self.__hbeam=cc
	@property
	def vbeam(self):
		return self.__vbeam
	@vbeam.setter
	def vbeam(self,cc):
		self.__vbeam=cc	
	@property
	def dbeam(self):
		return self.__dbeam
	@dbeam.setter
	def dbeam(self,cc):
		self.__dbeam=cc			
	@property
	def bullet(self):
		return self.__bullet
	@bullet.setter
	def bullet(self,cc):
		self.__bullet=cc
	@property
	def dragbull(self):
		return self.__dragbull
	@dragbull.setter
	def dragbull(self,cc):
		self.__dragbull=cc			
	@property
	def bullist(self):
		return self.__bullist
	@bullist.setter
	def bullist(self,cc):
		self.__bullist=cc			
	@property
	def bullxc(self):
		return self.__bullxc
	@bullxc.setter
	def bullxc(self,cc):
		self.__bullxc=cc			
	@property
	def bullyc(self):
		return self.__bullyc
	@bullyc.setter
	def bullyc(self,cc):
		self.__bullyc=cc			
	@property
	def bosslife(self):
		return self.__bosslife
	@bosslife.setter
	def bosslife(self,cc):
		self.__bosslife=cc			
	

	def bull(self,k,x,y,grid):
			grid[x+1][y+3]=self.bullet
			self.bullist.append(self.bullet)
			self.bullxc.append(x+1)
			self.bullyc.append(y+3)
	def travel(self,grid):
			for i in range(len(self.bullist)):
				if grid[self.bullxc[i]][self.bullyc[i]+1]== "$":
					grid[self.bullxc[i]][self.bullyc[i]-1]= " "
					self.bullist[i]="0"
				if grid[self.bullxc[i]][self.bullyc[i]+1]== "$":
					grid[self.bullxc[i]][self.bullyc[i]-1]= " "
					self.bullist[i]="0"	
				if (self.bullist[i]!="0"and grid[self.bullxc[i]][self.bullyc[i]+1]!= "$" and self.bullyc[i]+1 !=1800):
					grid[self.bullxc[i]][self.bullyc[i]-1]=" "
					grid[self.bullxc[i]][self.bullyc[i]]= ">"
					self.bullyc[i]+=1
					if ( grid[self.bullxc[i]][self.bullyc[i]+1] =='%'): #vertical beam				
							self.bullist[i]="0"
							grid[self.bullxc[i]][self.bullyc[i]-1]= " "
							#os.system('clear')
							a=self.bullxc[i]
							b=self.bullxc[i]+1
							while grid[a][self.bullyc[i]+1]=="%" :
								grid[a][self.bullyc[i]+1]=" "
								a-=1
							while grid[b][self.bullyc[i]+1]=="%":
								#print(a,"\t",self.bullyc[i]+1)
								grid[b][self.bullyc[i]+1]=" "
								b+=1
							self.bullist[i]="0"
							grid[self.bullxc[i]][self.bullyc[i]-1]= " "
					if ( grid[self.bullxc[i]][self.bullyc[i]+1] =='#'): #horizontal beam 
							#os.system('clear')
							grid[self.bullxc[i]][self.bullyc[i]-1]=' '	
							for k in range(8):
								grid[self.bullxc[i]][self.bullyc[i]+k]= " "
							self.bullist[i]="0"
					if(grid[self.bullxc[i]][self.bullyc[i]+1]=='@'):
							grid[self.bullxc[i]][self.bullyc[i]+1]=' '
							grid[self.bullxc[i]][self.bullyc[i]-1]=' '
							self.bullist[i]="0"

	def checkb(self,grid):
		for i in range(len(self.bullist)):
			if self.bullist[i]!="0" and grid[self.bullxc[i]][self.bullyc[i]+1] != " " and grid[self.bullxc[i]][self.bullyc[i]+1]!="<" :
				self.bosslife-=1
				self.bullist[i]="0"
		if self.bosslife==0:
			#print(Fore.BLUE +"\tYOU WIN"+RESET )
			for i in range(0,30):
				for j in range(1699,1799):
							grid[i][j]=" "
				print()

			with open("win.txt") as fl_in:
				lnes = fl_in.readlines()
			for i in range(1,len(lnes)):
				for j in range(1711,1711+len(lnes[i-1])):
					if lnes[i-1][j-1711] == '\t' or lnes[i-1][j-1711]=='\n':
						grid[i][j]=' '
					else:
						grid[i][j]=lnes[i-1][j-1711]

			print('\033[0;0H')
			for i in range(0,30):
				for j in range(1699,1799):
					print(grid[i][j],end='')
				print()

			exit()
	def gravity(self,x,fg):
		global force							
		if fg==1:
			force=0
			return self.x
		if force+self.x<=26:
			self.x+=force
			force+=1
		elif force+self.x>=26:
			self.x=26
		if force+self.x==26:
			force=0		
		return self.x
	def move(self,k,x,y,grid):		
		grid[x][y+1]=self.__shape[0][0]
		grid[x][y+2]=self.__shape[0][1]
		grid[x][y+3]=self.__shape[0][2]
		grid[x+1][y+1]=self.__shape[1][0]
		grid[x+1][y+2]=self.__shape[1][1]
		grid[x+1][y+3]=self.__shape[1][2]
		grid[x+2][y+1]=self.__shape[2][0]
		grid[x+2][y+2]=self.__shape[2][1]
		grid[x+2][y+3]=self.__shape[2][2]
	def auto_move(self,x,y,grid):
		self.y=y+2	
	def move_up(self,x,y,grid):
		self.x=x-1
	def move_right(self,x,y,grid):
		self.y=y+2
	def move_left(self,x,y,grid):
		self.y-=2
	
	def check_collision(self,shflag,k,x,y,grid,fg):
		if shflag!=0:
			if fg==1: #w
				if (grid[x-1][y] == self.coinchar or grid[x-1][y+1] == self.coinchar or grid[x-1][y+2] == self.coinchar):
					self.coins+=1
				if (grid[x-1][y] == self.dbeam or grid[x-1][y+1] == self.dbeam or grid[x-1][y+2] == self.dbeam or grid[x-1][y] == self.vbeam or grid[x-1][y+1] == self.vbeam or grid[x-1][y+2] == self.vbeam or grid[x-1][y] == self.hbeam or grid[x-1][y+1] == self.hbeam or grid[x-1][y+2] == self.hbeam):
					self.life-=1
				if self.life==0:
					
					#lose(gid)
					for i in range(0,30):
						for j in range(1699,1799):
							grid[i][j]=" "
						print()

					with open("lose.txt") as fl_in:
						lnes = fl_in.readlines()
					for i in range(1,len(lnes)):
						for j in range(1711,1711+len(lnes[i-1])):
							if lnes[i-1][j-1711] == '\t' or lnes[i-1][j-1711]=='\n':
								grid[i][j]=' '
							else:
								grid[i][j]=lnes[i-1][j-1711]

					print('\033[0;0H')
					for i in range(0,30):
						for j in range(1699,1799):
							print(grid[i][j],end='')
						print()

					#print(Fore.RED +"\tGAME OVER"+RESET)
					exit()
			if fg==2:  #a
				
				if (grid[x][y-1] == self.coinchar or grid[x+1][y-1] == self.coinchar or grid[x+2][y-1] == self.coinchar):
					self.coins+=1
				if (grid[x][y-1] == self.dbeam or grid[x+1][y-1] == self.dbeam or grid[x+2][y-1] == self.dbeam  or grid[x][y-1] == self.vbeam or grid[x+1][y-1] == self.vbeam or grid[x+2][y-1] == self.vbeam or grid[x][y-1] == self.hbeam or grid[x+1][y-1] == self.hbeam or grid[x+2][y-1] == self.hbeam):
					self.life-=1
				if self.life==0:
					#lose(gid)
					for i in range(0,30):
						for j in range(1699,1799):
							grid[i][j]=" "
						print()

					with open("lose.txt") as fl_in:
						lnes = fl_in.readlines()
					for i in range(1,len(lnes)):
						for j in range(1711,1711+len(lnes[i-1])):
							if lnes[i-1][j-1711] == '\t' or lnes[i-1][j-1711]=='\n':
								grid[i][j]=' '
							else:
								grid[i][j]=lnes[i-1][j-1711]

					print('\033[0;0H')
					for i in range(0,30):
						for j in range(1699,1799):
							print(grid[i][j],end='')
						print()

					# print(Fore.RED +"\tGAME OVER"+RESET)
					exit()
			if fg==3:  #d
				
				if (grid[x][y+4] == self.coinchar or grid[x+1][y+4] == self.coinchar or grid[x+2][y+4] == self.coinchar):
					self.coins+=1
				if (grid[x][y+4] == self.dragbull or grid[x+1][y+4] == self.dragbull or grid[x+2][y+4] == self.dragbull or grid[x][y+4] == self.dbeam or grid[x+1][y+4] == self.dbeam or grid[x+2][y+4] == self.dbeam or grid[x][y+4] == self.vbeam or grid[x+1][y+4] == self.vbeam or grid[x+2][y+4] == self.vbeam or grid[x][y+4] == self.hbeam or grid[x+1][y+4] == self.hbeam or grid[x+2][y+4] == self.hbeam):				 
					self.life-=1
				if self.life==0:
					print(Fore.RED +"\tGAME OVER"+RESET)
					#lose(gid)
					for i in range(0,30):
						for j in range(1699,1799):
							grid[i][j]=" "
						print()

					with open("lose.txt") as fl_in:
						lnes = fl_in.readlines()
					for i in range(1,len(lnes)):
						for j in range(1711,1711+len(lnes[i-1])):
							if lnes[i-1][j-1711] == '\t' or lnes[i-1][j-1711]=='\n':
								grid[i][j]=' '
							else:
								grid[i][j]=lnes[i-1][j-1711]

					print('\033[0;0H')
					for i in range(0,30):
						for j in range(1699,1799):
							print(grid[i][j],end='')
						print()

					exit()
			if fg==4: #gravity
				if x+3 <= 28:
					if (grid[x+3][y] == self.coinchar or grid[x+3][y+1] == self.coinchar or grid[x+3][y+2] == self.coinchar):
						self.coins+=1
					if (grid[x+3][y] == self.dbeam or grid[x+3][y] == self.dbeam or grid[x+3][y+2] == self.dbeam or grid[x+3][y] == self.vbeam or grid[x+3][y] == self.vbeam or grid[x+3][y+2] == self.vbeam or grid[x+3][y] == self.hbeam or grid[x+3][y] == self.hbeam or grid[x+3][y+2] == self.hbeam):
						self.life-=1
					if self.life==0:
					#	lose()
						print(Fore.RED +"\tGAME OVER"+RESET)
						exit()