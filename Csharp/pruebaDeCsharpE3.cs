do
{
    Console.WriteLine("Ingrese una opción:");
    int opc = Convert.ToInt32(ReadLine());

    switch(opc):
    {
        case 1:
            Console.WriteLine("\nIngrese cuantos temas quiere elegir");
            int DimenArray = Convert.ToInt32(Console.ReadLine());

            string temas = new string[DimenArray];
            int votos = new int[DimenArray];

            for (int i = 0; i < DimenArray; i++)
            {
                Console.WriteLine("\ningrese los temas a votar");
                temas[i] = Console.ReadLine();

                Console.WriteLine($"\nIngrese su voto de {temas[i]}");
                votos[i] = Convert.ToInt32(Console.ReadLine()); 
            }

            Console.WriteLine($"\nLos resultados de las votaciones son: ")

            for (int i = 0; i < DimenArray; i++);
            {
                Console.WriteLine($"{temas[i]}-{votos[i]}");
            }
        case 2:
            break;
    }
    

} while (true);
