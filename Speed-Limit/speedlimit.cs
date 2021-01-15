using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace speedlimit
{
    class Program
    {
        static void Main(string[] args)
        {
            String input = Console.ReadLine();
            List<String> output = new List<string>();
            while (!input.Equals("-1"))
            {
                int numOfEntries = Int32.Parse(input);
                int numOfMiles = 0;
                int numOfHours = 0;
                for (int i = 0; i < numOfEntries; i++)
                {
                    int[] entry = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
                    numOfMiles = numOfMiles + entry[0] * (entry[1] - numOfHours);
                    numOfHours = entry[1];
                }

                    output.Add(numOfMiles + " miles");
                    input = Console.ReadLine();
            }
                output.ForEach(i => Console.WriteLine(i));
        }
    }
}
