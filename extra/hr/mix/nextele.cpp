#include <iostream>
#include <cstdlib>
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  };

Node* Insert(Node *head,int value)
{
    if(head!=NULL)
    {
    Node * tail = head;
     while(tail->next!= NULL)
        {
          tail =tail->next;
      } 
      tail->next  = new Node;
    (tail->next)->data = value;
    (tail->next)->next = NULL;
    }
    else
    {
      Node * N = new Node;
      N->data = value;
      N->next = NULL;
      head = N;
    }
    
    return head;
  // Complete this method
}
int main(int argc, char const *argv[])
{
  int *a = new int[5];
  for (int i = 0; i < 5; ++i)
  {
    cin >> a[i];
  }

  return 0;
}
