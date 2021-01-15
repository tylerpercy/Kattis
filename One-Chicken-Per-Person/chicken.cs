using System;

namespace Skener
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            string[] s = Console.ReadLine().Split(' ');
            
            int difference = int.Parse(s[1]) - int.Parse(s[0]);

            if (difference > 1) Console.WriteLine($"Dr. Chaz will have {difference} pieces of chicken left over!");
            else if (difference == 1) Console.WriteLine($"Dr. Chaz will have {difference} piece of chicken left over!");
            else if (difference == -1) Console.WriteLine($"Dr. Chaz needs {Math.Abs(difference)} more piece of chicken!");
            else Console.WriteLine($"Dr. Chaz needs {Math.Abs(difference)} more pieces of chicken!");
        }                    
    }
}