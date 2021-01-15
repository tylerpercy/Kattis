using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(' '); 

            var h = Convert.ToDouble(input[0]);
            var v = Convert.ToDouble(input[1]);

            var answer = Math.Ceiling(h / Math.Sin(v * (Math.PI / 180)));

            Console.WriteLine(answer);

            Console.ReadKey();

        }
    }
}