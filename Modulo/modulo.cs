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
            bool[] values = new bool[42];
            for (int i = 0; i < 10; i++)
            {
                var input = int.Parse(Console.ReadLine());
                values[input % 42] = true;
            }
            Console.WriteLine(values.Count(b => b));
            Console.ReadKey();
        }
    }
}