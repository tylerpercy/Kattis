using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    class Program
    {
        private static string[] input;
        private static double firstNumber;
        private static double secondNumber;
        private static List<string> list = new List<string>();

        static void Main(string[] args)
        {
            do
            {                        
            input = Console.ReadLine().Split(' '); 

            firstNumber = Convert.ToDouble(input[0]);
            secondNumber = Convert.ToDouble(input[1]);

            var whole = Math.Floor(firstNumber / secondNumber);
            var remainder = (firstNumber % secondNumber);

            if (firstNumber != 0 && secondNumber != 0)
            { list.Add($"{whole} {remainder} / {secondNumber}"); }
            else
            {
                break;
            }        
            
            } while (firstNumber != 0 && secondNumber != 0);

            foreach (string item in list)
            {
                Console.WriteLine(item);
            }

            Console.ReadKey();
        }
    }
}