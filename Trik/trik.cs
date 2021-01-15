using System;

namespace trik
{
    class Program
    {
        public static void Main(string[] args)
        {
            int position = 1;
            string moves = Console.ReadLine();

            for (int i = 0; i < moves.Length; i++)
            {
                switch (moves[i])
                {
                    case 'A':   //swap 1-2
                        if (position == 1)
                            position = 2;
                        else if (position == 2)
                            position = 1;
                        break;
                    case 'B':   //swap 2-3
                        if (position == 2)
                            position = 3;
                        else if (position == 3)
                            position = 2;
                        break;
                    case 'C':   //swap 1-3
                        if (position == 1)
                            position = 3;
                        else if (position == 3)
                            position = 1;
                        break;
                }
            }
            Console.WriteLine(position);
        }
    }
}