do
{
    Console.WriteLine("Ingrese la cantidad de numeros deseada");
    int n = Convert.ToInt32(Console.ReadLine());

    int[] numeros = new int[n];

    for (int i = 0; i < numeros.Length; i++)
    {
        Console.WriteLine($"Ingrese el valor {i + 1}: ");
        numeros[i] = Convert.ToInt32(Console.ReadLine());
    }
    
    Console.WriteLine("Elija su operación: ");

    Console.WriteLine("1_Mostrar elementos del array");
    Console.WriteLine("2_Mostrar Promedio");
    Console.WriteLine("3_Suma");
    Console.WriteLine("4_Resta");
    Console.WriteLine("5_Multiplicación");
    Console.WriteLine("6_División");
    Console.WriteLine("7_Potenciación");
    Console.WriteLine("8_Ordenar numeros");
    Console.WriteLine("9_Salir");

    int opc = Convert.ToInt32(Console.ReadLine());

    switch(opc)
    {
        case 1:
            for (int i = 0; i < numeros.Length; i++)
            {
                Console.WriteLine($"{numeros[i]}");
            }

            break;
        case 2:
            for (int i = 0; i < numeros.Length; i++)
            {
                resultado += numeros[i];
            }

            arrayResultado = resultado/n;
            Console.WriteLine($"{arrayResultado}");
            break;
        case 3:
            for (int i = 0; i < numeros.Length; i++)
            {
                resultado += numeros[i];
            }
            Console.WriteLine($"el resultado de la suma es {resultado}");
            break;
        case 4:
            
            for (int i = 0; i < numeros.Length; i++)
            {
                resultado -= numeros[i];
            }
            Console.WriteLine($"el resultado de la resta es {resultado}");

            break;
        case 5:

            for (int i = 0; i < numeros.Length; i++)
            {
                resultado *= numeros[i];
            }
            Console.WriteLine($"el resultado de la multiplicación es {resultado}");

            break;
        case 6:

            for (int i = 0; i < numeros.Length; i++)
            {
                resultado /= numeros[i];
            }
            Console.WriteLine($"el resultado de la división es {resultado}");

            break;
        case 7:

            for (int i = 0; i < numeros.Length; i++)
            {
                resultado **= numeros[i];
            }
            Console.WriteLine($"el resultado de la potenciación es {resultado}");

            break;
        case 8:

            for (int i = 0; i < numeros.Length; i++)
            {
                Console.WriteLine($"{numeros[i].sort()}")
            }
            break;
        case 9:
            break;
    }
} while (true);