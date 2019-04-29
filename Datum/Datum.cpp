#include <iostream>

using namespace std;

int main()
{
   int arr[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
   string w[] = {"Thursday", "Friday", "Saturday",
                 "Sunday", "Monday", "Tuesday", "Wednesday"};
   int a, b, c;
   cin >> a >> b;

   for (int i = 0; i < 12; i++)
   {
        arr[i+1] += arr[i];
        c = (arr[b-1] + a-1) % 7;
   }

   cout << w[c] << endl;

   return 0;
}
