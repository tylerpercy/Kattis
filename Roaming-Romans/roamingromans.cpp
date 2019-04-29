#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
   float a;
   cin >> a;
   int b = a*1000*(5280./4854.) + .5;
   
   cout << fixed << setprecision(3) << b << endl;


   return 0;
}
