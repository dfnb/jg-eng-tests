export interface Document {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createDocument(id: string, tenantId: string): Document {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeDocument(value: Document): Document {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isDocumentActive(value: Document): boolean { return value.status === "active" }
export function compareDocument(left: Document, right: Document): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeDocument(current: Document, patch: Partial<Document>): Document { return normalizeDocument({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexDocuments(values: readonly Document[]): ReadonlyMap<string, Document> { return new Map(values.map(value => [value.id, value])) }
export function visibleDocuments(values: readonly Document[]): readonly Document[] { return values.filter(isDocumentActive).toSorted(compareDocument) }
