//
// Created by lenovo on 2019/4/8.
//

/*
 * 简单贪心算法
 * */
//月饼问题
#include <iostream>
#include <algorithm>
using namespace std;
//定义月饼参数
/*
struct mooncake{
    double store; //库存量
    double sell; //总售价
    double price; //单价
}cake[1010];

bool cmp(mooncake a, mooncake b){
    return a.price > b.price;
}

int main(){
    int n; //月饼种类数
    double D; //需求量
    cin >> n >> D;
    //输入每种月饼的库存量
    for (int i = 0; i < n; ++i) {
        cin >> cake[i].store;
    }
    //输入每种月饼的售价，并计算单价
    for (int i = 0; i < n; ++i) {
        cin >> cake[i].sell;
        cake[i].price = cake[i].sell/cake[i].store;
    }

    sort(cake, cake + n, cmp);

    double ans = 0; //收益
    for (int i = 0; i < n; ++i) {
        if (cake[i].store <= D){
            D -= cake[i].store;
            ans += cake[i].sell;
        }else{
            ans += cake[i].price * D;
            break;
        }
    }
    cout << ans << endl;
    return 0;
}
 */