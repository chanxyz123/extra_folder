#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main(int argc, char const *argv[])
{
	int V,edge;
	int source;
	cin >>	V >> edge;
	int arr[edge][3];
	int f,s,w;
	int m = 10000;
	for (int i = 0; i < edge; ++i)
	{
		cin >>f>>s>>w;
		arr[i][0] = f;
		arr[i][1] = s;
		arr[i][2] = w;
	}
	cin >> s ;
	// cout << "" <<endl;
	int temp[3];
	for (int j = 0; j < edge-1; ++j)
	{
		int i=j;
		while(i>=0)
		{
			if (arr[i][2]>arr[i+1][2])
			{
				for (int k = 0; k <3; ++k)
				{
					temp[k] = arr[i][k];	
				}
				for (int k = 0; k <3; ++k)
				{
					arr[i][k] = arr[i+1][k];	
				}
				for (int k = 0; k <3; ++k)
				{
					arr[i+1][k] = temp[k];	
				}
				i=i-1;
			}
			else
			{
				i=-1;
			}
		}
	}
	for (int l = 0; l < edge; ++l)
		{
			for (int j = 0; j <3; ++j)
			{
				cout << arr[l][j] << " ";
			}
			cout << "" <<endl;
		}
		cout << "" <<endl;
	int set[V+1];
	for (int k = 1; k <= V; ++k)
	{
		set[k] = 0;
	}
	int total=0;
	for (int k = 0; k < edge; ++k)
	{
		// cout <<"hello"<<endl;
		// cout << arr[k][0] <<endl;
		// cout << set[arr[k][0]] <<endl;
		// cout << set[arr[k][1]] <<endl;
		// cout << arr[k][1] <<endl;
		if (set[arr[k][0]] !=1 && set[arr[k][1]]!=1 || set[arr[k][0]] ==1 && set[arr[k][1]]!=1 ||set[arr[k][0]] !=1 && set[arr[k][1]]==1)
		{
			set[arr[k][0]] = 1;
			set[arr[k][1]] = 1;
			cout << arr[k][2] <<endl;
			total+=arr[k][2];
		}
		// cout << "hellooo" <<endl;
	}
	cout <<total <<endl;
}