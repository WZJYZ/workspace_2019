//
// Created by lenovo on 2019/5/14.
//
//寻找迷宫最小步数

#include <string>
#include <iostream>
#include <stack>
using namespace std;
string removeKdigits(string num, int k) {

    stack<int>list;
    stack<int>result;
    string s;
    if(num.size()==0||num.size() <=k)
        return "0";
    else
        list.push(num[0]-'0');
    for(int i=1;i<=num.size();++i) {
        int temp = list.top();
        if((num[i]-'0')<temp &&k>0) {
            list.pop();
            k=k-1;
            list.push(num[i]-'0');
        }
        else
            list.push(num[i]-'0');
    }
    while(!list.empty()) {
        int tmp;
        tmp = list.top();
        list.pop();
        result.push(tmp);
    }
    while(!result.empty()) {
        int tmp1 = result.top();
        result.pop();
        s.push_back(tmp1+'0');

    }
    cout<<"1:"<<s<<endl;
    s.resize(num.size()-k-2);
    cout<<"1:"<<s<<endl;
    cout <<"2:"<< s.size() << endl;
    while(s[0]=='0') {
        //s=s.substr(1);
        s.erase(0, 1);
    }
    cout<<"3:"<<s<<endl;
    cout<<"4:"<<s.size()<<endl;
    if(s=="\0")
        return "0";
    else
        return s;
}

int main279(){

    string s = "10200";

    string res = removeKdigits(s, 2);
    cout << res << endl;
}
