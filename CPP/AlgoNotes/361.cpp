//
// Created by lenovo on 2019/4/1.
//
/*
 * 回文串
 * */

#include <iostream>
#include <string>
using namespace std;
const  int MAXN = 256;
bool judge(string str){
    int length = str.length();
    for (int i = 0; i < length / 2; ++i) {
        if (str[i] != str[length -1 -i])
            return false;
    }
    return true;
}

int main361(){
    char str[MAXN];
    cin.getline(str, MAXN);
    bool flag = judge(str);
    if (flag == true)
        cout << "yes" <<endl;
    else
        cout << "no" <<endl;
    return 0;
}