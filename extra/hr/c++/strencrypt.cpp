#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    string s;
    cin>>n;
    cin>>s;
    int k;
    cin>>k;

    k%=26;
    for(int i=0;i<n;i++)
    {
        int c=s[i];
        // cout << "c =" <<c<<endl;
        if(c>=97 && c<=122) // Lowercase characters
        {
            c+=k;
            if(c>122) // C exceeds the ascii range of lowercase characters.
            {
               c=96+(c-122); //wrapping from z to a
            }
        }
        else if(c>=65 && c<=90 )//Uppercase characters
        {
            c+=k;
            if(c>90) // C exceeds the ascii range of uppercase characters.
            {
                c=64+(c-90); //wrapping from Z to A
            }
        }
        cout<<(char)c;
    }
    cout<<endl;
    return 0;
}