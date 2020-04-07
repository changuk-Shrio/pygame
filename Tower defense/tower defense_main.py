import pygame
import time
import random
from Screen import *
from Setting import *
from Enemy import *

def check_index(mouse_pos,list,screen):#l은리스트 마우스포느는 마우스좌표
    i=mouse_pos[0]//50-2
    j=mouse_pos[1]//50-2

    if list[j][i]==0:
        x=100+(i*50)
        y=100+(j*50)
        pygame.draw.rect(screen,RED,[x,y,50,50])

def dest(i,j,dir,l):
    ans=0
    if l[i][j]==2:
        return False

    if j-1>=0 and dir!=2:
        left = [l[i][j - 1], i, j-1,4]
        if left[0]:
            ans=left
    if j+1<=len(l[0]) and dir!=4:
        right = [l[i][j + 1],i,j+1,2]
        if right[0]:
            ans=right
    if i+1<len(l) and dir!=1:
        down = [l[i + 1][j],i+1,j,3]
        if down[0]:
            ans=down
    if i-1>=0 and dir!=3:
        up = [l[i - 1][j],i-1,j,1]
        if up[0]:
            ans=up
    return ans,i,j


pygame.init() #파이 게임 초기화
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

#변수

large_font = pygame.font.SysFont('malgungothic', 60)
small_font = pygame.font.SysFont('malgungothic', 20)


list=[[1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],#1이길 0은 설치되는곳 2는 끝부분
      [0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0],
      [0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0],
      [0,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0],
      [0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0],
      [0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0],
      [0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
      [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]]
#1,2 200,150

list_pos=[]
for i in range(0,len(list)):
    list_pos.append([])
    for j in range(0,len(list[0])):
        list_pos[i].append([100+50*j,100+50*i])
#for i in list_pos:
    #print (i)
game_screen=Screen(1200,800,"images/background.png")
enemy=Enemy(5)

poz=[]
#poz_x=0
#poz_y=0
cnt=0
ans,a,b=dest(0,0,0,list)
poz.append([a,b])
#print(ans)
while True:
    ans,a,b = dest(ans[1], ans[2], ans[3], list)
    poz.append([a,b])#좌표
    Enemy.move_Enemy(enemy,ans[1],ans[2])
    #print (ans[1]*50,ans[2]*50)
    #print (ans[1],ans[2])
    if dest(ans[1], ans[2], ans[3], list) == False:
        break
#print(poz)
while True:
    Screen.draw(game_screen,game_screen.screen)
    event = pygame.event.get()
    for e in event:
        if e.type==pygame.QUIT:
            pygame.quit()
    mouse=pygame.mouse.get_pos()
    if mouse[0]<100 or mouse[0]>=1100 or mouse[1]<100 or mouse[1]>=700:#작은게임판 나갓을때
        pass
    else:
        check_index(mouse,list,game_screen.screen)

    Enemy.draw_Enemy(enemy,game_screen.screen)
    #print (list_pos[cnt][0][0],list_pos[cnt][0][0])
    for i in range(0,len(list_pos)):#줄
        for j in range(0,len(list_pos[0])):#칸
            Enemy.move_Enemy(enemy,list_pos[cnt][cnt][0],list_pos[cnt][cnt][1])
            cnt+=1

    pygame.display.flip()

#test
#test2
