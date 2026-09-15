import { Component } from "@angular/core"
        import { executeScenario } from "./public-api.ts"
        @Component({ selector: "app-root", standalone: true, template: `<main><h1>Operations Console</h1><label for="scenario">Scenario input</label><input id="scenario" #field (input)="output=execute(field.value)"><output aria-live="polite">{{output}}</output></main>` })
        export class AppComponent { output = ""; execute = executeScenario }
