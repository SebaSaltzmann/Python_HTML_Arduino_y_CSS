Console.WriteLine("Ingrese una estación del año");
string estaciones = Console.ReadLine();

switch(estaciones)
{
    case verano:
        Console.WriteLine("Verano: Del 21 de diciembre al 20 de marzo");
        break;
    case otoño:
        Console.WriteLine("Otoño: Del 21 de marzo al 20 de junio");
        break;
    case invierno:
        Console.WriteLine("Invierno: Del 21 de junio al 20 de septiembre");
        break;
    case primavera:
        Console.WriteLine("Primavera: Del 21 de septiembre al 20 de diciembre");
        break;
}