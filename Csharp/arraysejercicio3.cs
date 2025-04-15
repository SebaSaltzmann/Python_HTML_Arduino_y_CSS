int Cantidad;

double contador = 0;
Console.WriteLine("ingrese la cantidad de productos");
cantidad = Convert.ToInt32(Console.ReadLine());
string[] producto = new string[Cantidad];
double[] precio = new double[Cantidad];

for (int i = 0; i < precio.Length; i++)
{
    Console.WriteLine($"ingrese el nombre y el precio del producto N°{i+1}");
    producto[i] = Console.ReadLine();
    precio[i] = Convert.ToDouble(Console.ReadLine());
    contador = contador + precio[i];
}

Console.WriteLine("El total es ", + contador);
Console.ReadKey();