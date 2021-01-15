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
            var input = Console.ReadLine();           
            var array = input.Split(' ');
       
            var x = Convert.ToInt32(array[0]);
            var y = Convert.ToInt32(array[1]);
            var n = Convert.ToInt32(array[2]);

            for (int i = 1; i <= n; i++)
            {
                if (i % x == 0 && i % y != 0)
                {
                    Console.WriteLine("Fizz");
                }
                else if (i % y == 0 && i % x != 0)
                {
                    Console.WriteLine("Buzz");
                }
                else if (i % x == 0 & i % y == 0)
                {
                    Console.WriteLine("FizzBuzz");
                }
                else
                {
                    Console.WriteLine(i);
                }
            }

            Console.ReadKey();

        }
    }
}
