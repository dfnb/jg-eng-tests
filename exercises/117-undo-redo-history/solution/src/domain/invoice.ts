export interface Invoice {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createInvoice(id: string, tenantId: string): Invoice {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeInvoice(value: Invoice): Invoice {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isInvoiceActive(value: Invoice): boolean { return value.status === "active" }
export function compareInvoice(left: Invoice, right: Invoice): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeInvoice(current: Invoice, patch: Partial<Invoice>): Invoice { return normalizeInvoice({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexInvoices(values: readonly Invoice[]): ReadonlyMap<string, Invoice> { return new Map(values.map(value => [value.id, value])) }
export function visibleInvoices(values: readonly Invoice[]): readonly Invoice[] { return values.filter(isInvoiceActive).toSorted(compareInvoice) }
