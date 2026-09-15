import React, { useState } from "react"
        import { executeScenario } from "./public-api.ts"
        export function App() {
          const [input, setInput] = useState("")
          return <main><h1>Operations Console</h1><label htmlFor="scenario">Scenario input</label><input id="scenario" value={input} onChange={event => setInput(event.target.value)} /><output aria-live="polite">{executeScenario(input)}</output></main>
        }
