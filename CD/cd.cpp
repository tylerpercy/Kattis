#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
   int n, m;

   //vector<int> jack;
   //vector<int> jill;
   //vector<int> shared;

   while (cin >> n >> m && n != 0 && m != 0)
   {

      vector<int> jack, jill, shared;
      
      for (int i = 0; i < n; i++)
      {
          int val;
          cin >> val;
          jack.push_back(val);
      }

      for (int i = 0; i < m; i++)
      {
          int val;
          cin >> val;
          jill.push_back(val);
      }

      set_intersection(jack.begin(), jack.end(), jill.begin(), jill.end(), back_inserter(shared));
   
   
      cout << shared.size() << endl;  
   }
  
}
