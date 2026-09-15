export interface Route {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createRoute(id: string, tenantId: string): Route {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeRoute(value: Route): Route {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isRouteActive(value: Route): boolean { return value.status === "active" }
export function compareRoute(left: Route, right: Route): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeRoute(current: Route, patch: Partial<Route>): Route { return normalizeRoute({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexRoutes(values: readonly Route[]): ReadonlyMap<string, Route> { return new Map(values.map(value => [value.id, value])) }
export function visibleRoutes(values: readonly Route[]): readonly Route[] { return values.filter(isRouteActive).toSorted(compareRoute) }
