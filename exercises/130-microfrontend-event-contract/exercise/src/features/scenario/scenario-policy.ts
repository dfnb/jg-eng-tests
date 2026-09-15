export function evaluateScenario(input: string): string { const[topic]=input.split("|");return topic.startsWith("commerce.")?"accept":"foreign" }
