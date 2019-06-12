//
// Created by lenovo on 2019/4/17.
//
//区间贪心
/*
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 110;

struct Inteval{
    int x, y;
}I[MAXN];

//按照左端点由大到小排序，左端点相同按右端点从小到大排序
bool cmp(Inteval a, Inteval b){
    if (a.x != b.x)
        return a.x > b.x;
    else
        return   a.y < b.y;
}

int main(){
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> I[i].x >> I[i].y;
    }
    sort(I, I + n, cmp);
    int ans = 1, lastX = I[0].x;
    for (int i = 1; i < n; ++i) {
        if (I[i].y <= lastX){
            lastX = I[i].x;
            ans ++;
        }
    }

    cout << ans << endl;
    return 0;
}

*/
