#include <iostream>
#include <string>

using namespace std;

int main()
{
   int n;
   cin >> n;

   for (int i = 0; i < n; i++)
   {
      string a;
      cin >> a;
      
      if (a[0] == 'P')
        cout << "skipped" << endl;
      else
      {
         string num1;
         string num2;
         int i;
         for (i = 0; a[i] != '+'; i++)
         {
             num1 += a[i];
         }
         i++;
         for (int j = i; j < a.length(); j++)
         {
             num2 += a[j];
         }
         
         int output = stoi(num1) + stoi(num2);
         cout << output << endl;
      }
   }
   return 0;
}
