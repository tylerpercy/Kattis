using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication9
{
    class Program
    {
        private static List<string> list = new List<string>();
        private static List<Int32> uniquePerTrip = new List<Int32>();

        static void Main(string[] args)
        {
            var trips = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < trips; i++)
            {
                var numberOfCities = Convert.ToInt32(Console.ReadLine());
                

                for (int j = 0; j < numberOfCities; j++)
                {
                    string cities = Console.ReadLine().ToLower();
                    list.Add(cities);
                }

                var uniqueCities = new HashSet<string>(list);
                int unique = uniqueCities.Count();
                uniquePerTrip.Add(unique);
                list.Clear();

            }

            foreach (int number in uniquePerTrip)
            {
                Console.WriteLine(number);
            }

            Console.ReadKey();
            
        }
    }
}
