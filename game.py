
from board import Board
from mandalorian import Mando
import time
from time import sleep
from  input import *
import os 
from objects import *
os.system('clear')
username=input("Enter your name ")
os.system('clear')
ix=26
iy=0
board=Board(35,1801)
board.make_grid()
mando= Mando(ix,iy,username)
mando.initial_pos(board.grid)
k=0  # column no
fg=0
plate=0
flag=0
shflag=1 #shield flag
t0=0
tc=0
shf=1
nitroflag=0
dragbslow=0
fw=0
while plate<=1699:
	for i in range(3):
		board.coin_gen(plate,board.grid)
		board.obstacles(plate,board.grid)
	plate+=100
sh='ready'
plate=0
while plate<=1699:
		board.magnet(plate,board.grid)
		plate+=700
art=Art(board.grid)	
while True:
	print('\033[0;0H') 
	print("username : ",username,"\tcoins : ",mando.coins,"\tlives : ",mando.life,"\tscore :",2*mando.coins+k,"\tshield : ",sh,"\tbosslife: ",mando.bosslife,"\n")
	board.print_grid(k,shflag,nitroflag)
	char = get_input(0.05)
	if flag==0:
		if ix<=25 and char!='w':
			mando.clear_mando(ix,iy,board.grid)
			ix=mando.gravity(ix,fw)
			mando.check_collision(shflag,k,ix,iy,board.grid,4)
		if fg!=1 :
			
			mando.check_collision(shflag,k,ix,iy,board.grid,3)
			mando.clear_mando(ix,iy,board.grid)
			if k!=iy and char!='w':
				mando.clear_mando(ix,iy,board.grid)
				mando.clear_mando(ix,iy+1,board.grid)
				mando.move_left(ix,iy,board.grid)
				iy-=1
			mando.clear_mando(ix,iy,board.grid)
			mando.auto_move(ix,iy,board.grid)
			mando.move(k,ix,iy,board.grid)
			iy+=1
			k+=1
		iy=board.magattraction(ix,iy,board.grid,k)	
		if char == 'w':
				ix=mando.gravity(ix,1)
				if ix==1:
					continue
				mando.check_collision(shflag,k,ix,iy,board.grid,1)
				mando.clear_mando(ix,iy,board.grid)
				mando.move_up(ix,iy,board.grid)
				ix-=1
				mando.move(k,ix,iy,board.grid)
		if char == 'a':
			if iy>k:
				mando.check_collision(shflag,k,ix,iy,board.grid,2)
				mando.clear_mando(ix,iy,board.grid)
				mando.move_left(ix,iy,board.grid)
				iy-=1
				mando.move(k,ix,iy,board.grid)
		if char == 'd':
			if iy!=1793 and iy <k+97 :
				mando.check_collision(shflag,k,ix,iy,board.grid,3)
				mando.clear_mando(ix,iy,board.grid)
				mando.move_right(ix,iy,board.grid)
				iy+=2
				if k>=1697:
					iy-=1
				mando.move(k,ix,iy,board.grid)
		if char == 'b':
				mando.bull(k,ix,iy,board.grid)
		if char == 'n':
			mando.clear_mando(ix,iy,board.grid)
			mando.auto_move(ix,iy,board.grid)
			mando.move(k,ix,iy,board.grid)
			iy+=1
			#iy+=1
			k+=1
			nitroflag=1
		nitroflag=0
		if char== 'q':
			exit()
		if char == ' ' and shflag==1 and shf==1:
			sh='activated'
			shflag=0
			shf=0
			t0=time.time()
		tc=time.time()
		if int(tc)-int(t0) >=10 and shf!=1:
			shflag=1
			sh='deactivated'
		if int(tc)-int(t0) >=70 and shf!=1:
			shf=1
			sh='ready       '
		mando.travel(board.grid)
		mando.travel(board.grid)
		sleep(0.05) 
	if k>=1697 and fg!=1:
		flag=1
		fg=1
	if flag==1:
		mando.y=iy
		art.cleardrag(board.grid)
		art.print(ix,board.grid)
		dragbslow+=1
		if dragbslow>=10:
			art.fire(ix,board.grid)
			dragbslow=0
		art.trav(board.grid)
		mando.check_collision(shflag,k,ix,iy,board.grid,3)	
		mando.checkb(board.grid)
		if ix<=25 and char!='w':
			mando.clear_mando(ix,iy,board.grid)
			ix=mando.gravity(ix,fw)
			mando.check_collision(shflag,k,ix,iy,board.grid,4)
			mando.move(k,ix,iy,board.grid)
		
		if char == 'w':
				if ix==1:
					continue
				mando.check_collision(shflag,k,ix,iy,board.grid,1)
				mando.clear_mando(ix,iy,board.grid)
				mando.move_up(ix,iy,board.grid)
				ix-=1
				mando.move(k,ix,iy,board.grid)
		if char == 'a':
			if iy>k:
				mando.check_collision(shflag,k,ix,iy,board.grid,2)
				mando.clear_mando(ix,iy,board.grid)
				mando.move_left(ix,iy,board.grid)
				iy-=1
				mando.move(k,ix,iy,board.grid)
		if char == 'd':
			if iy<=1746:
				mando.check_collision(shflag,k,ix,iy,board.grid,3)
				mando.clear_mando(ix,iy,board.grid)
				mando.move_right(ix,iy,board.grid)
				iy+=1
				mando.move(k,ix,iy,board.grid)
		if char == 'b':
				mando.bull(k,ix,iy,board.grid)
		if char == ' ' and shflag==1 and shf==1:
			sh='activated'
			shflag=0
			shf=0
			t0=time.time()
		tc=time.time()
		if int(tc)-int(t0) >=10 and shf!=1:
			shflag=1
			sh='deactivated'
		if int(tc)-int(t0) >=70 and shf!=1:
			shf=1
			sh='ready       '
		mando.travel(board.grid)
		mando.travel(board.grid)
		sleep(0.05) 
	