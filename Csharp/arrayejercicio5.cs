int dimenArray = Convert.ToInt32(Console.ReadLine());

double[] parcial = new double[dimenArray];
double[] oral = new double[dimenArray];
double[] final = new double[dimenArray];
double[] Promedio = new double[dimenArray];

for (int i = 0; i < dimenArray; i++)
{
    Console.WriteLine($"ingrese la nota parcial {i + 1}");
    parcial[i] = Console.ReadLine();

    Console.WriteLine($"Ingrese la nota oral {i + 1}");
    oral[i] = Console.ReadLine();

    Console.WriteLine($"Ingrese su nota final {i + 1}");
    final[i] = Convert.ToInt32(Console.ReadLine());

    Promedio[i] = (parcial[i]+oral[i]+final[i])/3;
}

for (int i = 0; i < dimenArray; i++)
{
    if (Promedio[i] >= 13)
    {
        Console.WriteLine("Aprobado");
    }
    else
    {
        Console.WriteLine("Desaprobado");
    }
}




