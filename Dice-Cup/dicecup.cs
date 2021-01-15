using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication9
{
    class Program
    {
      
        static void Main(string[] args)
        {
            string[] dice = Console.ReadLine().Split();

            int d1 = Convert.ToInt32(dice[0]);
            int d2 = Convert.ToInt32(dice[1]);

            if (d1 <= d2)
            {
                for (int i = d1 + 1; i <= d2 + 1; i++)
                {
                    Console.WriteLine(i);
                }
            }
            else
            {
                for (int i = d2 + 1; i <= d1 + 1; i++)
                {
                    Console.WriteLine(i);
                }
            }

            Console.ReadKey();
        }
    }
}