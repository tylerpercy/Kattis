#include <iostream>

using namespace std;

int factorial(int);

int main()
{
   int n;
   cin >> n;
   int arr[n];
   
   for (int i = 0; i < n; i++)
   {
      int x;
      cin >> x;
      int y = factorial(x);
      int ans = y % 10;
      arr[i] = ans;
   }

   for (int i = 0; i < n; i++)
       cout << arr[i] << endl;

   return 0;
}

int factorial(int n)
{
   if (n==0)
      return 1;
   
   return n*factorial(n-1);

}
