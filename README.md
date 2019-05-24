# Binary-Search-Tree
A simple commandline program that demonstrates breadth and depth searches on a binary tree using Python

To Use:
Open the commandline, and run command
`python Binary_Search.py [--arguments]`

Commands:

'--list','-l' : input a series of numbers seperated by spaces, to build our tree from (if blank, defaults to 1k random numbers 1-10)
		
"--breadth","-b" : performs a breadthFirstSearch on the tree. REMEMBER to include an integer as an argument!
		
"--depth","-d" :  performs a depthFirstSearch on the tree (by default inorder). REMEMBER to include an integer as an argument!
"--inorder","-in" : for use with depthFirstSearch. Changes the type of dfs to inorder.
"--preorder","-pre" : for use with depthFirstSearch. Changes the type of dfs to preorder.
"--postorder","-post" : for use with depthFirstSearch. Changes the type of dfs to postorder.
		
"--single","-s" : only include the first matching result (works with both dfs and bfs).
"--traverse","-t" : show the path through the tree up until the first matching result (works with both dfs and bfs).
