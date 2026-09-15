import React, { useState } from "react";
        import { evaluate } from "./challenge";

        export function App() {
          const [input, setInput] = useState("");
          return <main><h1>Laboratório</h1><label htmlFor="case">Entrada</label><input id="case" value={input} onChange={e => setInput(e.target.value)} /><output aria-live="polite">{evaluate(input)}</output></main>;
        }
