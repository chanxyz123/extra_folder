#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int x;
    cin >> x;
    int sum=0,y;
    int  * arr = new int[x];
    for(int i=0;i<x;i++)
        {
        cin >> y;
        sum = sum + y;
    }
    cout << sum <<endl;
    return 0;
}