#include <bits/stdc++.h>
using namespace std;

class Node 
{
public:
    int val;
    Node* Next;

    Node(int val)
    {
        this->Next = NULL;
        this->val = val;
    }
};


void insert_at_tail(Node*& head, int v) 
{
    Node* newNode = new Node(v);

    if (head == NULL) 
    {
        head = newNode;
    }
    else 
    {
        Node* tmp = head;
        while (tmp->Next != NULL) 
        {
            tmp = tmp->Next;
        }
        tmp->Next = newNode;
    }
}

void Max_Min(Node* head, Node*& max, Node*& min) 
{
    if (head == NULL) 
    {
        max = NULL;
        min = NULL;
        return;
    }

    max = head;
    min = head;

    Node* tmp = head;
    while (tmp != NULL) 
    {
        if (tmp->val > max->val) 
        {
            max = tmp;
        }
        if (tmp->val < min->val) 
        {
            min = tmp;
        }
        tmp = tmp->Next;
    }
}

int main() 
{
    Node* head = NULL;
    int val;

    while (true) //choltey thakbe 
    {
        cin >> val;
        if (val == -1) 
        {
            break;
        }
        insert_at_tail(head, val);
    }

    Node* max = NULL;
    Node *min = NULL;
    Max_Min(head, max, min);

    cout << max->val << " " << min->val << endl;

    return 0;
}