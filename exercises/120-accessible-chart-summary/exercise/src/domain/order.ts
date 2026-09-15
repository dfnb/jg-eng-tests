export interface Order {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createOrder(id: string, tenantId: string): Order {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeOrder(value: Order): Order {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isOrderActive(value: Order): boolean { return value.status === "active" }
export function compareOrder(left: Order, right: Order): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeOrder(current: Order, patch: Partial<Order>): Order { return normalizeOrder({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexOrders(values: readonly Order[]): ReadonlyMap<string, Order> { return new Map(values.map(value => [value.id, value])) }
export function visibleOrders(values: readonly Order[]): readonly Order[] { return values.filter(isOrderActive).toSorted(compareOrder) }
