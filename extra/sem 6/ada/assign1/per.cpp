#include <iostream>
#include <string>
#include <sstream>
// #include <array>
using namespace std;

string permutation(int st,int arr[])
{
	if( (sizeof(arr)/sizeof(int))<=1)
	{
		stringstream ss;
		ss << arr[0];
		return ss.str();
	}
	else
	{
		for (int i = 0; i < (sizeof(arr)/sizeof(int))-1; ++i)
		{
			// cout <<i<<endl;
			swap(arr[st],arr[i]);
			stringstream s1,s2;
			s1 << arr[st];
			return s1.str() + permutation(arr[i+1],arr+i);
		}
	}
}

int main(int argc, char const *argv[])
{
	int n ;
	cin >> n;
	int arr[n];
	for (int i = 1; i <=n; ++i)
	{
		arr[i-1]=i;
		cout <<arr[i-1] <<endl;;
	}
	cout << arr+1 <<endl;
	cout << permutation(arr[0],arr) <<endl;
	return 0;
}