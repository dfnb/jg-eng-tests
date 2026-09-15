export interface Account {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createAccount(id: string, tenantId: string): Account {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeAccount(value: Account): Account {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isAccountActive(value: Account): boolean { return value.status === "active" }
export function compareAccount(left: Account, right: Account): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeAccount(current: Account, patch: Partial<Account>): Account { return normalizeAccount({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexAccounts(values: readonly Account[]): ReadonlyMap<string, Account> { return new Map(values.map(value => [value.id, value])) }
export function visibleAccounts(values: readonly Account[]): readonly Account[] { return values.filter(isAccountActive).toSorted(compareAccount) }
