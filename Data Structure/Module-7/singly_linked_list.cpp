#include<bits/stdc++.h>
using namespace std;

class Node 
{
    public :
    Node * next;
    int val;

    Node (int val)
    {
        this->next=NULL;
        this->val=val;
    }
};
void print_linked_list(Node * head)
{
    Node * tmp=head;
    while(tmp!= NULL)
    {
        cout<<tmp->val<<" ";
        tmp=tmp->next;
    }
    cout<<endl;

}
int main()
{
    Node * head=new Node(10);
    Node * a=new Node(20);
    Node * b=new Node(30);
    Node * c=new Node(40);
    Node * d=new Node(50);
    head->next=a;
    a->next=b;
    b->next=c;
    c->next=d;
    print_linked_list(head);
    return 0;
}