//
// Created by lenovo on 2019/4/17.
//

//two pointers

//问题
//1 2 3 4 5 6
//M = 8
//2+6=8, 3+5=8
/*
#include <iostream>

using namespace std;

int main(){
    int arr[] = {1, 2, 3, 4, 5, 6};
    int m = 8;
    int i = 0, j = sizeof(arr)/ sizeof(int) - 1;
    cout << j << endl;
    while (i < j){
        if (arr[i] + arr[j] == m){
            cout <<arr[i] <<" "<<arr[j]<<endl;
            i++;
            j--;
        }else if (arr[i] + arr[j] < m){
            i++;
        }else{
            j--;
        }
    }
    return 0;
}
*/