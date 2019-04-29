#include <iostream>
#include <string>


using namespace std;
  
int main()
{
  int n;
  cin >> n;  
  string arrA[n];
  string arrB[n];
  string arrAns[n];
 
  for (int i = 0; i < n; i++)
  {
         string a;
         string b;
         string s;
         cin >> a >> b;
         arrA[i] = a;
         arrB[i] = b;
 
         for (int j = 0; j < arrA[i].length(); j++)
         {
             if ((arrA[i])[j] == (arrB[i])[j])
                s += ".";
            else
                s += "*";
         }

      arrAns[i] = s;
  }
 
     for (int i = 0; i < n; i++)
     {
         cout << arrA[i] << endl << arrB[i] << endl << arrAns[i] << endl;
     }

 
 
     return 0;
}
