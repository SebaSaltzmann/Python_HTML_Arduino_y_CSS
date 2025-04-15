int[] edad = new int[5];
string[] nombre = new string[5];
string[] apellido = new string[5];
char[] sexo = new char[5];

for (int i = 0; i < nombre.Length; i++)
{
    Console.WriteLine($"\ningrese el nombre {i + 1}");
    nombre[i] = Console.ReadLine();

    Console.WriteLine($"ingrese el apellido {i + 1}");
    apellido[i] = Console.ReadLine();

    Console.WriteLine($"Ingrese su edad {i + 1}");
    edad[i] = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine($"Ingrese su sexo (M/F)");
    sexo[i] = Convert.ToChart(Console.ReadLine());
}
Console.WriteLine("Los datos son:");

for (int i = 0; i < 5; i++)
{
    Console.WriteLine($"{nombre[i]}-{apellido[i]}-{edad[i]}-{sexo[i]}");
}