using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace thing
{
    class Program
    {
        static void Main(string[] args)
        {
            int input = Convert.ToInt32(Console.ReadLine());
            if (input % 2 == 0)
            {
                Console.WriteLine("Bob");
            }
            else
            {
                Console.WriteLine("Alice");
            }

        }
    }
}