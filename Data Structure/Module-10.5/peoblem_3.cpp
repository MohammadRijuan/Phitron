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

bool Palindrome(Node* head)
{
    if (head == NULL)
        return true;

    Node* start = head;
    Node* end = head;


    while (end->next != NULL)
        end = end->next;

    
    while (start != end && start->prev != end)
    {
        if (start->val != end->val)
            return false;

        start = start->next;
        end = end->prev;
    }

    return true;
}

int main()
{
    Node* head = NULL;
    Node* tail = NULL;
    int val;

    // Input values until -1 is encountered
    while (true)
    {
        cin >> val;
        if (val == -1)
            break;
        insert_tail(head, tail, val);
    }

    // Check if the doubly linked list is a palindrome
    if (Palindrome(head))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    return 0;
}
