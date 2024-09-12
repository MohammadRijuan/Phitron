stack<int> pushatBottom(stack<int>&st,int x)
{
    stack<int>newSt;
    while(!st.empty())
    {
        newSt.push(st.top());
        st.pop();
    }
    newSt.push(x);
    while(!newSt.empty())
    {
        st.push(newSt.top());
        newSt.pop();
    }
    return st;
}