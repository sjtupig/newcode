s = input().strip()
stack = []
now = 0
depth = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
        depth = max(depth, len(stack))
    elif s[i] == ')':
        stack.remove(stack[-1])
print(depth)

'''
链接：https://www.nowcoder.com/questionTerminal/a2d5b1875bb0408384278f40d1f236c9
来源：牛客网

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    string sequence; cin >> sequence;
    int depth = 0, maxDepth = 0;
    for (int i = 0; i < sequence.length(); i++) {
        if (sequence[i] == '(') {
            depth++;
            maxDepth = max(maxDepth, depth);
        }
        else depth--;
    }
    cout << maxDepth << endl;
    return 0;
}
'''