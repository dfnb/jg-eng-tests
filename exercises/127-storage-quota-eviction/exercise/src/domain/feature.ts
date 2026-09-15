export interface Feature {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createFeature(id: string, tenantId: string): Feature {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeFeature(value: Feature): Feature {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isFeatureActive(value: Feature): boolean { return value.status === "active" }
export function compareFeature(left: Feature, right: Feature): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeFeature(current: Feature, patch: Partial<Feature>): Feature { return normalizeFeature({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexFeatures(values: readonly Feature[]): ReadonlyMap<string, Feature> { return new Map(values.map(value => [value.id, value])) }
export function visibleFeatures(values: readonly Feature[]): readonly Feature[] { return values.filter(isFeatureActive).toSorted(compareFeature) }
