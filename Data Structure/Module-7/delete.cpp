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

void delete_Node(Node* head,int pos)
{
    Node* tmp=head;
    for (int i = 1; i <=pos-1; i++)
    {
        tmp=tmp->next;
    }
    Node * deleteNode =tmp->next;
    tmp->next=tmp->next->next;
    delete deleteNode;
    
}

int size(Node * head)  //jehetu int return korci sehetu void er poriborte int hobe
{
    Node * tmp=head;
    int count=0;
    while(tmp!=NULL)
    {
        count++;
        tmp=tmp->next;
    }
    return count;
}
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

void delete_head(Node * head)
{
    Node * deleteNode=head;
    head=head->next;
    delete deleteNode;
    return;
}
int main()
{
    Node * head=new Node(10);
    Node * a=new Node(20);
    Node * b=new Node(30);
    Node * c=new Node(40);
    Node * d=new Node(50);
    Node* tail=d;
    head->next=a;
    a->next=b;
    b->next=c;
    c->next=d;
    print_linked_list(head);
    int pos;
    cin>>pos;

    if(pos>size(head))
    {
        cout<<"Invalid index"<<endl;
    }
    else if(pos==0)
    {
        delete_head(head);
    }
    else
    {
        delete_Node(head,pos);
    }
    print_linked_list(head);
    return 0;
}