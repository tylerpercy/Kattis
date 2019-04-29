#include <iostream>
#include <map>
#include <algorithm>
#include <set>
#include <functional>

using namespace std;

int main()
{
   int n;
   cin >> n;
   map<string, string> test;
   map<string, int> yeet;
                   
   for (int i = 0; i < n; i++)
   {
       string r, s;
       
       cin >> r >> s;
       test[r] = s;

       int b = atoi(r.c_str());
       int c = atoi(s.c_str());

       if (c == 0)
       {
          b/=2;
          yeet[s] = b;
       }
       else
          yeet[r] = c;
      
   }
 
   typedef function<bool(pair<string, int>, pair<string, int>)> Compare;

   Compare compFunc = [](pair<string, int> x, pair<string, int> y)
                      {
                          return x.second < y.second;
                      };

   set<pair<string, int>, Compare> myset(yeet.begin(), yeet.end(), compFunc);

   for (auto elem : myset)
       cout << elem.first << endl;

   return 0;
}
