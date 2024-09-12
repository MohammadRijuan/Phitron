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
    Node*root;
    if(val==-1) 
        root=NULL;
    else 
        root=new Node(val);
     queue<Node*>q;
     if(root!=NULL) //if(root) eibave o likha jabe
     q.push(root);
     while(!q.empty())
     {
        //ber kore ana
        Node* p=q.front();
        q.pop();

        //jabotiyo kaj
        int l,r;
        cin>>l>>r;
        Node* myLeft;
        Node* myRight;

        if(l==-1)
        {
            myLeft=NULL;
        }
        else
        {
            myLeft=new Node(l);
        }
        if(r==-1)
        {
            myRight=NULL;
        }
        else
        {
            myRight=new Node(r);
        }
        p->left=myLeft;
        p->right=myRight;

        //child ke push kora
        if(p->left!=NULL)
        {
            q.push(p->left);
        }
        if(p->right!=NULL)
        {
            q.push(p->right);
        }
     }   
     return root;
}

void level_order(Node* root)
{
    if(root==NULL) 
    {
        cout<<"TREE nai";
    }
    queue<Node*>q;
    q.push(root);
    while(!q.empty())
    {
        //1. ber kore ana
        Node* p=q.front();
        q.pop();

        //2. jabotiyo kaj kora
        cout<<p->val<<" ";

        //3. child ke push kora
        if(p->left!=NULL)
        {
            q.push(p->left);
        }
        if(p->right!=NULL)
        {
            q.push(p->right);
        }   
    }
}
int main()
{
    Node* root=input_tree();
    level_order(root);
     
    return 0;
}