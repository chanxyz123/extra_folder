#include <iostream>

using namespace std;

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;
class binarysrch
{
public:
	node * insert(node * root, int value)
	{
		node * temp1  = root;
	    if(temp1==NULL)
	        {
	        	cout << "hello"<<endl;
	        node * curr = new node;
	        curr ->left = NULL;
	        curr ->right = NULL;
	        curr->data = value;
	        root =curr;
	    }
	    else
	        {
	        	cout << "hello1"<<endl;
	       node * temp = root;
	       node * ptr = temp;
	    while(temp!= NULL)
	        {
	        if(temp->data < value)
	            {
	            	cout << "hello2"<<endl;
	            temp =  temp->right;
	        }
	        else
	            {
	            	cout << "hello3"<<endl;
	            temp = temp->left;
	        }
	    }
	    node * curr = new node;
	    curr ->left = NULL;
	    curr ->right = NULL;
	    curr->data = value;
	    temp = curr;
	    root = ptr;
	    cout << "hello5"<<endl; 
	    }
	    return root;
	};
	void Inorder(node *root) {
	    if(root->left!=NULL)
	        {
	        Inorder(root->left);
	    }
	    cout << root->data << " ";
	    if(root->right!=NULL)
	        {
	        Inorder(root->right);
	    }

	};	
};
int main(int argc, char const *argv[])
{
	int x ,y;
	cin  >> x;
	node * temp = NULL;
	binarysrch* yo = new binarysrch();
	for(int i=0;i<x;i++)
	{
		cin >>y;
		temp = yo->insert(temp,y);
	}
	yo->Inorder(temp);
	return 0;
}