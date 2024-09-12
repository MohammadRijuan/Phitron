#include <bits/stdc++.h> 
using namespace std;

int findSecondLargest(int n, vector<int> &arr)
{
    // একটি সেট তৈরি করছে, যেটি ইন্টিজারগুলির একটি বিন্যাসে সাজানো হবে বৃহত্তম থেকে ছোট ধরে
    set<int, greater<int>> s;

    // ইনপুট ভেক্টর arr এর প্রতি উপাদানকে সেটে ঢুকিয়ে যাচ্ছে
    for(int i = 0; i < arr.size(); i++)
    {
        s.insert(arr[i]);
    }

    // যদি সেটে শুধুমাত্র একটি উপাদান থাকে তবে -1 রিটার্ন করা হবে
    if(s.size() == 1) return -1;
    else{
        // সেটের দ্বিতীয় উপাদানে পৌঁছার জন্য ইটারেটর ব্যবহার হচ্ছে
        auto it = s.begin();
        it++;

        // দ্বিতীয় উপাদানটি রিটার্ন করা হচ্ছে
        return *it;
    }
}
