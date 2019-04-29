#include <iostream>

using namespace std;

int fib(int);

int main() {
    int n;
    cin >> n;
    
    cout << fib(n-1) << " " << fib(n) << endl;
    
    
    return 0;
}

int fib(int n) {
    if(n <= 1) {
        return n;
    }
    
    int fibo = 1;
    int fiboPrev = 1;
    
    for(int i = 2; i < n; i++) {
        int temp = fibo;
        fibo += fiboPrev;
        fiboPrev = temp;
    }
    return fibo;
}
