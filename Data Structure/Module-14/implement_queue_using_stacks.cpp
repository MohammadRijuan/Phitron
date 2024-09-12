int pop() {
        stack<int>newst;
        int last;
        while(!st.empty())
        {
            int k=st.top();
            st.pop();

            if(st.empty())
            {
                //last element e
                last=k;
                break;
            }
            newst.push(k);
        }
        while(!newst.empty())
        {
            st.push(newst.top());
            newst.pop();
        }
        return last;
    }
    
    int peek() {
        stack<int>newst;
        int last;
        while(!st.empty())
        {
            int k=st.top();
            st.pop();

            if(st.empty())
            {
                //last element e
                last=k;
            }
            newst.push(k);
        }
        while(!newst.empty())
        {
            st.push(newst.top());
            newst.pop();
        }
        return last;

        
    }