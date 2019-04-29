#include <iostream>
#include <string>
#include <cmath>

using namespace std;

bool checkPrime(int a)
{
   for (int i = 0; i < sqrt(a); i++)
   {
       if (a % i == 0)
         return false;
   }
   
   return true;
}



int main()
{
   int n;
   cin >> n;
   
   for (int i = 0; i < n; i++)
   {
       string input;
       cin >> input;
       int* arr = new int[size];

       cout << size << endl;
   }


   return 0;
}
