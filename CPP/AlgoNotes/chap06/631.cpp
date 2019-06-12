//
// Created by lenovo on 2019/4/22.
//

// are they equal
//字符串处理
//page211
#include <iostream>
#include <string>
using namespace std;
/*
int n; //有效位数

string deal(string s, int &e){
    int k = 0; //s的下标
    while (s.length() > 0 && s[0] == '0'){
        s.erase(s.begin()); //去掉s的前导0
    }
    if (s[0] == '.'){ //s是小于1的小数
        s.erase(s.begin()); //去掉小数点
        while (s.length() > 0 && s[0] == '0'){
            s.erase(s.begin()); //去掉小数点后非零位前的所有零
            e--; //指数e减一
        }
    }else { //找到小数点
        while (k < s.length() && s[k] != '.') {
            k++;
            e++;
        }
        if (k < s.length()) {
            s.erase(s.begin() + k); //删除小数点
        }
    }
    if (s.length() == 0){
        e = 0; //去掉前导0后s的长度变为0，说明这个数是0
    }

    int num = 0;
    k = 0;
    string res;
    while (num < n){
        if (k < s.length())
            res += s[k++];
        else
            res += '0';
        num++;
    }

    return res;
}

int main(){
    string s1, s2, s3, s4;
    cin >> n >> s1 >> s2;
    int e1 = 0, e2 = 0;
    s3 = deal(s1, e1);
    s4 = deal(s2, e2);
    if (s3 == s4 && e1 == e2){
        cout << "YES 0."<< s3 <<"*10^"<<e1<<endl;
    }else{
        cout <<"NO 0."<<s3<<"*10^"<<e1<<"  0."<<s4<<"*10^"<<e2<<endl;
    }
    return 0;
}*/