Console.WriteLine("Elija una opción");
Console.WriteLine("1_Hora y Fecha");
Console.WriteLine("2_Día de la semana");
int opc = Convert.ToInt32(Console.ReadLine());
switch(opc)
{
    case 1:
        DateTime fechaYhora = DateTime.UtcNow;
        Console.WriteLine($"la fecha y la hora es {fechaYhora}");
        break;
    case 2:
        DateTime Fecha = DateTime.Today;
        Console.WriteLine($"La fecha de hoy es{Fecha}");
        break;
}