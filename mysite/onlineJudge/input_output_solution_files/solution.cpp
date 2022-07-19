#include <bits/stdc++.h>

using namespace std;

int main()
{
    int x;
    cin >> x;
    string s1 = to_string(x);
    string s2 = s1;
    reverse(s2.begin(), s2.end());

    if (s1 == s2)
        cout << "YES";
    else
        cout << "NO";

    return 0;
}