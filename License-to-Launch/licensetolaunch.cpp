#include <iostream>
#include <valarray>

using namespace std;

int main()
{
   int n;
   cin >> n;
   valarray<int> arr(n);

   for (int i = 0; i < n; i++)
   {
      int v;
      cin >> v;
      arr[i] = v; 
   }
   
   int min = arr[0];
   int loc = 0;
   for (int i = 0; i < arr.size(); i++)
       if (arr[i] < min)
       {
         min = arr[i];
         loc = i;
      }

   cout << loc << endl;

   return 0;
}
