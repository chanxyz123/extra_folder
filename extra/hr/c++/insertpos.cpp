#include <iostream>
 
using namespace  std;

struct Node{
    int data;
    Node * next;
};

void insertnth(Node * head,int data,int pos)
{
    Node * ptr = head;
    int i=0;
    while(i<pos)
    {
        i++;
        ptr= ptr->next;
    }
    Node * temp = new Node;
    temp->data = data;
    temp->next = ptr->next;
    ptr->next = temp;
    head = ptr;
}
void Print(Node *head)
{
    Node * temp = head;
     while(1)
        {
        if(temp->next!=NULL)
        {
        cout << (temp->next)->data<< endl ;
        temp = temp->next;
    }
        else
            break;
    }
}
void Printrev(Node *head)
{
    Node * temp = head;
     while(1)
        {
        if(temp!=NULL)
        {
        cout << temp->data<< endl ;
        temp = temp->next;
    }
        else
            break;
    }
}
Node* Reverse(Node *head)
{
    if(head->next ==NULL)
    {
        return head;
    }
    if(head->next->next==NULL)
        {
        return head;
    }
    else if(((head->next)->next)->next==NULL)
        {
        Node * ptr = head->next;
        Node * temp = ptr->next;
        temp->next =  ptr;
        ptr->next =NULL;
        head = temp;
        return head;
    }
    else
        {
    Node * ptr  = head;
    ptr = ptr->next;
    Node * temp = ptr ->next;
    Node * curr = temp->next;
    ptr->next =NULL;
    while(curr!=NULL)
        {
        temp->next = ptr;
        ptr = temp;
        temp = curr;
        curr= temp->next;
    }
    temp->next = ptr;
    Node * head1 = new Node ;
    head1->data = 0;
    head1->next = temp;
    head =  head1;
    return head;
    }
}
int GetNode(Node *head,int positionFromTail)
{
    int len=0;
   while(head!=NULL)
        {
        head = head->next;
      len++;
    }
    cout << len <<endl;
    int i = 0;
    cout << len-positionFromTail-1 <<endl;
    while(i<(len-positionFromTail-1))
        {
        cout << "hello"<<endl;
        cout << head ->next <<endl;
        head =  head->next;
        cout << head ->data <<endl;
        i++;
    }
    cout << i <<endl;
    return head->data;
}

int main(int argc, char const *argv[])
{
    Node * head = new Node;
    head->data = 0;
    head->next = NULL;
    int num;
    cin >>num;
    int x,y;
    for (int i = 0; i < num; ++i)
    {
        cin >> x>>y;
        insertnth(head,x,y);
    }
    // head = Reverse(head);
    // Print(head);
    int node = GetNode(head,2);
    cout << node <<endl;
    return 0;
}