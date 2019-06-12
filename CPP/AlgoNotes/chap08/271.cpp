//
// Created by lenovo on 2019/5/14.
//

//背包问题，使用DFS解决

#include <iostream>
#include <cstdio>
using namespace std;
/*
const int maxn = 30;
//物品数量， 背包容量，最大价值
int n, V, maxValue = 0;
int w[maxn], c[maxn]; //每件物品的重量和价值

void DFS(int index, int sumW, int sumC) {

    //递归终止条件
    if (index == n){
        if (sumW <= V && sumC > maxValue) {
            maxValue = sumC;
        }
        return;
    }

    //递归式
    DFS(index + 1, sumW, sumC); //选择该物品
    DFS(index + 1, sumW + w[index], sumC + c[index]);//不选择该物品
}

int main(){
    //cin >> n >> V;
    scanf("%d%d", &n, &V);
    for (int i = 0; i < n; ++i) {
        //cin >> w[i];
        scanf("%d", &w[i]);
    }
    for (int j = 0; j < n; ++j) {
        //cin >> c[j];
        scanf("%d", &c[j]);
    }
    DFS(0, 0, 0);
    cout << maxValue << endl;
    return 0;
}
*/
