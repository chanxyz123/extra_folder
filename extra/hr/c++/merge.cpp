#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
	int f[] = {5,10,15,20,25};
	int s[] = {50,40,30,20,10};
	int v[10];

	sort(f,f+5);
	sort(s,s+5);
	merge(f,f+5,s,s+5,v);
	reverse(v,v+10);
	for (int i = 0; i < 10; ++i)
	{
		cout <<v[i]<< " " ;
	}
	cout <<""<<endl;
	remove(v,v+10,30);
	for (int i = 0; i < 10; ++i)
	{
		cout <<v[i]<< " " ;
	}
	cout <<""<<endl;
	replace(v,v+10,30,5);
	for (int i = 0; i < 10; ++i)
	{
		cout <<v[i]<< " " ;
	}
	cout <<""<<endl;
	sort(f,f+5);
	sort(s,s+5);
	merge(f,f+5,s,s+5,v);
	if (binary_search(f,f+5,20))
		cout <<"found"<<endl;
	else
		cout <<"not found"<<endl;

	for (int i = 0; i < 10; ++i)
	{
		cout <<v[i]<< " " ;
	}
	return 0;
}
