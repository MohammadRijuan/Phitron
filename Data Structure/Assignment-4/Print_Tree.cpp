#include<bits/stdc++.h>
using namespace std;

class Node
{
public:
    int val;
    Node* left;
    Node* right;

    Node(int val)
    {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
};

Node* input_tree()
{
    int val;
    cin >> val;
    Node* root;
    if (val == -1) root = NULL;
    else root = new Node(val);

    queue<Node*> q;

    if (root != NULL)
    {
        q.push(root);
    }

    while (!q.empty())
    {
        Node* p = q.front();
        q.pop();

        int l, r;
        cin >> l >> r;

        Node* myLeft;
        Node* myRight;

        if (l == -1) myLeft = NULL;
        else myLeft = new Node(l);

        if (r == -1) myRight = NULL;
        else myRight = new Node(r);

        p->left = myLeft;
        p->right = myRight;

        if (p->left) q.push(p->left);
        if (p->right) q.push(p->right);
    }
    return root;
}

void reverseOrder(Node* root)
{
    vector<int> v;
    queue<Node*> q;

    if (root) q.push(root);

    while (!q.empty())
    {
        Node* p = q.front();
        q.pop();

        v.push_back(p->val);

        if (p->right) q.push(p->right);
        if (p->left) q.push(p->left);
    }

    reverse(v.begin(), v.end());

    for (int val : v)
    {
        cout << val << " ";
    }
}

int main()
{
    Node* root = input_tree();
    reverseOrder(root);

    return 0;
}
