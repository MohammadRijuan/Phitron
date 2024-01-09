#include <bits/stdc++.h>
using namespace std;

class Node
{
    public:
        int val;
        Node* next;
    
        Node(int val)
        {
            this->val = val;
            this->next = NULL;
        }
};


void insert_tail(Node*&head,int val)
{
    Node *newNode=new Node(val);
    if(head==NULL)
    {
        head=newNode;
        return;
    }
    Node*tmp=head;
    while(tmp->next!=NULL)
    {
        tmp=tmp->next;
    }
    tmp->next=newNode;
}


void reverse_list(Node* curr, Node* &start, bool *flag)
{
    if(curr == NULL)
    {
        return;
    }

    reverse_list(curr->next, start, flag);

    if(curr->val == start->val)
    {
        start = start->next;
    }
    else
    {
        *flag = false;
        return;
    }
        
}
bool isPalindrome(Node* head) {
    bool flag = true;
    reverse_list(head, head, &flag);  

    return flag;  
}


int main()
{
    Node* head = NULL;
    Node* tail = head;

    int val;
    while(true)
    {
        cin >> val;
        if(val == -1)
        {
            break;
        }
        
        insert_tail(head,val);
    }

    if(isPalindrome(head) == true)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
}