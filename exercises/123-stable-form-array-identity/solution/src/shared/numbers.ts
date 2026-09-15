export function normalize4(value: string): string { return value.trim().normalize("NFC") }
export function present4(value: string | null | undefined): boolean { return Boolean(value?.trim()) }
export function unique4(values: readonly string[]): readonly string[] { return [...new Set(values)] }
export function ordered4(values: readonly string[]): readonly string[] { return [...values].sort((a, b) => a.localeCompare(b)) }
export function partition4(values: readonly string[], predicate: (value: string) => boolean): readonly [readonly string[], readonly string[]] {
  const yes: string[] = []
  const no: string[] = []
  for (const value of values) (predicate(value) ? yes : no).push(value)
  return [yes, no]
}
export function safeRecord4(entries: readonly (readonly [string, string])[]): Readonly<Record<string, string>> { return Object.fromEntries(entries) }
export function clamp4(value: number, minimum: number, maximum: number): number { return Math.min(maximum, Math.max(minimum, value)) }
export const moduleVersion4 = "1.0.0"
