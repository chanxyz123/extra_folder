#include <iostream>
#include <algorithm>
#define INT_MAX 1000000

using namespace std;
int minKey(int key[], bool mstSet[],int V)
{
   int min = INT_MAX, min_index;
 
   for (int v = 0; v < V; v++)
     if (mstSet[v] == false && key[v] < min)
         min = key[v], min_index = v;
 
   return min_index;
}
int main(int argc, char const *argv[])
{
	int V,edge;
	int source;
	cin >>	V >> edge;
		int arr[V][V];
	for (int i = 0; i < V; ++i)
		{
			for (int j = 0; j < V; ++j)
			{
				arr[i][j]=0;
			}
		}
	int f,s,w;
	for (int i = 0; i < edge; ++i)
	{
		cin >>f>>s>>w;
		arr[f-1][s-1] = w;
		arr[s-1][f-1] = w;
	}
	cin >> s;
	int parent[V]; 
    int key[V]; 
    bool mstSet[V]; 
    for (int i = 0; i < V; i++)
    	key[i] = INT_MAX, mstSet[i] = false;

    key[s-1] = 0; 
    parent[s-1] = -1; 
    for (int count = 0; count < V; count++)
    {
        int u = minKey(key, mstSet,V);
        mstSet[u] = true;
        for (int v = 0; v < V; v++)
          if (arr[u][v] && mstSet[v] == false && arr[u][v] <  key[v])
          {
             parent[v]  = u, key[v] = arr[u][v];
          }
    }
    int total =0;
    for (int i = 0; i < V; ++i)
    {
    	if (i!=s-1)
    	{
    		total+=arr[i][parent[i]];
    	}
    }
    cout << total <<endl;
	return 0;
}