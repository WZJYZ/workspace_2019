//
// Created by lenovo on 2019/5/14.
//

//bfs
/*
#include <iostream>
#include <queue>
using namespace std;

const int maxn = 100;

struct node {
    int x;
    int y;
} Node;

int n = 6, m = 7;
int matrix[maxn][maxn] = {{0, 1, 1, 1, 0, 0, 1},
                          {0, 0, 1, 0, 0, 0, 0},
                          {0, 0, 0, 0, 1, 0, 0},
                          {0, 0, 0, 1, 1, 1, 0},
                          {1, 1, 1, 0, 1, 0, 1},
                          {1, 1, 1, 1, 0, 0, 0}};
bool inq[maxn][maxn] = {false};
int X[4] = {0, 0, 1, -1};
int Y[4] = {1, -1, 0, 0};

bool judge(int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m) {
        return false;
    }
    if (matrix[x][y] == 0 || inq[x][y] == true) {
        return false;
    }
    return true;
}

void BFS(int x, int y) {
    queue<node> Q;
    Node.x = x;
    Node.y = y;
    Q.push(Node);
    inq[x][y] = true;
    while (!Q.empty()) {
        node cur = Q.front();
        Q.pop();

        for (int i = 0; i < 4; ++i) {
            int newX = cur.x + X[i];
            int newY = cur.y + Y[i];

            if (judge(newX, newY)) {
                Node.x = newX;
                Node.y = newY;
                Q.push(Node);
                inq[newX][newY] = true;
            }
        }
    }
}

void DFS(int x, int y) {
    if (!judge(x, y)) {
        return;
    }
    inq[x][y] = true;
    DFS(x + 1, y);
    DFS(x, y + 1);
    DFS(x - 1, y);
    DFS(x, y - 1);
}

int main() {

    int ans = 0;
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < m; ++y) {
            if (matrix[x][y] == 1 && inq[x][y] == false) {
                ans++;
                //BFS(x, y);
                DFS(x, y);
            }
        }
    }
    cout << ans << endl;
    return 0;
}

*/