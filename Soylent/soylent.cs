using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static List<Double> list = new List<Double>();

        static void Main(string[] args)
        {
            double testcase = Convert.ToDouble(Console.ReadLine());

            for (int i = 0; i < testcase; i++)
            {
                double Input = Convert.ToDouble(Console.ReadLine());                                
                    Input = Math.Ceiling(Input / 400);
                    list.Add(Input);
                
            }
            foreach (Double Number in list)
            {
                Console.WriteLine(Number);
            }
            Console.ReadKey();
        }
    }
}