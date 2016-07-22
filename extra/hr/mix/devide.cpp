#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
     int x,y;
    cin >> x;
    int p=0,z=0,n=0;
    for(int i=0;i<x;i++)
        {
        cin >> y;
        if(y>0){p++;}
        else if(y<0){n++;}
        else{z++;}
    }
    cout << p <<endl;
    cout << n <<endl;
    cout << z <<endl;
    return 0;
}