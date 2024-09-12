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

void insert_at_tail(Node*& head, Node *&tail,int v) //ata moduke 7 er 7.3 onushare kora..module 6 er onujayi korle timeout kai..karon complexity O(N)cole jaccilo
{
    Node* newNode = new Node(v);
    if (head == NULL) 
    {
        head = newNode;
        tail = newNode;
        return;
    }
    tail->next=newNode;
    tail=newNode;
}

void print_Reverse(Node* n) 
{
    if (n == NULL) 
    {
        return;
    }
    print_Reverse(n->next);
    cout << n->val << " ";
}

void print_recursion(Node* head) //same as print linked list...original value same as testcase
{
    Node* tmp = head;
    while (tmp != NULL) 
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
    cout << endl;
}
int main()
{
    Node* head = NULL;
    Node* tail = NULL;
    int val;
    while (true)
    {
        cin >> val;
        if (val == -1) break;
        insert_at_tail(head, tail, val);
    }
    print_Reverse(head);
    cout<<endl;
    print_recursion(head);



    return 0;
}