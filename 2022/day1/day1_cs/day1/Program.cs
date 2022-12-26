class Day1
{
    static void Main(string[] args)
    {
        string input_lines = File.ReadAllText("day1_input.txt");

        var calorieBatches = input_lines.Split("\n\n").ToList();
        var sumsList = new List<int>();

        foreach (var batch in calorieBatches)
        {
            sumsList.Add(batch.Split("\n").ToList().ConvertAll(int.Parse).Sum());
        }

        // part 1
        Console.WriteLine(GetMaxSumOfCalories(sumsList, 1));

        // part 2
        Console.WriteLine(GetMaxSumOfCalories(sumsList, 3));
    }

    private static int GetMaxSumOfCalories(List<int> calorieSumsList, int nTopOfElves)
    {
        calorieSumsList.Sort();
        calorieSumsList.Reverse();

        return calorieSumsList.GetRange(0, nTopOfElves).Sum();
    }
}