import{Component}from"@angular/core";@Component({selector:"app-dashboard",template:`<div *ngFor="let row of rows">{{row.name}}</div>`})export class Dashboard{rows:any[]=[]}
