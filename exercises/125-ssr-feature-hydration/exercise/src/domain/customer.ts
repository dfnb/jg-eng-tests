export interface Customer {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createCustomer(id: string, tenantId: string): Customer {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeCustomer(value: Customer): Customer {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isCustomerActive(value: Customer): boolean { return value.status === "active" }
export function compareCustomer(left: Customer, right: Customer): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeCustomer(current: Customer, patch: Partial<Customer>): Customer { return normalizeCustomer({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexCustomers(values: readonly Customer[]): ReadonlyMap<string, Customer> { return new Map(values.map(value => [value.id, value])) }
export function visibleCustomers(values: readonly Customer[]): readonly Customer[] { return values.filter(isCustomerActive).toSorted(compareCustomer) }
