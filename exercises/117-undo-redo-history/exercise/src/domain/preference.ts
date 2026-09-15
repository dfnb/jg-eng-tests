export interface Preference {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createPreference(id: string, tenantId: string): Preference {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizePreference(value: Preference): Preference {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isPreferenceActive(value: Preference): boolean { return value.status === "active" }
export function comparePreference(left: Preference, right: Preference): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergePreference(current: Preference, patch: Partial<Preference>): Preference { return normalizePreference({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexPreferences(values: readonly Preference[]): ReadonlyMap<string, Preference> { return new Map(values.map(value => [value.id, value])) }
export function visiblePreferences(values: readonly Preference[]): readonly Preference[] { return values.filter(isPreferenceActive).toSorted(comparePreference) }
