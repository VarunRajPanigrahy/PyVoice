from sys import stdin
#import nltk
import math
from collections import defaultdict

stdin=open('input.txt','r')
#nltk.download('words')
I=stdin.readline


def f(c):
	if(ord(c)>=ord('0') and ord(c)<=ord('9')):
		return ord(c)-ord('0')

	else: return ord(c)-ord('A')+10

def base(b,a):
	ans=0
	for i in range(len(b)-1,-1,-1):
		ans+=pow(a,len(b)-1-i)*f(b[i])
		if(f(b[i])>=a):return -1

	return ans

#print(base("1A1",2))



for _ in range(int(I())):
	n=int(I())
	arr=defaultdict(int)
	pakka=-1
	for i in range(n):
		a,b=map(str,I().split())
		if(a=="-1"):
			visited=defaultdict(int)
			for j in range(2,37):
				zk=base(b,j)
				if(zk==-1): continue
				if(visited[zk]==0):
					arr[zk]+=1
					visited[zk]=1

		else:
			zk=base(b,int(a))
			#print(zk)
			if(zk==-1):continue
			arr[zk]+=1
			if(pakka!=-1 and pakka!=zk):
				
				pakka=-10
				
			else:
				pakka=zk

	ans=-1
	keys=sorted(list(arr.keys()))
	#print(keys)
	for i in keys:
		if(arr[i]==n and i!=-1):
			ans=i
			break
	if(pakka!=-1 and ans!=pakka):
		ans=-1
	if(ans>10**12):
		ans=-1
	print(ans)
	
