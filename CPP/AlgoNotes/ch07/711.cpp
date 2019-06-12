//
// Created by lenovo on 2019/4/24.
//
//栈的应用，简单计算器
/**
 * 步骤1：中缀表达式转换为后缀表达式
 * 步骤2：计算后缀表达式
 */
#include <iostream>
#include <stack>
#include <string>
#include <queue>
#include <map>

using namespace std;

struct node{
    double num; //操作数
    char op; //操作符
    bool flag; //true:num,false:op
};

string str;
stack<node> s; //操作符栈
queue<node> q; //后缀表达式序列
map<char, int> op; //记录操作符优先级：*/ > +-

void change(){
    //double num;
    node temp;
    for (int i = 0; i < str.length(); ) {
        if (str[i] >= '0' && str[i] <= '9'){ //如果是数字，就将字符转换为数字
            temp.flag = true;
            temp.num = str[i++] - '0'; //"234"
            while (i < str.length() && str[i] >= '0' && str[i] <= '9'){
                temp.num = temp.num * 10 + (str[i] - '0');
                i++;
            }
            q.push(temp);
        }else{ //若果是操作符。就比较优先级
            temp.flag = false;
            //如果当前操作符的优先级小于等于操作符栈顶元素，就不断弹出
            //到后缀表达式序列中
            while (!s.empty() && op[str[i]] <= op[s.top().op]){
                q.push(s.top());
                s.pop();
            }
            //如果当前操作符的优先级大于操作符栈顶元素，直接入栈
            temp.op = str[i];
            s.push(temp);
            i++;
        }
    }
    //若果操作符栈不为空，弹出
    while (!s.empty()){
        q.push(s.top());
        s.pop();
    }
}

//计算后缀表达式序列
double cal(){
    double temp1, temp2;
    node cur, temp;
    while (!q.empty()){
        cur = q.front();
        q.pop();
        if(cur.flag == true){ //操作数直接入栈
            s.push(cur);
        }else{
            temp2 = s.top().num;
            s.pop();
            temp1 = s.top().num;
            s.pop();
            temp.flag = true;
            if (cur.op == '+')
                temp.num = temp1 + temp2;
            else if (cur.op == '-')
                temp.num = temp1- temp2;
            else if (cur.op == '*')
                temp.num = temp1 * temp2;
            else temp.num = temp1 / temp2;
            s.push(temp);
        }
    }
    return s.top().num;
}

int main711(){

    op['+'] = op['-'] = 1;
    op['*'] = op['/'] = 2;
    getline(cin, str);
    for (string::iterator it = str.end(); it != str.begin(); it--){
        if (*it == ' ') //删除空格
            str.erase(it);
    }
    while (!s.empty())
        s.pop(); //清空栈，初始化
    change();
    cout<< cal() << endl;
    return 0;
}


