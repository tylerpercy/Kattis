using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication9
{
    class Program
    {
        static List<Double> costs = new List<Double>();
        static double total;

        static void Main(string[] args)
        {
            var cost = Convert.ToDouble(Console.ReadLine());
            var lawns = Convert.ToDouble(Console.ReadLine());

            for (int i = 0; i < lawns; i++)
            {
                string[] input = Console.ReadLine().Split(' ');
                var width = Convert.ToDouble(input[0]);
                var length = Convert.ToDouble(input[1]);

                var area = length * width;
                costs.Add(area);
                
            }

            foreach (double lawn in costs)
            {                
                total += lawn;
            }

            total = total * cost;
            Console.WriteLine(total);
            Console.ReadKey();

            
        }
    }
}