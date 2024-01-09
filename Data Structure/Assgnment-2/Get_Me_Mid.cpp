#include<bits/stdc++.h>
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

void insert_at_tail(Node*& head, int v)
{
    Node* newNode = new Node(v);
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

int countlength(Node* head)
{
    int count = 0;
    Node* tmp = head;
    while (tmp != NULL)
    {
        count++;
        tmp = tmp->next;
    }
    return count;
}

void findmid(Node* head)
{
    int size = countlength(head);
    int mid = (size + 1) / 2;
    Node* tmp = head;
    for (int i = 0; i < mid - 1; i++)
    {
        tmp = tmp->next;
    }
    if (size % 2 == 0)
    {
        cout << tmp->val << " " << tmp->next->val << endl;
    }
    else {
        cout << tmp->val << endl;
    }
}

int main()
{
    Node* head = NULL;
    int val;
    while (true)
    {
        cin >> val;
        if (val == -1) break;
        insert_at_tail(head, val);
    }

    for (Node* i = head; i->next != NULL; i = i->next)
    {
        for (Node* j = i->next; j != NULL; j = j->next)
        {
            if (i->val < j->val)
            {
                swap(i->val, j->val);
            }
        }
    }

    findmid(head);

    return 0;
}
