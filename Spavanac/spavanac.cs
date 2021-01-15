using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            
            string[] time = Console.ReadLine().Split(' ');

            int h = Convert.ToInt32(time[0]);
            int m = Convert.ToInt32(time[1]);

            m += 15;

            if (m / 60 == 0)
            {
                h--;
            }
            else
            {
                m = m % 60;
            }

            if (h < 0)
            {
                h += 24;
            }

            Console.WriteLine("{0} {1}", h, m);
            Console.ReadKey();


        }
    }
}
