#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N,x,m,z,v;
    cin >>N;
    m=-100000000;
    stack <int> s,maxstack;
    maxstack.push(m);
    for(int i=0;i<N;i++)
        {
        cin>>x;
        if(x==1)
            {
            cin>>v;
            s.push(v);
            if(maxstack.top()<v)
                {
                maxstack.push(v);
            }
        }
        else if (x==2)
            {
            if(maxstack.top()==s.top())
                {
                maxstack.pop();
            }
            s.pop();
        }
        else
            {
            cout <<maxstack.top() <<endl;
        }
    }
    return 0;
}
