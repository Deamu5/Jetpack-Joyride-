import numpy as np
import time
from random import randint
from colorama import *
RESET= '\x1b[0m'

class Board:
    
    def __init__(self,row,col):
        self.__rows = row
        self.__columns= col
        self.__grid= []
        self.__mag=[]
        self.__magx=[]
        self.__magy=[]

    @property
    def rows(self):
        return self.__rows
    @rows.setter
    def rows(self,cc):
        self.__rows=cc
    @property
    def columns(self):
        return self.__columns
    @columns.setter
    def columns(self,cc):
        self.__columns=cc
    @property
    def grid(self):
        return self.__grid
    @grid.setter
    def grid(self,cc):
        self.__grid=cc
    @property
    def mag(self):
        return self.__mag
    @mag.setter
    def mag(self,cc):
        self.__mag=cc
    @property
    def magx(self):
        return self.__magx
    @magx.setter
    def magx(self,cc):
        self.__magx=cc
    @property
    def magy(self):
        return self.__magy
    @magy.setter
    def magy(self,cc):
        self.__magy=cc
    
        

    def make_grid(self):
        self.grid = np.full((self.rows,self.columns)," ")
        
        for j in range(self.columns):
            self.grid[0][j]="="
            self.grid[29][j]="="        
    def print_grid(self,k,shflag,nitro): 
        if  k<=1699:
            for i in range(0,30):
                for j in range(0+k,100+k):
                    if i==0 or i==29:
                        print(Fore.BLUE + self.grid[i][j] + RESET,end='')
                    elif self.grid[i][j]=="$":
                        print(Fore.YELLOW + self.grid[i][j] + RESET,end='')
                    elif self.grid[i][j]=="#" or self.grid[i][j]=="@" or self.grid[i][j]=="%":
                        print(Fore.RED + self.grid[i][j] + RESET,end='')
                    elif self.grid[i][j]=="U":
                        print(Fore.CYAN + self.grid[i][j] + RESET,end='')
                    elif  shflag==1 and (self.grid[i][j]=="*" or self.grid[i][j]=="|" or self.grid[i][j]=="-") :
                        print(Fore.BLUE + self.grid[i][j] + RESET,end='')
                    
                    elif  shflag==0 and (self.grid[i][j]=="*" or self.grid[i][j]=="|" or self.grid[i][j]=="-") :
                        print(Fore.RED + self.grid[i][j] + RESET,end='')
                    elif self.grid[i][j]==">":
                        print(Fore.BLUE + self.grid[i][j] + RESET,end='')
                    elif self.grid[i][j]=="<":
                        print(Fore.RED + self.grid[i][j] + RESET,end='')
                    else :
                        print(self.grid[i][j] + RESET,end='')
                print() 
        if k>1699:
            for i in range(0,30):
                for j in range(1699,1799):
                    print(self.grid[i][j],end='')
                print()
    def magnet(self,plate,grid):
            x=randint(2,25)
            y=randint(plate,plate+100)
            if y<1790:
                grid[x][y]='U'
                grid[x+1][y]='U'
                grid[x][y+1]='U'
                grid[x+1][y+1]='U'
            self.mag.append('1')
            self.magx.append(x)
            self.magy.append(y)
    def magattraction(self,ix,iy,grid,k):
        for i in range(len(self.mag)):
            x=self.magx[i]
            y=self.magy[i]
            if iy >= y-20 and iy>k and iy<y:
                  grid[ix][iy-1]=" "
                  grid[ix+1][iy-1]=" "
                  grid[ix+2][iy-1]=" "
                  grid[ix][iy]=" "
                  grid[ix+1][iy]=" "
                  grid[ix+2][iy]=" "
                  iy+=1
                  iy+=1  
            elif iy <=y+20 and iy>k and iy>y:
                  iy-=1
        return iy               
    def coin_gen(self,plate,grid):
        x=randint(1,28)
        if x==25:
            x=22
        y=randint(plate,plate+90)
        size=7
        for i in range(1,size):
            grid[x][y]="$"
            y+=1
    def obstacles(self,plate,grid):
        x=randint(1,28)
        if x==25:
            x=22
        y=randint(plate+4,plate+90)
        size=7
        for i in range(1,size):
            grid[x][y]="#"
            y+=1
        for i in range(1,size):
            if grid[x][y]!="$" and x<=26 :
                grid[x][y]="%"
                x+=1
        x=randint(1,15)
        y=randint(plate,plate+90)
        for i in range(1,size-3):
            if grid[x][y]!="$" and x<=26:
                grid[x][y]="@"
                x+=1
                y+=1
                grid[x][y]=""
                x+=1
                y+=1







