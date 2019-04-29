#include <iostream>

using namespace std;

int main()
{
   int total = 0;
   int x;
   cin >> x;

   int n;
   cin >> n;

   for (int i = 0; i < n; i++)
   {
       int a;
       cin >> a;
       total += x-a;
   }   

   total+=x;
   cout << total << endl;

   return 0;
}
