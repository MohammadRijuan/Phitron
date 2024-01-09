#include<bits/stdc++.h>
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
        this->next = NULL;
        this->prev = NULL;
    }
};

void print_normal(Node* head)
{
    Node* tmp = head;
    while (tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
    cout << endl;
}

void insert_tail(Node*& head, Node*& tail, int val)
{
    Node* newNode = new Node(val);
    if (head == NULL)
    {
        head = newNode;
        tail = newNode;
        return;
    }
    tail->next = newNode;
    newNode->prev = tail;
    tail = tail->next;
}

/*bool areEqual(Node* head1, Node* head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->val != head2->val)
            return false;

        head1 = head1->next;
        head2 = head2->next;
    }

    return (head1 == NULL && head2 == NULL);
}*/

int main()
{
    Node* head1 = NULL;
    Node* tail1 = NULL;

    Node* head2 = NULL;
    Node* tail2 = NULL;

    int val1,val2;
    bool flag=false;
    while (true)
    {
        cin >> val1;
        if (val1== -1)
            break;
        insert_tail(head1, tail1, val1);
    }

    while (true)
    {
        cin >> val2;
        if (val2 == -1)
            break;
        insert_tail(head2, tail2, val2);
        if(val1!=val2)
    {
        flag=false;
    }
    }

    if(flag==true)
    cout<<"YES";
    else
    {
        cout<<"NO";

    }

    /*if (areEqual(head1, head2))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;*/

    return 0;
}
