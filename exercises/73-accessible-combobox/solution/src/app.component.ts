import { Component } from "@angular/core";
        import { evaluate } from "./challenge";

        @Component({selector: "app-root", standalone: true, template: `<main><h1>Laboratório</h1><label for="case">Entrada</label><input id="case" #value (input)="output=evaluate(value.value)"><output aria-live="polite">{{output}}</output></main>`})
        export class AppComponent { output=""; evaluate=evaluate; }
