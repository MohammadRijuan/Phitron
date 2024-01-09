class Solution {
public:
    int size(ListNode* head) 
    {
        ListNode* tmp=head;
        int count=0;
        while(tmp!=NULL)
        {
            count++;
            tmp=tmp->next;
        }
        return count;
    }

    ListNode* middleNode(ListNode* head)
    {
        int sz=size(head);
        ListNode* tmp=head;
        for(int i=1;i<=sz/2;i++)
        {
            tmp=tmp->next;
        }
        cout<<slow->val<<" ";
        return tmp;
        
    }
};


class Solution {
public:
    ListNode* middleNode(ListNode* head)
    {
        ListNode* fast=head;
        ListNode* slow=head;
        while(fast!=NULL && fast->next!=NULL)
        {
            slow=slow->next;
            fast=fast->next->next;
        }
        cout<<slow->val<<" ";
        return slow;
    }
};