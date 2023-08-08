"use strict";
let username = 'Kyle';
console.log(username);
let a = 3;
let b = 6;
// TypeScript does not like dividing different types.
// JavaScript has dynamic types so it allows number to divide string
// Valid JS does not mean good TS
// change noEmitError to true in tsconfig.json if there is a problem compiling in TS and there is no JS error
// or just type tsc --noEmitOnError -w
console.log(a / b);
