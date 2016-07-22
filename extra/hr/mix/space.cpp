#include <iostream>
using namespace std;

void space(int num)
    {
    for(int i=0;i<num;i++)
        {
        cout << " ";
    }
}
void hase(int number)
    {
    for(int i=0;i<number;i++)
        {
        cout << "#";
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
     int x,y;
    cin >> x;
    for(int i=0;i<x;i++)
        {
        space(x-(i+1));
       /* cout << hase(i);*/
    }
    return 0;
}
