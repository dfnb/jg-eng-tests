export interface Actor {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createActor(id: string, tenantId: string): Actor {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeActor(value: Actor): Actor {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isActorActive(value: Actor): boolean { return value.status === "active" }
export function compareActor(left: Actor, right: Actor): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeActor(current: Actor, patch: Partial<Actor>): Actor { return normalizeActor({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexActors(values: readonly Actor[]): ReadonlyMap<string, Actor> { return new Map(values.map(value => [value.id, value])) }
export function visibleActors(values: readonly Actor[]): readonly Actor[] { return values.filter(isActorActive).toSorted(compareActor) }
