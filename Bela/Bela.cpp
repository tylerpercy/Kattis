#include <iostream>

using namespace std;

int main()
{
   int n;
   int ans = 0;
   char x;

   cin >> n >> x;
   
   for (int i = 0; i < n*4; i++)
   {
      string s;  
      cin >> s;
      char c = s[0];
      char d = s[1];

      switch(c)
      {
         case 'A': ans += 11; break;
         case 'K': ans += 4; break;
         case 'Q': ans += 3; break;
         case 'J': (d==x) ? ans += 20 : ans += 2; break;
         case 'T': ans += 10; break;
         case '9': (d==x) ? ans += 14 : ans += 0; break; 
      }
   }

   cout << ans;


   return 0;
}
