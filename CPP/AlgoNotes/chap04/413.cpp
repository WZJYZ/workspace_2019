//
// Created by lenovo on 2019/4/2.
//

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

struct Student{
    char id[15];
    int score;
    int location_number;
    int local_randk;
};
/*
 * 排名的实现：
 * string：可以直接使用关系符号比较。
 * char : 使用strcmp比较。
 * */
bool cmp(Student a, Student b){
    if (a.score != b.score)
        return a.score > b.score;
    else
        return strcmp(a.id, b.id);
}

int main413() {
    /*
     * n:考场数
     * k:考场内人数
     * num:总考生数
     * */
    int n, k, num = 0;
    Student stu[30010];
    //输入考生数据
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> k;
        for (int j = 0; j < k; ++j) {
            cin >> stu[num].id >> stu[num].score;
            stu[num].location_number = i;
            num ++;
        }
    }
    sort(stu + num - k, stu+ num, cmp);
    stu[num - k].local_randk = 1;
    for(int j = num - k + 1; j < num; j++){
        if (stu[j].score == stu[j - 1].score){
            stu[j].local_randk = stu[j - 1].local_randk;
        }else{
            stu[j].local_randk = j + 1 -(num - k);
        }
    }

    //为所有考生排序
    cout << num << endl;
    sort(stu, stu + num, cmp);
    int r = 1;
    for ( int i = 0; i < num; i++){
        if (i > 0 && stu[i].local_randk != stu[i - 1].score){
            r = i + 1;
        }
        cout << stu[i].id << " ";
        cout << r << " " << stu[i].location_number << " " << stu[i].local_randk << endl;
    }
    return 0;
}