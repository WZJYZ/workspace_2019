//
// Created by lenovo on 2019/5/14.
//
/*
#include <iostream>
#include <vector>

using namespace std;

const int maxn = 10;
//从n个数选择k个数，其和为x，最大平方和为maxSumSqu
int n, k, x, maxSumSqu = -1, A[maxn];

vector<int > temp, ans;

void DFS(int index, int nowK, int sum, int sumSqu) {
    //找到最佳值
    if (nowK == k and sum == x) {
        if (sumSqu > maxSumSqu) {
            maxSumSqu = sumSqu;
            ans = temp;
        }
        return;
    }
    //为找到
    if (index == n || nowK > k || sum > x)
        return;

    temp.push_back(index);
    DFS(index + 1, nowK + 1, sum + A[index], sumSqu + A[index] * A[index]);
    temp.pop_back();
    DFS(index + 1, nowK, sum, sumSqu);
}


int main() {
    n = 4;
    k = 2;
    x = 6;
    A[0] = 2;
    A[1] = 3;
    A[2] = 3;
    A[3] = 4;
    DFS(0, 0, 0, 0);

    for (auto x: ans) {
        cout << x << endl;
    }
    cout << ans[0] << ans[1] << endl;
    return 0;
}
*/