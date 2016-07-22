#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
struct node 
{
	int data;
	node * next;
};

class bfs
{
private:
	node * head;
	node * tail;
	int vertex;
public:
	bfs(int v)
	{
		vertex = v;
		head = new node[v+1];
		tail = new node[v+1];
		for (int i = 1; i <= v; ++i)
		{
			(head+i)->next = NULL;
			(tail+i)->next = (head+i);
		}
	};
	void adjacency_list(int f,int s)
	{
		node * temp = new node;
		temp->data = s;
		temp->next = NULL;
		if((tail+f)->next->next!=NULL)
		{
			(tail+f)->next = (tail+f)->next->next;
		}
		(tail+f)->next->next = temp;
		node * curr = new node;
		curr ->data = f;
		curr->next = NULL;
		if((tail+s)->next->next!=NULL)
		{
			(tail+s)->next = (tail+s)->next->next;
		}
		(tail+s)->next->next = curr;
	};
	void print()
	{
		for (int i = 1; i <= vertex; ++i)
		{
			node * ptr = (head+i)->next;
			cout << i ;
			while(ptr)
			{
				cout << "-->";
				 cout <<ptr->data ;
				 ptr = ptr->next;
			}
			cout <<""<<endl;
		}
	};
	void bfssort(int s)
	{
		int arr[vertex];
		int out[vertex];
		for (int i = 1; i <= vertex; ++i)
		{
			arr[i] = -1;
			out[i] = 0;
		}
		queue<int> q;
		q.push(s);
		int x =0;
		while(q.size()!=0)
		{	
			int v =q.front(); 
			q.pop();
			arr[v] = 1;
			node * temp = (head+v)->next;
			while(temp!=NULL)
			{
				if (arr[temp->data]==-1)
				{
					q.push(temp->data);
					out[temp->data]=out[v]+1;
					arr[temp->data]=0;
					temp = temp->next;	
				}
				else
					temp = temp->next;
			}
		}
		for (int i = 1; i <= vertex; ++i)
		{
			if (i!=s && out[i]!=0)
			{
				cout <<out[i]*6 << " " ;	
			}
			else if( i!=s && out[i]==0)
			{
				cout << "-1"<< " ";
			}
		}
	};
};
int main(int argc, char const *argv[])
{
	int test_case;
	cin >> test_case;
	int vertex,edge;
	int source;
	for (int i = 0; i < test_case; ++i)
	{
		cin >>	vertex >> edge;
		bfs *g = new bfs(vertex);
		int f,s;
		for (int i = 0; i < edge; ++i)
		{
			cin >>f>>s;
			g->adjacency_list(f,s);
		}
		cin >> source;
		g->bfssort(source);
		// g->print();
	}
	return 0;
}