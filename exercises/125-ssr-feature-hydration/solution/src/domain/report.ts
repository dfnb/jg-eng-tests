export interface Report {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createReport(id: string, tenantId: string): Report {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeReport(value: Report): Report {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isReportActive(value: Report): boolean { return value.status === "active" }
export function compareReport(left: Report, right: Report): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeReport(current: Report, patch: Partial<Report>): Report { return normalizeReport({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexReports(values: readonly Report[]): ReadonlyMap<string, Report> { return new Map(values.map(value => [value.id, value])) }
export function visibleReports(values: readonly Report[]): readonly Report[] { return values.filter(isReportActive).toSorted(compareReport) }
