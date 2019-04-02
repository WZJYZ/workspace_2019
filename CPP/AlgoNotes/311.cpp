//
// Created by lenovo on 2019/4/1.
//

/*
 * 卡拉兹猜想
 *
 * */
#include <iostream>
using namespace std;
int main311(){
    int n, step = 0; //输入值和步数
    cin >> n;
    while (n != 1){
        if (n % 2 == 0)
            n = n / 2;
        else
            n = (3 * n + 1) / 2;
        step ++;
    }
    cout << step << endl;
    return 0;
}
