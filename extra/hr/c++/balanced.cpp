#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string check(string s)
    {
     stack <char> st;
        for(int j=0;j<s.length();j++)
            {
            if(s[j]=='(' || s[j]=='{' || s[j]=='[')
                {
                st.push(s[j]);
            }
            else if(s[j]==')' || s[j]=='}' || s[j]==']')
                {
                if(st.size()==0)
                    {
                    return "NO";
                }
                if(s[j]==')' && st.top()!='(')
                    return "NO";
                else if(s[j]==')' && st.top()=='(')
                    st.pop();
                else if(s[j]==']' && st.top()!='[')
                    return "NO";
                else if(s[j]==']' && st.top()=='[')
                    st.pop();
                else if(s[j]=='}' && st.top()!='{')
                    return "NO";
                else if(s[j]=='}' && st.top()=='{')
                    st.pop();
            }
        }
    return "YES";
}

int main() {
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
        {
        string s;
        cin >>s;
        cout << check(s) <<endl;
    }
    return 0;
}
