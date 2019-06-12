//
// Created by lenovo on 2019/4/3.
//

//字符串hash初步
/*
#include <iostream>
using namespace std;
const int MAXN = 100;
char S[MAXN][5], temp[5];
int hashTable[26 * 26 * 26 + 10];

int hashFunc(char S[], int len){ //哈希函数，将字符串转换为整数
    int id = 0;
    for (int i = 0; i < len; ++i) {
        id = id * 26 + (S[i] - 'A');
    }
    return id;
}
int main422(){
 */
    /*
     * n：字符串个数
     * m：目标字符串个数
     * */
    /*
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> S[i];
        int id = hashFunc(S[i], 3); //将字符串S[i]转换为整数
        hashTable[id] ++ ;//该字符串出现的个数加1
    }

    for (int j = 0; j < m; ++j) {
        cin >> temp;
        int id = hashFunc(temp, 3);
        cout << hashTable[id] << endl;
    }
    */
    /*
    char  a[5];
    cin >> a;
    cout << a << endl;

    return 0;
}
    */