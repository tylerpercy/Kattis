#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
   int n;
   vector<int> ans;
   cin >> n;
   
   for (int i = 0; i < n; i++)
   {
       vector<int> guests;
       int g;
       cin >> g;
       for (int j = 0; j < g; j++)
       {
           int a;
           cin >> a;
           guests.push_back(a);
       }

       sort(guests.begin(), guests.end());
       for (int k = 0; k < guests.size(); k++)
       {
           if (guests[k] != guests[k+1] && guests[k] != guests[k-1])
              ans.push_back(guests[k]);

       }

       cout << "Case #" << i+1 << ": " << ans[i] << endl;
   }


   return 0;
}
