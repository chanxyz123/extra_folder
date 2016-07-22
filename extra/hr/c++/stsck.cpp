// stack::push/pop
#include <iostream>       // std::cout
#include <stack>          // std::stack
using namespace std;

int main ()
{
  stack<int> mystack;

  for (int i=0; i<5; ++i) mystack.push(i);

  cout << "Popping out elements...";
  while (!mystack.empty())
  {
    cout << ' ' << mystack.top();
     mystack.pop();
  }
  // mystack.pop();
  // cout << ' ' << mystack.top();
  cout << '\n';

  return 0;
}