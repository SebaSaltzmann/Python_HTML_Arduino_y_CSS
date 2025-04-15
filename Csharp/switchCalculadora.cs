Console.WriteLine("Ingrese la cantidad de numeros a calcular");
int n = Convert.ToInt32(Console.ReadLine());

int[] numeros = new int[n];

for (i = 0; i < numeros.Length; i++)
{
    Console.WriteLine($"Ingrese el valor {i + 1}: ");
    numeros[i] = Convert.ToInt32(Console.ReadLine());
}

Console.WriteLine("Elija su operación: ");
Console.WriteLine("1_Suma");
Console.WriteLine("2_Resta");
Console.WriteLine("3_Multiplicación");
Console.WriteLine("4_División");
Console.WriteLine("5_Potenciación");

int opc = Convert.ToInt32(Console.ReadLine());

switch(opc)
{
    case 1:
        for (i = 0; i < numeros.Length; i++)
        {
            resultado += numeros[i]
        }
        Console.WriteLine("el resultado de la suma es {resultado}")
        break;
    case 2:
        {
            Console.WriteLine($"Ingrese el valor {i + 1}: ");
            numeros[i] = Convert.ToInt32(Console.ReadLine());
        }

        break;
}
