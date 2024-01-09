#include <stdio.h>

int main() {
    int T;  // Number of test cases
    scanf("%d", &T);
    
    for (int caseNum = 1; caseNum <= T; caseNum++) {
        int N;  // Size of the list
        scanf("%d", &N);
        
        int numbers[N];  // Values of the list
        
        for (int i = 0; i < N; i++) {
            scanf("%d", &numbers[i]);
        }
        
        int S;  // Number to find
        scanf("%d", &S);
        
        int found = 0;
        int position = -1;
        
        for (int i = 0; i < N; i++) {
            if (numbers[i] == S) {
                found = 1;
                position = i + 1;
                break;
            }
        }
        
        if (found) {
            printf("Case %d: %d\n", caseNum, position);
        } else {
            printf("Case %d: Not Found\n", caseNum);
        }
    }
    
    return 0;
}
