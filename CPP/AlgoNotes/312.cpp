//
// Created by lenovo on 2019/4/1.
//

/*
 * 挖掘机技术哪家强？
 * */

//输入：6
// 3 65
// 2 80
// 1 100
// ...

//输出：2 150
#include <iostream>
using namespace std;

const int  MAXN = 100010;
int school[MAXN] = {0}; //记录每个学校的总分
int main322(){
    int n, schID, score;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> schID >> score; //学校ID,分数
        school[schID] += score; //学校为schID的总分增加score
    }
    int k = 1, MAX = -1; //总分最高的学校ID 和分数
    for (int j = 1; j <= n; ++j) {
        if (school[j] > MAX){
            MAX = school[j];
            k = j;
        }


    }
    cout << k << " " << MAX;
    return 0;
}
