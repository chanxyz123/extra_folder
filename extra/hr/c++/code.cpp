#include <iostream>
using namespace std;
int main() {
    string y;
    while(getline(cin,y))
        {
        int i=0;
        while(i<y.length())
            {
            while(1)
                {
                if(y[i]=='/' && y[i+1]=='*')
                    {
                    cout << y[i];
                }
                cout <<"hello"<<endl;
                else if(y[i]=='*' && y[i+1]=='/')
                    {
                    cout <<y[i] <<y[i+1];
                    i+=1;
                    break;
                }
                else if(y[i]=='/' && y[i+1]=='/')
                    {
                    cout <<y[i];
                }
                else if(y[i]=='\n')
                    {
                    cout <<y[i];
                    i+=1;
                    break;
                }
                i+=1;
            }   
        }
    }
    return 0;
}