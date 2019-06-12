//
// Created by lenovo on 2019/4/3.
//
//分治和·递归
//分治可以使用递归实现，也可以不使用递归实现。
//例子

#include <iostream>
using  namespace std;
/*
 * 1. 求阶乘 n!
 * F(n) = F(n - 1) * n
 *
 * */
/*

int F(int n){
    if (n == 0) //递归边界
        return 1;
    else
        return F(n - 1) * n; //递归式
}
*/
/**
 * 2.全排列（Full permutation）问题。
 * 比如1，2，3
 * ｛（1，2，3），（1，3，2），（2，1，3）...（3，2，1）｝
 *
 * */
//const int MAXN = 11;
//int n, P[MAXN], hashTable[MAXN] = {false};
//第index位数字
/*
void generateP(int index){
    if(index == n + 1){
        for (int i = 1; i <= n; ++i) {
            cout << P[i] << " ";
        }
        cout << endl;
        return ;
    }

    for(int x = 1; x <= n; x++){
        if(hashTable[x] == false){
            P[index] = x;
            hashTable[x] = true;
            generateP(index + 1);
            hashTable[x] = false;
        }
    }

}
 */
/*
 * n皇后
 * */
/*
int count = 0; //计数
void generateP(int index){
    if(index == n + 1){
        bool flag = true;
        for (int i = 1; i <= n; ++i) { //遍历任意两个皇后是否在同一条对角线上。
            for (int j = i + 1; j <= n; ++j) {
                if(abs(i - j) == abs(P[i] - P[j])){
                    flag = false;
                }
            }
        }
        if (flag)
            count++;
        return ;
    }

    for(int x = 1; x <= n; x++){
        if(hashTable[x] == false){
            P[index] = x;
            hashTable[x] = true;
            generateP(index + 1);
            hashTable[x] = false;
        }
    }

}
int main432(){
    n = 3;
    //cout << F(n) << endl;
    generateP(1);

    return 0;
}
*/