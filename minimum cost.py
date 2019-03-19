def countcherry(l):
             	rc=3
                  	c=0
                      	for i in range(len(l)-1):
	               	if l[i]==l[i+1]:
	                		if l[i]=='R':
	                			c+=rc
	               		else:
	              			c+=gc
	              	else:
	              		continue
	                   return c
           def cherry():
          	n=int(input())
            	m=int(input())
	                  l=[]
                 	c=0
                    	for i in range(n):
                  			s=input()
	               		l.append(list(s))
	              for i in l:
	              	c+=countcherry(i)
                                try:
                     	cherry()
                                      except:
    	    print('invalid')
