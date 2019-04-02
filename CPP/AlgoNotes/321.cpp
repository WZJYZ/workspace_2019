//
// Created by lenovo on 2019/4/1.
//
/*
 * 找元素之找x
 * */
#include <iostream>
using namespace std;
const int MAXN = 210;
int a[MAXN]; //存放N个数
int main321(){
    int n, x;
    while (cin >> n){
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        cin >> x;
        int k = 0;//目标下标值
        for (int j = 0; j < n; ++j) {
            k == j;
            if (a[j] == x){
                cout << j << endl;
                break;
            }

        }
        if (k == n-1){
            cout << "-1" << endl;
        }

    }
    return 0;
}
