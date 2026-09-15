export interface Address {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createAddress(id: string, tenantId: string): Address {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeAddress(value: Address): Address {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isAddressActive(value: Address): boolean { return value.status === "active" }
export function compareAddress(left: Address, right: Address): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeAddress(current: Address, patch: Partial<Address>): Address { return normalizeAddress({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexAddresss(values: readonly Address[]): ReadonlyMap<string, Address> { return new Map(values.map(value => [value.id, value])) }
export function visibleAddresss(values: readonly Address[]): readonly Address[] { return values.filter(isAddressActive).toSorted(compareAddress) }
