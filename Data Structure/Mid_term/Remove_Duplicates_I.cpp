#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    Node* next;

    Node(int val) 
    {
        this->val = val;
        this->next = NULL;
    }
};

void insert_tail(Node*& head, int val) 
{
    Node* newNode = new Node(val);
    if (head == NULL) 
    {
        head = newNode;
        return;
    }
    Node* tmp = head;
    while (tmp->next != NULL) 
    {
        tmp = tmp->next;
    }
    tmp->next = newNode;
}

void print_linked_list(Node* head) 
{
    Node* tmp = head;
    while (tmp != NULL) 
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
}

void sort(Node* head) 
{
    Node* tmp = head;
    for (auto i = tmp; i != NULL; i = i->next) 
    {
        for (auto j = i->next; j != NULL; j = j->next) 
        {
            if (i->val > j->val) 
            {
                swap(i->val, j->val);
            }
        }
    }
}

void removeDuplicates(Node* head) 
{
    Node* tmp = head;
    if(head==NULL) return;
    while (tmp != NULL && tmp->next != NULL) 
    {
        if (tmp->val == tmp->next->val) 
        {
            tmp->next = tmp->next->next;
        } 
        else 
        {
            tmp = tmp->next;
        }
    }
}

/*Node* deleteDuplicates(Node* head) {
        if (head==NULL) return head;
        Node* tmp=head;
        while(tmp->next!=NULL)
        {
            if(tmp->val==tmp->next->val)
            {
                tmp->next=tmp->next->next;
            }
            if(tmp->next==NULL) break;
            else if(tmp->val!=tmp->next->val)
            {
                tmp=tmp->next;
            }
        }
        return head;
        
    }*/


int main() 
{
    Node* head = NULL;
    int val;
    while (true) 
    {
        cin >> val;
        if (val == -1)
            break;

        insert_tail(head, val);
    }
    //sorting na korle ,remove function kaj e korce na...tai aghe sort kore nite hbe...then remove function execute hoy..
    sort(head);
    removeDuplicates(head);

    print_linked_list(head);

    return 0;
}
