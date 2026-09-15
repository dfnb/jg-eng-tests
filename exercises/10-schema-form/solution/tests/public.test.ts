import test from"node:test";import assert from"node:assert/strict";import{buildForm}from"../src/challenge.ts";test("text",()=>assert.equal(buildForm([{name:"x",type:"text"}],{x:"a"}).values.x,"a"));
