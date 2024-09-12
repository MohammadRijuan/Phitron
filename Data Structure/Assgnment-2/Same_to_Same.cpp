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

bool compareLists(Node* head1, Node* head2) 
{
    while (head1 != NULL && head2 != NULL) //true dile test 1,test 2 bar segmentation fault kai...r ei 2ta list NULL na howa porjnto colbe so true howar question e asena
    {
        if (head1->val != head2->val) 
        {
            return false;
        }
        head1 = head1->next;
        head2 = head2->next;
    }
    return head1 == NULL && head2 == NULL; // jodi NULL porjnto coltese amon return na kori tahole testcase 1 wrong ase
}

int main() 
{
    Node* N1 = NULL; //2ta singly linkd list nilam
    Node* N2 = NULL;
    int val;

    //2ta list er jonno 2bar loop nilam

    while (true) 
    {
        cin >> val;
        if (val == -1) 
        {
            break;
        }
        insert_at_tail(N1, val);
    }

    while (true) 
    {
        cin >> val;
        if (val == -1) 
        {
            break;
        }
        insert_at_tail(N2, val);
    }

    if (compareLists(N1, N2))
    {
        cout << "YES";
    } 
    else 
    {
        cout << "NO";
    }
    return 0;
}
