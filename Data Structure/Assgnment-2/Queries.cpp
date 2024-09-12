#include <bits/stdc++.h>
using namespace std;

class Node 
{
public:
    Node* next;
    int val;

    Node(int val) 
    {
        this->next = NULL;
        this->val = val;
    }
};

void insert_head(Node*& head, int val) 
{
    Node* newNode = new Node(val);
    newNode->next = head;
    head = newNode;
}


void insert_at_tail(Node*& head, Node*& tail, int v) 
{
    Node* newNode = new Node(v);
    if (tail == NULL) 
    {
        head = tail = newNode;
    } 
    else 
    {
        tail->next = newNode;
        tail = newNode;
    }
}

void print_head_tail(Node* head, Node* tail) 
{
    if (head == NULL) 
    {
        cout << "Empty ";
    } 
    else 
    {
        cout << head->val << " ";
    }

    if (tail == NULL) 
    {
        cout << "Empty ";
    } 
    else 
    {
        cout << tail->val << " ";
    }
    cout << endl;
}



int main() 
{
    int q;
    cin >> q;

    Node* head = NULL;
    Node* tail = NULL;

    for (int i = 0; i < q; i++) 
    {
        int x, v;
        cin >> x >> v;
        if (x == 0) 
        {
            insert_head(head, v);
        } 
        else 
        {
            insert_at_tail(head, tail, v);
        }
        print_head_tail(head, tail);
    }

    return 0;
}
