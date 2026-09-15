export interface MenuItem {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createMenuItem(id: string, tenantId: string): MenuItem {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeMenuItem(value: MenuItem): MenuItem {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isMenuItemActive(value: MenuItem): boolean { return value.status === "active" }
export function compareMenuItem(left: MenuItem, right: MenuItem): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeMenuItem(current: MenuItem, patch: Partial<MenuItem>): MenuItem { return normalizeMenuItem({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexMenuItems(values: readonly MenuItem[]): ReadonlyMap<string, MenuItem> { return new Map(values.map(value => [value.id, value])) }
export function visibleMenuItems(values: readonly MenuItem[]): readonly MenuItem[] { return values.filter(isMenuItemActive).toSorted(compareMenuItem) }
