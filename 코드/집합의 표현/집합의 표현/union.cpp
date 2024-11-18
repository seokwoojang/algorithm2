#include <iostream>
#include <vector>
using namespace std;

vector<int> parent;

int find(int i) {
    if (parent[i] != i) {
        parent[i] = find(parent[i]); // 경로 압축
    }
    return parent[i];
}

void unionSets(int a, int b) {
    a = find(a);
    b = find(b);
    if (a < b) {
        parent[b] = a;
    }
    else {
        parent[a] = b;
    }
}

int main() {
    //입출력 속도 최적화
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    parent.resize(n + 1);
    for (int i = 0; i <= n; i++) {
        parent[i] = i;
    }

    for (int r = 0; r < m; r++) {
        int o, a, b;
        cin >> o >> a >> b;

        if (o == 0) {
            if (a != b) {
                unionSets(a, b);
            }
        }
        else {
            if (find(a) == find(b)) {
                cout << "YES\n";
            }
            else {
                cout << "NO\n";
            }
        }
    }

    return 0;
}
