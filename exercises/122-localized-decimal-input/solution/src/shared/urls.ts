export function normalize5(value: string): string { return value.trim().normalize("NFC") }
export function present5(value: string | null | undefined): boolean { return Boolean(value?.trim()) }
export function unique5(values: readonly string[]): readonly string[] { return [...new Set(values)] }
export function ordered5(values: readonly string[]): readonly string[] { return [...values].sort((a, b) => a.localeCompare(b)) }
export function partition5(values: readonly string[], predicate: (value: string) => boolean): readonly [readonly string[], readonly string[]] {
  const yes: string[] = []
  const no: string[] = []
  for (const value of values) (predicate(value) ? yes : no).push(value)
  return [yes, no]
}
export function safeRecord5(entries: readonly (readonly [string, string])[]): Readonly<Record<string, string>> { return Object.fromEntries(entries) }
export function clamp5(value: number, minimum: number, maximum: number): number { return Math.min(maximum, Math.max(minimum, value)) }
export const moduleVersion5 = "1.0.0"
