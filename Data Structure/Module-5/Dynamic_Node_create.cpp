#include<bits/stdc++.h>
using namespace std;
class Node
{
    public :
    int val;
    Node* Next;

    Node(int val)
    {
        this->val=val;
        this->Next=Next;
    }
};
int main()
{
    //Node head(10)
    Node* head =new Node (10);
    Node* a =new Node (20); //egulo nijeray address

    head->Next=a; //tai eikane r & use korte hobena

    cout<<head->val<<endl;
    cout<<a->val<<endl;
    cout<<head->Next->val<<endl;
    //cout<<(*head.Next).val<<endl; //ata error kabe karon head nijey pointer
     
    return 0;
}