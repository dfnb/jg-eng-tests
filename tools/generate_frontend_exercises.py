#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from textwrap import dedent

ROOT=Path(__file__).resolve().parents[1]
CAT={x["id"]:x for x in json.loads((ROOT/"catalog.json").read_text())["exercises"]}
def clean(x):return dedent(x).strip()+"\n"
def write(p,x,exe=False):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(clean(x));p.chmod(0o755 if exe else 0o644)
RUN=r'''#!/usr/bin/env python3
import json,os,re,subprocess,sys
from pathlib import Path
here=Path(__file__).resolve().parent;target=Path(sys.argv[1] if len(sys.argv)>1 else here.parent/"exercise").resolve();spec=json.loads((here/"criteria.json").read_text());env={**os.environ,"CHALLENGE_TARGET":target.as_uri()};statuses={};diag=[]
try:
 r=subprocess.run(["node",str(here/"hidden.test.ts")],capture_output=True,text=True,env=env,timeout=90)
 diag.extend([r.stderr[-2000:]] if r.stderr else [])
 for line in r.stdout.splitlines():
  m=re.search(r"(C\d\d)\|(pass|fail)(?:\|(.*))?",line)
  if m:statuses[m.group(1)]=m.group(2)
except (FileNotFoundError,subprocess.TimeoutExpired) as e:diag.append(str(e))
source="\n".join(p.read_text(errors="ignore") for p in (target/"src").rglob("*") if p.is_file())
for c in spec.get("staticChecks",[]):
 ok=not re.search(c["forbid"],source,re.M) if "forbid" in c else True
 if "require" in c:ok=ok and re.search(c["require"],source,re.M) is not None
 statuses[c["id"]]="pass" if ok else "fail"
items=[]
for c in spec["criteria"]:
 s=statuses.get(c["id"],"fail");items.append({**c,"status":s,"points":c["weight"] if s=="pass" else 0})
score=sum(x["points"] for x in items);maximum=sum(x["weight"] for x in items);minimum=all(x["status"]=="pass" for x in items if x["level"]=="minimum")
out={"exercise":spec["exercise"],"criteria":items,"score":score,"maximum":maximum,"minimumPassed":minimum and score*100>=maximum*60,"diagnostics":diag};print(json.dumps(out,ensure_ascii=False));raise SystemExit(0 if out["minimumPassed"] else 1)
'''
def make(c):
 i=CAT[c["id"]];name=f"{i['id']}-{i['slug']}";root=ROOT/"exercises"/name
 deps={"react":"19.3.0","react-dom":"19.3.0"} if "react" in i["stack"] else {"@angular/core":"22.1.6","@angular/forms":"22.1.6","rxjs":"7.8.2"}
 pkg={"name":name,"private":True,"version":"1.0.0","type":"module","scripts":{"test":"node tests/public.test.ts","lint":"node --check src/challenge.ts"},"dependencies":deps,"devDependencies":{"typescript":"7.0.2"}}
 setup='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
npm ci --ignore-scripts
'''
 test='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
npm test
'''
 lint='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
npm run lint
'''
 start='''#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
node --watch tests/public.test.ts
'''
 readme=f'''# {i['title']}

Este repositório simula {c['context']}

## Stack

    {', '.join(i['stack'])}, Node.js 24.15.0 (fixado em `.node-version`). A lógica testável está em `src/challenge.ts`; o componente do framework está ao lado dela.

## Executar

```bash
./scripts/setup.sh
./scripts/test.sh
./scripts/lint.sh
```

Os testes públicos cobrem apenas o ambiente e o caminho básico. Preserve as exportações existentes.
'''
 challenge=f'''# Desafio: {i['title']}

## Situação

{c['situation']}

## Resultado esperado

{c['expected']}

## Restrições

Preserve as exportações públicas, TypeScript estrito e o framework já escolhido. Não codifique respostas específicas para os fixtures públicos.

## Fora de escopo

Backend real, autenticação e deploy não fazem parte da tarefa. A API simulada já está pronta.

## Verificação

Execute `./scripts/test.sh` e `./scripts/lint.sh` e entregue testes de regressão relevantes.
'''
 rows="\n".join(f"| {x[0]} | {x[1]} | {x[2]} | {x[3]} | `{x[0]}` |" for x in c["criteria"])
 evaluation=f'''# Avaliação: {i['title']}

- **ID:** {i['id']}
- **Nível:** {i['level']}
- **Duração:** {i['minutes']} minutos
- **Tecnologias:** {', '.join(i['stack'])}

## Intenção e estado inicial

{c['intent']}

**Causa/omissão:** {c['cause']}

**Armadilha:** {c['trap']}

## Critérios

| ID | Nível | Peso | Condição | Teste |
| --- | --- | ---: | --- | --- |
{rows}

Soluções estruturalmente diferentes são aceitas se preservarem o contrato observável e a acessibilidade. A referência é um exemplo, não um molde obrigatório.
'''
 for variant,code,component in (("exercise",c["broken"],c["componentBroken"]),("solution",c["solution"],c["componentSolution"])):
  b=root/variant;write(b/"package.json",json.dumps(pkg,ensure_ascii=False,indent=2));write(b/".node-version","24.15.0");write(b/".gitignore","node_modules/\ndist/\n.coverage/\n");write(b/"src/challenge.ts",code);write(b/c["componentPath"],component);write(b/"src/styles.css",c.get("css","body{font-family:system-ui;margin:0} button,input{font:inherit}"));write(b/"tests/public.test.ts",c["public"]);write(b/"scripts/setup.sh",setup,True);write(b/"scripts/start.sh",start,True);write(b/"scripts/test.sh",test,True);write(b/"scripts/lint.sh",lint,True);write(b/"README.md",readme);write(b/"CHALLENGE.md",challenge)
  if variant=="solution":write(b/"SOLUTION_NOTES.md","# Notas da solução\n\n"+c["notes"])
 write(root/"EVALUATION.md",evaluation);write(root/"grader/run.py",RUN,True);write(root/"grader/hidden.test.ts",c["hidden"])
 levels={"mínimo":"minimum","intermediário":"intermediate","desejado":"desired"};spec={"exercise":name,"criteria":[{"id":x[0],"level":levels[x[1]],"weight":x[2],"description":x[3]} for x in c["criteria"]],"staticChecks":c.get("static",[])};write(root/"grader/criteria.json",json.dumps(spec,ensure_ascii=False,indent=2))

CASES=[
{"id":"07","context":"o checkout web da loja Northstar, com API simulada e especificação responsiva.","situation":"Complete validação, payload e estados acessíveis de uma tela de checkout. Nome, endereço e método de pagamento são obrigatórios.","expected":"`validateCheckout` produz erros por campo; `buildOrder` normaliza texto sem descartar o método; o componente associa labels/erros, bloqueia duplo envio e anuncia status.","intent":"Avaliar implementação de interface React além do caminho visual feliz.","cause":"validação aceita espaços, payload omite pagamento e componente não tem labels/status.","trap":"fazer apenas screenshot desktop e ignorar teclado, erro e loading.","notes":"A referência mantém regras puras testáveis e usa labels, aria-live e disabled no componente.","criteria":[("C01","mínimo",3,"campos vazios ou só com espaços são rejeitados"),("C02","mínimo",2,"payload normalizado inclui pagamento"),("C03","mínimo",2,"controles possuem labels associados"),("C04","intermediário",2,"status é anunciado e submit é bloqueado durante envio"),("C05","desejado",1,"CSS inclui adaptação móvel")],"broken":'''export type Checkout={name:string,address:string,payment:string};export function validateCheckout(x:Checkout){return {} as Record<string,string>}export function buildOrder(x:Checkout){return {customerName:x.name,address:x.address}}''',"solution":'''export type Checkout={name:string,address:string,payment:string};export function validateCheckout(x:Checkout){const e:Record<string,string>={};if(!x.name.trim())e.name="required";if(!x.address.trim())e.address="required";if(!x.payment.trim())e.payment="required";return e}export function buildOrder(x:Checkout){return {customerName:x.name.trim(),address:x.address.trim(),paymentMethod:x.payment}}''',"componentPath":"src/Checkout.tsx","componentBroken":'''import React from "react";export function Checkout(){return <form><input name="name"/><input name="address"/><button>Buy</button></form>}''',"componentSolution":'''import React,{useState} from "react";export function Checkout(){const[busy,setBusy]=useState(false);return <form onSubmit={()=>setBusy(true)}><label htmlFor="name">Name</label><input id="name" name="name"/><label htmlFor="address">Address</label><input id="address" name="address"/><label htmlFor="payment">Payment</label><select id="payment" name="payment"><option>card</option></select><button disabled={busy}>Buy</button><p aria-live="polite">{busy?"Sending":""}</p></form>}''',"css":'''body{font-family:system-ui;margin:0}.checkout{display:grid;grid-template-columns:2fr 1fr}@media(max-width:640px){.checkout{grid-template-columns:1fr}}''',"public":'''import test from"node:test";import assert from"node:assert/strict";import{validateCheckout}from"../src/challenge.ts";test("valid",()=>assert.deepEqual(validateCheckout({name:"A",address:"B",payment:"card"}),{}));''',"hidden":'''import test from"node:test";import assert from"node:assert/strict";const m=await import(process.env.CHALLENGE_TARGET+"/src/challenge.ts");function c(id,f){test(id,()=>{try{f();console.log(id+"|pass")}catch(e){console.log(id+"|fail|"+e.message);throw e}})}c("C01",()=>assert.deepEqual(Object.keys(m.validateCheckout({name:" ",address:"",payment:" "})).sort(),["address","name","payment"]));c("C02",()=>assert.deepEqual(m.buildOrder({name:" A ",address:" B ",payment:"pix"}),{customerName:"A",address:"B",paymentMethod:"pix"}));''',"static":[{"id":"C03","require":"<label[^>]+htmlFor="},{"id":"C04","require":"(?s)(?=.*aria-live)(?=.*disabled=)"},{"id":"C05","require":"@media"}]},
{"id":"08","context":"a busca incremental React cujo transporte simula respostas com latências diferentes.","situation":"Uma resposta antiga substitui a consulta mais recente. Implemente um controlador que publique somente o resultado da geração atual e ignore tudo após dispose.","expected":"`SearchController.search` aceita uma função assíncrona; limpar termo publica lista vazia e não chama o transporte.","intent":"Avaliar race condition no cliente e ciclo de vida assíncrono.","cause":"toda promessa atualiza o estado quando termina.","trap":"aumentar debounce sem garantir ordem.","notes":"A referência incrementa uma geração por busca/dispose e compara antes de publicar.","criteria":[("C01","mínimo",3,"só a busca mais recente publica"),("C02","mínimo",2,"termo vazio limpa sem chamar API"),("C03","mínimo",2,"dispose impede publicação tardia"),("C04","intermediário",2,"erro obsoleto não apaga resultado novo"),("C05","desejado",1,"componente limpa controller ao desmontar")],"broken":'''export class SearchController{publish:(x:string[])=>void;constructor(publish:(x:string[])=>void){this.publish=publish}async search(term:string,fetcher:(x:string)=>Promise<string[]>){this.publish(await fetcher(term))}dispose(){}}''',"solution":'''export class SearchController{private generation=0;private disposed=false;publish:(x:string[])=>void;constructor(publish:(x:string[])=>void){this.publish=publish}async search(term:string,fetcher:(x:string)=>Promise<string[]>){const g=++this.generation;if(!term.trim()){if(!this.disposed)this.publish([]);return}try{const r=await fetcher(term);if(!this.disposed&&g===this.generation)this.publish(r)}catch(e){if(g===this.generation&&!this.disposed)throw e}}dispose(){this.disposed=true;this.generation++}}''',"componentPath":"src/Search.tsx","componentBroken":'''import React from"react";export function Search(){return <input placeholder="Search"/>}''',"componentSolution":'''import React,{useEffect,useRef}from"react";import{SearchController}from"./challenge";export function Search(){const c=useRef(new SearchController(()=>{}));useEffect(()=>()=>c.current.dispose(),[]);return <label>Search<input type="search"/></label>}''',"public":'''import test from"node:test";import assert from"node:assert/strict";import{SearchController}from"../src/challenge.ts";test("one",async()=>{let x=[];await new SearchController(v=>x=v).search("a",async()=>["a"]);assert.deepEqual(x,["a"])});''',"hidden":'''import test from"node:test";import assert from"node:assert/strict";const{SearchController}=await import(process.env.CHALLENGE_TARGET+"/src/challenge.ts");const wait=()=>new Promise(r=>setImmediate(r));function c(id,f){test(id,async()=>{try{await f();console.log(id+"|pass")}catch(e){console.log(id+"|fail");throw e}})}c("C01",async()=>{let release;const out=[];const s=new SearchController(x=>out.push(x));const a=s.search("a",()=>new Promise(r=>release=r));await s.search("b",async()=>["b"]);release(["a"]);await a;assert.deepEqual(out,[["b"]])});c("C02",async()=>{let n=0,o;await new SearchController(x=>o=x).search(" ",async()=>{n++;return[]});assert.equal(n,0);assert.deepEqual(o,[])});c("C03",async()=>{let r,n=0;const s=new SearchController(()=>n++);const p=s.search("a",()=>new Promise(x=>r=x));s.dispose();r(["a"]);await p;assert.equal(n,0)});c("C04",async()=>{let reject;const out=[];const s=new SearchController(x=>out.push(x));const old=s.search("a",()=>new Promise((_,x)=>reject=x));await s.search("b",async()=>["b"]);reject(new Error());await old;assert.deepEqual(out,[["b"]])});''',"static":[{"id":"C05","require":"dispose\\(\\)"}]},
{"id":"09","context":"um dashboard Angular com milhares de linhas e uma viewport virtual simulada.","situation":"`visibleRows` hoje ordena/mapeia todo o conjunto antes de filtrar e ignora a janela. Retorne somente a fatia visível depois do filtro e uma ordenação estável sem mutar a entrada.","expected":"Respeite `start` e `size`, preserve seleção por ID e não execute o formatador em linhas fora da janela.","intent":"Avaliar performance frontend por trabalho observável, não por milissegundos frágeis.","cause":"a função formata toda a lista e retorna tudo.","trap":"esconder linhas com CSS ou ordenar mutando o array original.","notes":"A referência filtra, copia/ordena, fatia e só então formata.","criteria":[("C01","mínimo",3,"janela contém somente size linhas"),("C02","mínimo",2,"filtro e ordenação são corretos"),("C03","mínimo",2,"entrada não é mutada"),("C04","intermediário",2,"formatador roda apenas na janela"),("C05","desejado",1,"trackBy usa ID")],"broken":'''export type Row={id:string,name:string,value:number};export function visibleRows(rows:Row[],filter:string,start:number,size:number,format:(x:Row)=>Row){return rows.sort((a,b)=>a.name.localeCompare(b.name)).map(format).filter(x=>x.name.includes(filter))}''',"solution":'''export type Row={id:string,name:string,value:number};export function visibleRows(rows:Row[],filter:string,start:number,size:number,format:(x:Row)=>Row){return rows.filter(x=>x.name.toLowerCase().includes(filter.toLowerCase())).toSorted((a,b)=>a.name.localeCompare(b.name)||a.id.localeCompare(b.id)).slice(start,start+size).map(format)}''',"componentPath":"src/dashboard.component.ts","componentBroken":'''import{Component}from"@angular/core";@Component({selector:"app-dashboard",template:`<div *ngFor="let row of rows">{{row.name}}</div>`})export class Dashboard{rows:any[]=[]}''',"componentSolution":'''import{Component}from"@angular/core";@Component({selector:"app-dashboard",template:`<div *ngFor="let row of rows;trackBy:trackById" tabindex="0">{{row.name}}</div>`})export class Dashboard{rows:any[]=[];trackById=(_:number,row:any)=>row.id}''',"public":'''import test from"node:test";import assert from"node:assert/strict";import{visibleRows}from"../src/challenge.ts";test("window",()=>assert.equal(visibleRows([{id:"1",name:"A",value:1}],"",0,1,x=>x).length,1));''',"hidden":'''import test from"node:test";import assert from"node:assert/strict";const{visibleRows}=await import(process.env.CHALLENGE_TARGET+"/src/challenge.ts");const rows=Array.from({length:100},(_,i)=>({id:String(i),name:String(999-i),value:i}));function c(id,f){test(id,()=>{try{f();console.log(id+"|pass")}catch(e){console.log(id+"|fail");throw e}})}c("C01",()=>assert.equal(visibleRows(rows,"",10,5,x=>x).length,5));c("C02",()=>assert.deepEqual(visibleRows([{id:"2",name:"b",value:0},{id:"1",name:"A",value:0}],"a",0,5,x=>x).map(x=>x.id),["1"]));c("C03",()=>{const a=[{id:"2",name:"B",value:0},{id:"1",name:"A",value:0}];visibleRows(a,"",0,2,x=>x);assert.equal(a[0].id,"2")});c("C04",()=>{let n=0;visibleRows(rows,"",20,7,x=>(n++,x));assert.equal(n,7)});''',"static":[{"id":"C05","require":"trackById"}]},
{"id":"10","context":"um formulário Angular definido por esquema recebido da API.","situation":"Converta os campos suportados (`text`, `number`, `select`) em um modelo tipado, valide obrigatoriedade/min/max e rejeite esquema desconhecido.","expected":"`buildForm` devolve valores com tipos corretos, erros por campo e `valid` global; não codifique nomes dos fixtures.","intent":"Avaliar feature dinâmica, tipos e validação orientada por dados.","cause":"a implementação cria apenas campos text e ignora regras.","trap":"hardcode dos campos do exemplo.","notes":"A referência percorre o esquema, converte valores por tipo e aplica regras genéricas.","criteria":[("C01","mínimo",3,"três tipos suportados são montados"),("C02","mínimo",2,"required controla validade"),("C03","mínimo",2,"min/max numérico é aplicado"),("C04","intermediário",2,"tipo desconhecido gera erro seguro"),("C05","desejado",1,"componente usa ReactiveFormsModule")],"broken":'''export type Field={name:string,type:string,required?:boolean,min?:number,max?:number,options?:string[]};export function buildForm(schema:Field[],input:Record<string,unknown>){const values={};for(const f of schema)if(f.type==="text")values[f.name]=String(input[f.name]??"");return{values,errors:{},valid:true}}''',"solution":'''export type Field={name:string,type:string,required?:boolean,min?:number,max?:number,options?:string[]};export function buildForm(schema:Field[],input:Record<string,unknown>){const values:Record<string,unknown>={},errors:Record<string,string>={};for(const f of schema){if(!["text","number","select"].includes(f.type))throw new Error("unsupported_field");const raw=input[f.name];const value=f.type==="number"&&raw!==""&&raw!=null?Number(raw):String(raw??"");values[f.name]=value;if(f.required&&(value===""||Number.isNaN(value)))errors[f.name]="required";else if(f.type==="number"&&((f.min!=null&&Number(value)<f.min)||(f.max!=null&&Number(value)>f.max)))errors[f.name]="range";else if(f.type==="select"&&f.options&&!f.options.includes(String(value)))errors[f.name]="option"}return{values,errors,valid:Object.keys(errors).length===0}}''',"componentPath":"src/schema-form.component.ts","componentBroken":'''import{Component}from"@angular/core";@Component({selector:"app-schema-form",template:"<form></form>"})export class SchemaForm{}''',"componentSolution":'''import{Component}from"@angular/core";import{ReactiveFormsModule}from"@angular/forms";@Component({selector:"app-schema-form",imports:[ReactiveFormsModule],template:"<form aria-label=\"Dynamic form\"></form>"})export class SchemaForm{}''',"public":'''import test from"node:test";import assert from"node:assert/strict";import{buildForm}from"../src/challenge.ts";test("text",()=>assert.equal(buildForm([{name:"x",type:"text"}],{x:"a"}).values.x,"a"));''',"hidden":'''import test from"node:test";import assert from"node:assert/strict";const{buildForm}=await import(process.env.CHALLENGE_TARGET+"/src/challenge.ts");function c(id,f){test(id,()=>{try{f();console.log(id+"|pass")}catch(e){console.log(id+"|fail");throw e}})}c("C01",()=>assert.deepEqual(buildForm([{name:"a",type:"text"},{name:"b",type:"number"},{name:"c",type:"select",options:["x"]}],{a:"z",b:"2",c:"x"}).values,{a:"z",b:2,c:"x"}));c("C02",()=>assert.equal(buildForm([{name:"x",type:"text",required:true}],{}).valid,false));c("C03",()=>assert.equal(buildForm([{name:"x",type:"number",min:2,max:4}],{x:5}).errors.x,"range"));c("C04",()=>assert.throws(()=>buildForm([{name:"x",type:"date"}],{}),/unsupported/));''',"static":[{"id":"C05","require":"ReactiveFormsModule"}]},
{"id":"11","context":"uma lista React com edição otimista e API versionada.","situation":"Aplique edição imediatamente; em falha reverta somente se nenhuma edição mais nova substituiu aquela versão. Conflito deve ser distinguido de falha comum.","expected":"`OptimisticStore.edit` retorna `ok`, `failed` ou `conflict` e mantém o estado mais recente sob mutações sobrepostas.","intent":"Avaliar estado otimista, rollback condicional e conflito de integração.","cause":"qualquer falha restaura um snapshot antigo, apagando edição posterior.","trap":"rollback cego ou tratar HTTP 409 como erro genérico.","notes":"A referência usa uma geração por item e só reverte quando a mutação ainda é a mais nova.","criteria":[("C01","mínimo",3,"valor é publicado antes da resposta"),("C02","mínimo",2,"falha simples reverte"),("C03","mínimo",2,"rollback antigo não apaga edição nova"),("C04","intermediário",2,"conflito retorna estado próprio"),("C05","desejado",1,"componente anuncia o resultado")],"broken":'''export type Item={id:string,title:string,version:number};export class OptimisticStore{items=new Map<string,Item>();constructor(items:Item[]){items.forEach(x=>this.items.set(x.id,x))}async edit(id:string,title:string,send:(x:Item)=>Promise<Item>){const old=this.items.get(id);if(!old)throw new Error("missing");const next={...old,title};this.items.set(id,next);try{this.items.set(id,await send(next));return"ok"}catch{this.items.set(id,old);return"failed"}}}''',"solution":'''export type Item={id:string,title:string,version:number};export class OptimisticStore{items=new Map<string,Item>();private gen=new Map<string,number>();constructor(items:Item[]){items.forEach(x=>this.items.set(x.id,x))}async edit(id:string,title:string,send:(x:Item)=>Promise<Item>){const old=this.items.get(id);if(!old)throw new Error("missing");const g=(this.gen.get(id)??0)+1;this.gen.set(id,g);const next={...old,title};this.items.set(id,next);try{const saved=await send(next);if(this.gen.get(id)===g)this.items.set(id,saved);return"ok"}catch(e){if(this.gen.get(id)===g)this.items.set(id,old);return e&&typeof e==="object"&&"status"in e&&e.status===409?"conflict":"failed"}}}''',"componentPath":"src/Editor.tsx","componentBroken":'''import React from"react";export function Editor(){return <button>Save</button>}''',"componentSolution":'''import React from"react";export function Editor(){return <><button>Save</button><output aria-live="polite"/></>}''',"public":'''import test from"node:test";import assert from"node:assert/strict";import{OptimisticStore}from"../src/challenge.ts";test("success",async()=>{const s=new OptimisticStore([{id:"1",title:"a",version:1}]);await s.edit("1","b",async x=>({...x,version:2}));assert.equal(s.items.get("1").title,"b")});''',"hidden":'''import test from"node:test";import assert from"node:assert/strict";const{OptimisticStore}=await import(process.env.CHALLENGE_TARGET+"/src/challenge.ts");function c(id,f){test(id,async()=>{try{await f();console.log(id+"|pass")}catch(e){console.log(id+"|fail");throw e}})}const item=()=>({id:"1",title:"a",version:1});c("C01",async()=>{let release;const s=new OptimisticStore([item()]);const p=s.edit("1","b",()=>new Promise(r=>release=r));assert.equal(s.items.get("1").title,"b");release({...item(),title:"b",version:2});await p});c("C02",async()=>{const s=new OptimisticStore([item()]);await s.edit("1","b",async()=>{throw Error()});assert.equal(s.items.get("1").title,"a")});c("C03",async()=>{let reject;const s=new OptimisticStore([item()]);const old=s.edit("1","b",()=>new Promise((_,r)=>reject=r));await s.edit("1","c",async x=>({...x,version:2}));reject(Error());await old;assert.equal(s.items.get("1").title,"c")});c("C04",async()=>{const s=new OptimisticStore([item()]);assert.equal(await s.edit("1","b",async()=>{throw{status:409}}),"conflict")});''',"static":[{"id":"C05","require":"aria-live"}]}
]
if __name__=="__main__":
 for c in CASES:make(c)
 print(f"Generated {len(CASES)} frontend exercises")
