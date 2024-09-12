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
        this->val=val;
        this->left=NULL;
        this->right=NULL;
    }
};

Node* input_tree()
{
    int val;
    cin>>val;
    Node* root;
    if(val==-1) root=NULL;
    else root=new Node(val);

    queue<Node*>q;

    if(root!=NULL)
    {
        q.push(root);
    }
    
    while(!q.empty())
    {
        Node * p=q.front();
        q.pop();

        int l,r;
        cin>>l>>r;
        Node* myLeft;
        Node* myRight;

        if(l==-1) myLeft=NULL;
        else myLeft=new Node(l);
        if(r==-1) myRight=NULL;
        else myRight=new Node(r);

        p->left=myLeft;
        p->right=myRight;

        if(p->left) q.push(p->left);
        if(p->right) q.push(p->right);
    }
    return root;
}

void leaf(Node* root, int* mx, int* mn)
{
    if(!root) return;

    if(!root->left && !root->right)
    {
        int maX=*mx;
        int miN=*mn;

        *mx=max(maX,root->val);
        *mn=min(miN,root->val);
    }
    leaf(root->left,mx,mn);
    leaf(root->right,mx,mn);

}

int main()
{
    Node* root=input_tree();
    int mx=INT_MIN;
    int mn=INT_MAX;
    leaf(root,&mx,&mn);
    cout<<mx<< " "<<mn;


     
    return 0;
}