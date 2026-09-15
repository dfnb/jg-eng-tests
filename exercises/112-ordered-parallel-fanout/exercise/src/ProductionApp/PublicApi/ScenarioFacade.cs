using ProductionApp.Application.Policies;
namespace ProductionApp;
public static class ScenarioFacade
{
    public static string Execute(string input)
    {
        ArgumentNullException.ThrowIfNull(input);
        return ScenarioPolicy.Evaluate(input);
    }
}
