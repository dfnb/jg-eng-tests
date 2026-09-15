export interface Alert {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createAlert(id: string, tenantId: string): Alert {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeAlert(value: Alert): Alert {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isAlertActive(value: Alert): boolean { return value.status === "active" }
export function compareAlert(left: Alert, right: Alert): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeAlert(current: Alert, patch: Partial<Alert>): Alert { return normalizeAlert({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexAlerts(values: readonly Alert[]): ReadonlyMap<string, Alert> { return new Map(values.map(value => [value.id, value])) }
export function visibleAlerts(values: readonly Alert[]): readonly Alert[] { return values.filter(isAlertActive).toSorted(compareAlert) }
