export interface Workspace {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createWorkspace(id: string, tenantId: string): Workspace {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeWorkspace(value: Workspace): Workspace {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isWorkspaceActive(value: Workspace): boolean { return value.status === "active" }
export function compareWorkspace(left: Workspace, right: Workspace): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeWorkspace(current: Workspace, patch: Partial<Workspace>): Workspace { return normalizeWorkspace({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexWorkspaces(values: readonly Workspace[]): ReadonlyMap<string, Workspace> { return new Map(values.map(value => [value.id, value])) }
export function visibleWorkspaces(values: readonly Workspace[]): readonly Workspace[] { return values.filter(isWorkspaceActive).toSorted(compareWorkspace) }
