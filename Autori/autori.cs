using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication12
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] names = Console.ReadLine().Split('-');

            foreach (string name in names)
            {              
                Console.Write(name[0]);
            }

            Console.ReadKey();
        }
    }
}