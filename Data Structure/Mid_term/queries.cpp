#include <bits/stdc++.h>
using namespace std;

class Node
{
    public:
        int val;
        Node* next;
        Node* prev;

        Node(int val)
        {
            this->val = val;
            this->next =NULL;
            this->prev =NULL;
        }
};

void print_normal(Node* head)
{
    Node* tmp = head;
    while(tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
}
void print_reverse(Node* tail)
{
    Node* tmp = tail;
    while(tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp = tmp->prev;
    }
}

void insert_tail(Node* &head, Node* &tail, int val)
{
    Node* newNode = new Node(val);
    if(tail == NULL)
    {
        head = newNode;
        tail = newNode;
        return;
    }

    tail->next = newNode;
    newNode->prev = tail;
    tail = tail->next;
}

void insert_head(Node*& head,Node*& tail, int val)
{
    Node*newNode =new Node (val);
    if(head==NULL)
    {
        head=newNode;
        tail=newNode;
        return;
    }
    newNode->next=head;
    head->prev=newNode;
    head=newNode;
}


void insert_at_position(Node* &head, int pos, int val)
{
    Node* newNode = new Node(val);
    Node* tmp = head;
    for(int i = 0; i < pos - 1; i++)
    {
        tmp = tmp->next;
    }

    newNode->next = tmp->next;
    tmp->next = newNode;
    newNode->prev = tmp;
    newNode->next->prev = newNode;
}

int size(Node* head)
{
    Node* tmp = head;
    int cnt = 0;
    while(tmp != NULL)
    {
        cnt++;
        tmp = tmp->next;
    }
    return cnt;
}

int main()
{
    Node* head = NULL;
    Node* tail = NULL;
    int Q;
    cin >> Q;

    while(Q--)
    {
        int x, v;
        cin >> x >> v;

        if(x > size(head))
        {
            cout << "Invalid" << endl;
            continue;
        }
        else if(x == 0)
        {
            insert_head(head, tail, v);
        }
        else if(x == size(head))
        {
            insert_tail(head, tail, v);
        }
        else
        {
            insert_at_position(head, x, v);
        }

        cout <<"L -> ";
        print_normal(head);
        cout << endl;

        cout <<"R -> ";
        print_reverse(tail);
        cout << endl;
    }
}