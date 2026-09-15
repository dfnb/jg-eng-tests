FROM mcr.microsoft.com/dotnet/sdk:10.0.100 AS build
WORKDIR /src
COPY App.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /out --no-restore
FROM mcr.microsoft.com/dotnet/aspnet:10.0.0
WORKDIR /app
COPY --from=build /out .
USER 1654
ENTRYPOINT ["dotnet","App.dll"]
