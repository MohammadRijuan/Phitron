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
        Node* p= q.front();
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

void level_order(Node* root,int x)
{
    queue<Node*>q;

    if(root) q.push(root);

    int level=q.size();
    level--;
    bool flag=false;
    while(!q.empty())
    {
        int l=q.size();

        if(level==x)
        {
            while(!q.empty())
            {
                cout<<q.front()->val<<" ";
                q.pop();
            }
            flag=true;
                break;
        }
        for (int i = 0; i < l; i++)
        {
            Node* p=q.front();
            q.pop();

            if(p->left) q.push(p->left);
            if(p->right) q.push(p->right);
        }
        level++;
        
    }
    if(!flag) cout<<"Invalid";
}
int main()
{
    Node* root = input_tree();
    int x;
    cin >> x;
    level_order(root, x);
     
    return 0;
}