//
// Created by lenovo on 2019/4/17.
//

//贪心算法，组个最小数
// 0-9      0 1 2 3 4 5 6 7 8 9
//输入个数：2 2 0 0 0 3 0 0 1 0
//输出：10015558
/*
#include <iostream>

using namespace std;

int main(){
    //输入
    int count[10]; //记录0-9每个数的个数
    for (int i = 0; i < 10; ++i) {
        cin >> count[i];
    }

    //找到第一个不为0的最小的数，并输出,中断
    for (int i = 1; i < 10; ++i) {
        if (count[i] > 0){
            cout << i;
            count[i] --;
            break;
        }
    }

    //
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < count[i]; ++j) {
            cout << i;
        }
    }

    return 0;
}
*/