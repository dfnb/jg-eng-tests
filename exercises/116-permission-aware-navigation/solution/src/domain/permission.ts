export interface Permission {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createPermission(id: string, tenantId: string): Permission {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizePermission(value: Permission): Permission {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isPermissionActive(value: Permission): boolean { return value.status === "active" }
export function comparePermission(left: Permission, right: Permission): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergePermission(current: Permission, patch: Partial<Permission>): Permission { return normalizePermission({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexPermissions(values: readonly Permission[]): ReadonlyMap<string, Permission> { return new Map(values.map(value => [value.id, value])) }
export function visiblePermissions(values: readonly Permission[]): readonly Permission[] { return values.filter(isPermissionActive).toSorted(comparePermission) }
