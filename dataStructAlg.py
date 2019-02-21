import argparse
import random
import time
from collections import deque 

#Nodes for our tree
#this contains some extra functions and properties that were used for debugging, and I decided to leave them
class Node:
	def __init__(self,value):
		global _Incrementer
		self.value=value
		self.left=None
		self.right=None

		#a unique id for our node, for nodes with identical values
		self.id= random.randrange(100, 999)

		#the order in which the node was created. For example in array [1,2,3], for array[0] would be getOrder()=0
		self.order=_Incrementer
		_Incrementer+=1

	def getValue(self):
		return self.value

	def getOrder(self):
		return self.order

	def getChildren(self):
		if self.left==None and self.right==None:
			return None
		children=[]

		if self.left!=None:
			children.append(self.left)
		else:
			children.append(None)

		if self.right!=None:
			children.append(self.right)
		else:
			children.append(None)

		return children

	def getChildrenVal(self):
		if self.left==None and self.right==None:
			return None

		children=[]
		if self.left!=None:
			children.append(self.left.getValue())
		else:
			children.append(None)

		if self.right!=None:
			children.append(self.right.getValue())
		else:
			children.append(None)

		return children

#inserts a new node into our tree
def insert(root,node): 
    if root is None: 
    	root = node 
    else: 
        if root.value < node.value: 
            if root.right is None: 
            	root.right = node 
            else: 
            	insert(root.right, node) 
        else: 
            if root.left is None: 
            	root.left = node 
            else: 
            	insert(root.left, node) 

#builds our tree
def buildTree(array):
	print("building tree....")
	root=Node(array[0])
	del(array[0])
	for a in array:
		insert(root,Node(a))
	print("building complete")
	return root

def breadthFirstSearch(root,target,single,t,flag=0):
	
	results=[]

	if not root or root==None:
		return results,flag

	children= deque([])

	#first check the target against the root
	current=root

	#if we are traversing the list, then add the value of each Node in the tree to results, until we hit the target
	if t:
		results.append(current.getValue())
	if root.getChildren()!=None:
		children.extend(root.getChildren())

	if root.getValue()==target:
	#this flag is set to true(1) if our target was found, and returns false(0) otherwise
		flag=1

	#if we are not traversing and the root matches the target, then add the value to results
		if not t:
			results.append(root.getValue())

	#if single=true, we will only return the first result we find and then return. This is automatically set to true if we are traversing
		if single:
			return results,flag

	#take the first child added to the queue, and add it's children to the queue. Then check it's value for the target. When there are no children left in the queue, exit the while loop
	while len(children):
		for child in list(children):
			current=children.popleft()
			if t and current!=None:
				results.append(current.getValue())

			if current!=None and current.getChildren()!=None:
				children.extend(current.getChildren())

			if current!=None and current.getValue()==target:
				flag=1
				if not t:
					results.append(current.getValue())
				if single:
					return results,flag

	return results,flag

#we can execute three types of dps:
#subType=0 - preorder
#subType=1 - inorder (default)
#subType=2 - postorder

#single - only return first result of search (otherwise we will return ALL matches)
#t - traverse the tree, showing our path, until we find a match (changes single=True automatically)
#flag - set to True(1) if the target was found
def depthFirstSearch(current,target,results,single,t,subType,flag = 0):
	if current!=None:

		#get the value of the current node. Record it if we are traversing. Otherwise add it to results if it matches the target.
		if subType==0:
			if t:
				results.append(current.getValue())
			if current.getValue()==target:
				if not single or len(results)==0:
					results.append(current.getValue())

				#if single=true, set our flag to True once we find a match
				if single:
					return results, 1

		#recurse using the left child. If we already found a result, return
		results, flag =depthFirstSearch(current.left,target,results,single,t,subType)
		if flag == 1:
			return results, flag
		
		if subType==1:
			if t:
				results.append(current.getValue())
			if current.getValue()==target:
				if not single or len(results)==0:
					results.append(current.getValue())
				if single:
					return results, 1
		
		#recurse using the right child. If we already found a result, return
		results, flag =depthFirstSearch(current.right,target,results,single,t,subType)
		if flag == 1:
			return results, flag
		
		if subType==2:
			if t:
				results.append(current.getValue())
			if current.getValue()==target:
				if not single or len(results)==0:
					results.append(current.getValue())
				if single:
					return results, 1
			
	return results, flag

#if no arguments are entered, it will run a helloWorld 
def helloWorld():
	print ("Running dataStruct!")
	exit()

#displays welcome/help message
def displayHelp():
	text="""\
------------------------
Binary Tree Search
------------------------
Commands:

'--list','-l' : input a series of numbers seperated by spaces, to build our tree from (if blank, defaults to 1k random numbers 1-10)
		
"--breadth","-b" : performs a breadthFirstSearch on the tree
		
"--depth","-d" :  performs a depthFirstSearch on the tree (by default inorder)
"--inorder","-in" : for use with depthFirstSearch. Changes the type of dfs to inorder
"--preorder","-pre" : for use with depthFirstSearch. Changes the type of dfs to preorder
"--postorder","-post" : for use with depthFirstSearch. Changes the type of dfs to postorder
		
"--single","-s" : only include the first matching result (works with both dfs and bfs)
"--traverse","-t" : show the path through the tree up until the first matching result (works with both dfs and bfs)
	"""
	print(text)
	exit()

if __name__ == '__main__':
	#set global variables
	_Incrementer=0
	array=[]

	#get arguments
	parser=argparse.ArgumentParser()
	parser.add_argument('--list','-l', nargs='+',type=int, help='Array to be sorted (defaults to 1k random numbers 1-10)')
	parser.add_argument("--breadth","-b",help="performs a breadthFirstSearch on the tree")
	parser.add_argument("--depth","-d", help="performs a depthFirstSearch on the tree")
	parser.add_argument("--inorder","-in",help="performs a depthFirstSearch (inorder) on the tree",action="store_true")
	parser.add_argument("--preorder","-pre",help="performs a depthFirstSearch (preorder) on the tree",action="store_true")
	parser.add_argument("--postorder","-post",help="performs a depthFirstSearch (postorder) on the tree",action="store_true")	
	parser.add_argument("--single","-s",help="only include first result",action="store_true")
	parser.add_argument("--traverse","-t",help="show path to result",action="store_true")
	args = parser.parse_args()

	#depth first and breadth first searches
	if args.breadth or args.depth:
		#create our array
		if not args.list:
			for x in range(1000):
				x=random.randrange(1,11)
				array.append(x)
		else:
			for i in args.list:
				try:
					array.append(int(i))
				except:
					print("couldn't add:"+str(i))

		print("array: "+str(array))
		
		if len(array)<1:
			print("empty array!")
			exit()

		root=buildTree(array)

		#set arguments for depth and breadth searches
		single=False
		if args.single:
			single=True

		t=False
		if args.traverse:
			single=True
			t=True

		#execute breadth first search
		if args.breadth:
			#check if the value enter is an integer
			try:
				args.breadth=int(args.breadth)
			except:
				print("error: value being searched for is not an integer")
				exit()

			print("init depthFirstSearch...")
			start=time.time()
			results,found=breadthFirstSearch(root,int(args.breadth),single,t)
			print('Completed search in {0:0.1f} seconds'.format(time.time() - start))

			if not results:
				print("breadth search returned no results")
				exit()	
			else:
				if t:
					print("path through tree:"+str(results))
					if found==0:
						print("search returned no results")
				else:
					print("breadth found "+str(len(results))+" results"+str(results))
				exit()

		#execute depth first search
		if args.depth:
			#check if the value enter is an integer
			try:
				args.depth=int(args.depth)
			except:
				print("error: value being searched for is not an integer")
				exit()

			subType = 1
			if args.preorder:
				subType = 0
			if args.postorder:
				subType = 2

			print("init depthFirstSearch...")
			start=time.time()
			results=[]
			nodes=[]
			results, found=depthFirstSearch(root,int(args.depth),results,single,t,subType)
			print('Completed search in {0:0.1f} seconds'.format(time.time() - start))

			if not results:
				print("depth search returned no results")
				exit()
			else:
				if t:
					print("path through tree:"+str(results))
					if found==0:
						print("search returned no results")
				else:
					print("depth found "+str(len(results))+" results"+str(results))
				exit()

#if no arguments are entered, display help message that explains how to use
	elif args.breadth==None and args.depth==None:
		displayHelp()