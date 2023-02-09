#include <bits/stdc++.h>

using namespace std;

int V, E;

struct Edge {
    int u, v, w;
    Edge(int u, int v, int w) : u(u), v(v), w(w) {}
    bool operator<(const Edge &e) const {
        return w < e.w;
    }
};

int parent[10001];

int find(int u) {
    if (u == parent[u]) return u;
    return parent[u] = find(parent[u]);
}

void merge(int u, int v) {
    u = find(u);
    v = find(v);
    if (u == v) return;
    parent[u] = v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> V >> E;
    vector<Edge> edges;
    for (int i = 0; i < E; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.emplace_back(u, v, w);
    }
    sort(edges.begin(), edges.end());
    for (int i = 1; i <= V; i++) parent[i] = i;
    int ans = 0;
    for (auto &e : edges) {
        if (find(e.u) != find(e.v)) {
            merge(e.u, e.v);
            ans += e.w;
        }
    }
    cout << ans << '\n';
    return 0;
}