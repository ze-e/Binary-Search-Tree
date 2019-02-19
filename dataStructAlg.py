import argparse
import random
import time
from collections import deque 

class Node:
	def __init__(self,value):
		global _Incrementer
		self.value=value
		self.left=None
		self.right=None
		self.id= random.randrange(100, 999)
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

def inorder(root): 
    if root: 
        inorder(root.left) 

        children=root.getChildrenVal()
        if children != None:
        	left=children[0]
        	right=children[1]
        else:
        	left=None
        	right=None

       # print("left: "+str(left)+"value: "+str(root.value)+"right: "+str(right))
        inorder(root.right) 

def buildTree(array):
	print("building tree....")
	root=Node(array[0])
	del(array[0])
	for a in array:
		insert(root,Node(a))
	print("building complete")
	inorder(root)
	return root

def breadthFirstSearch(root,target,single,t):
	start=time.time()
	results=[]
	if not root or root==None:
		return results
	print("init breadthFirstSearch...")
	children= deque([])
	current=root
	if t:
		results.append(current.getValue())

	if root.getChildren()!=None:
		children.extend(root.getChildren())
	'''
		print(str(root)+" "+str(root.getValue()))
		if root.getChildren()[0]!=None:
			print("child1: "+" "+str(root.getChildren()[0])+str(root.getChildren()[0].getValue()))
		else:
			print("child1: None")
		if root.getChildren()[1]!=None:
			print("child2: "+" "+str(root.getChildren()[1])+str(root.getChildren()[1].getValue()))
		else:
			print("child2: None")
'''
	if root.getValue()==target:
		if not t:
			results.append(root.getValue())
		if single:
			return results

	while len(children):
		for child in list(children):
			current=children.popleft()
			if t and current!=None:
				results.append(current.getValue())

			if current!=None and current.getChildren()!=None:
				children.extend(current.getChildren())

			if current!=None and current.getValue()==target:
				if not t:
					results.append(current.getValue())
				if single:
					return results
				'''
				print(str(current)+" "+str(current.getValue()))
				if current.getChildren()[0]!=None:
					print("child1: "+" "+str(current.getChildren()[0])+str(current.getChildren()[0].getValue()))
				else:
					print("child1: None")
				if current.getChildren()[1]!=None:
					print("child2: "+" "+str(current.getChildren()[1])+str(current.getChildren()[1].getValue()))
				else:
					print("child2: None")
				print("children: "+str(children))
				'''
	print('Completed search in {0:0.1f} seconds'.format(time.time() - start))
	return results

#type
def depthFirstSearch(root,target,results,single,t,subSearch):
	if root!=None:

		if subSearch==0:
			if t:
				results.append(root.getValue())
			if not t and root.getValue()==target:
				results.append(root.getValue())
			if single and root.getValue()==target:
				return results

		depthFirstSearch(root.left,target,results,single,t,subSearch)
		
		if subSearch==1:
			if t:
				results.append(root.getValue())
			if not t and root.getValue()==target:
				results.append(root.getValue())
			if single and root.getValue()==target:
				return results


		depthFirstSearch(root.right,target,results,single,t,subSearch)
		
		if subSearch==2:
			if t:
				results.append(root.getValue())
			if not t and root.getValue()==target:
				results.append(root.getValue())
			if single and root.getValue()==target:
				return results
	
	return results

def helloWorld():
	print ("Running dataStruct!")
	SystemExit

if __name__ == '__main__':
	#set global variables
	_Incrementer=0
	array=[]

	#get arguments
	parser=argparse.ArgumentParser()
	parser.add_argument("--sort",help="Array to be sorted (defaults to 1k random numbers 1-10)")
	parser.add_argument("--breadth","-b",help="performs a breadthFirstSearch on the tree")
	parser.add_argument("--depth","-d",help="performs a depthFirstSearch on the tree (defaults to inorder)")
	parser.add_argument("--inorder","-in",help="performs a depthFirstSearch (inorder) on the tree",action="store_true")
	parser.add_argument("--preorder","-pre",help="performs a depthFirstSearch (preorder) on the tree",action="store_true")
	parser.add_argument("--postorder","-post",help="performs a depthFirstSearch (postorder) on the tree",action="store_true")	
	parser.add_argument("--single","-s",help="only include first result",action="store_true")
	parser.add_argument("--traverse","-t",help="show path to result",action="store_true")
	args = parser.parse_args()

	#depth first and breadth first searches
	if args.breadth or args.depth:
		#create our array

		#for x in range(1000):
		#	x=random.randrange(1,11)
		#	array.append(x)
		array=[3,2,4,1,4,6,8,5]
		root=buildTree(array)

		#set arguments for depth and breadth searches
		if args.single:
			single=True
		else:
			single=False

		if args.traverse:
			single=True
			t=True
		else:
			single=False
			t=False

		#execute breadth first search
		if args.breadth:
			results=breadthFirstSearch(root,int(args.breadth),single,t)

			if not results:
				print("breadth search returned no results")
				SystemExit	
			else:
				print("breadth found results"+str(results))
				SystemExit

		#execute depth first search
		if args.depth:
			subSearch = 1
			if args.preorder:
				subSearch = 0
			if args.postorder:
				subSearch = 2

			print("init depthFirstSearch...")
			start=time.time()
			results=[]
			results=depthFirstSearch(root,int(args.depth),results,single,t,subSearch)
			print('Completed search in {0:0.1f} seconds'.format(time.time() - start))
			if not results:
				print("depth search returned no results")
				SystemExit
			else:
				print("depth found results"+str(results))
				SystemExit



	elif args.breadth==None and args.depth==None:
		helloWorld()