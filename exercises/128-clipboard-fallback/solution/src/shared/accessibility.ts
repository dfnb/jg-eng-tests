export function normalize8(value: string): string { return value.trim().normalize("NFC") }
export function present8(value: string | null | undefined): boolean { return Boolean(value?.trim()) }
export function unique8(values: readonly string[]): readonly string[] { return [...new Set(values)] }
export function ordered8(values: readonly string[]): readonly string[] { return [...values].sort((a, b) => a.localeCompare(b)) }
export function partition8(values: readonly string[], predicate: (value: string) => boolean): readonly [readonly string[], readonly string[]] {
  const yes: string[] = []
  const no: string[] = []
  for (const value of values) (predicate(value) ? yes : no).push(value)
  return [yes, no]
}
export function safeRecord8(entries: readonly (readonly [string, string])[]): Readonly<Record<string, string>> { return Object.fromEntries(entries) }
export function clamp8(value: number, minimum: number, maximum: number): number { return Math.min(maximum, Math.max(minimum, value)) }
export const moduleVersion8 = "1.0.0"
