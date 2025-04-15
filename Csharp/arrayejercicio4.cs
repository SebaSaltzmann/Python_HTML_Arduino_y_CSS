int dimenArray = Convert.ToInt32(Console.ReadLine());

int[] notas = new int[dimenArray];
string[] estudiantes = new string[dimenArray];
string[] practicas = new string[dimenArray]

for (int i = 0; i < estudiantes.Length; i++)
{
    Console.WriteLine($"ingrese el nombre del estudiante {i + 1}");
    estudiantes[i] = Console.ReadLine();

    Console.WriteLine("Ingrese la materia");
    practicas[i] = Console.ReadLine();

    Console.WriteLine("Ingrese su nota final");
    notas[i] = Convert.ToInt32(Console.ReadLine());
}

Console.WriteLine("los estudiantes, sus notas y materias guardados son:");

for (int i = 0; i < estudiantes.Length; i++)
{
    Console.WriteLine($"{estudiantes[i]} - {practica[i]} - {notas[i]}");
}
