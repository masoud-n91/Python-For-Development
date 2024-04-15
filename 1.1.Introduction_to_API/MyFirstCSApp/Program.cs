using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        Console.WriteLine("Enter a number:");
        string numberInput = Console.ReadLine();

        if (!int.TryParse(numberInput, out int number))
        {
            Console.WriteLine("Invalid input. Please enter a valid integer.");
            return;
        }

        Console.WriteLine("Enter a fruit:");
        string fruit = Console.ReadLine(); // No need to parse as integer

        var client = new HttpClient();

        // Numbers API call
        var request = new HttpRequestMessage(HttpMethod.Get, $"http://numbersapi.com/{number}");
        var response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();
        Console.WriteLine(await response.Content.ReadAsStringAsync());

        // Fruityvice API call
        request = new HttpRequestMessage(HttpMethod.Get, $"https://www.fruityvice.com/api/fruit/{fruit}");
        response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();
        Console.WriteLine(await response.Content.ReadAsStringAsync());

        // Harry Potter API call
        request = new HttpRequestMessage(HttpMethod.Get, $"https://hp-api.onrender.com/api/spells");
        response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();
        Console.WriteLine(await response.Content.ReadAsStringAsync());

        // Advice Slip API call
        request = new HttpRequestMessage(HttpMethod.Get, $"https://api.adviceslip.com/advice");
        response = await client.SendAsync(request);
        response.EnsureSuccessStatusCode();
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
