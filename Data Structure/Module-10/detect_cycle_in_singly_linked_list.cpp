#include<bits/stdc++.h>
using namespace std;

class Node 
{
    public:
    int val;
    Node * next;

    Node(int val)
    {
        this->val=val;
        this->next=NULL;
    }
};

int main()
{
    Node* head= new Node(10);
    Node* a= new Node(20);
    Node* b= new Node(30);
    Node* c= new Node(40);

    //connection
    head->next=a;
    a->next=b;
    b->next=c;
    //c->next=a;
    c->next=NULL;

    Node* slow=head;  //slow r fast head thekey suru korbe..slow 1 dhap r fast 2 dhap kore agabe...
    Node* fast=head;
    bool flag=false;

    while(fast!=NULL && fast->next!=NULL)
    {
        slow=slow->next;
        fast=fast->next->next;
        if(fast==slow)
        {
        flag=true;
        break;
        }
    }
    if(flag==true) cout<<"cycle detected"<<endl;
    else cout<<"no cycle"<<endl;
     
    return 0;
}