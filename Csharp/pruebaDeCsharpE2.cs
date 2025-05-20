Console.WriteLine("ingrese el tamaño de los arrays");
int n = Convert.ToInt32(ReadLine());

string[] dias = new string[n];
string[] nombre = new string[n];
string[] asistencia = new string[n];

for (int i = 0; i < nombre.Length; i++)
{
    Console.WriteLine($"\ningrese el nombre {i + 1}");
    nombre[i] = Console.ReadLine();

    Console.WriteLine($"ingrese la asistencia {i + 1}");
    asistencia[i] = Console.ReadLine();

    Console.WriteLine($"Ingrese el dia {i + 1}");
    dias[i] = Console.ReadLine();

}
Console.WriteLine("Los datos son:");

for (int i = 0; i < 5; i++)
{
    Console.WriteLine($"{nombre[i]}-{asistencia[i]}-{dia[i]}");
}