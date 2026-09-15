export interface Attachment {
  id: string
  tenantId: string
  label: string
  status: "active" | "inactive" | "pending"
  version: number
  updatedAt: string
  metadata: Readonly<Record<string, string>>
}

export function createAttachment(id: string, tenantId: string): Attachment {
  return { id: id.trim(), tenantId: tenantId.trim(), label: "", status: "active", version: 1, updatedAt: new Date(0).toISOString(), metadata: {} }
}
export function normalizeAttachment(value: Attachment): Attachment {
  return { ...value, id: value.id.trim(), tenantId: value.tenantId.trim(), label: value.label.trim() }
}
export function isAttachmentActive(value: Attachment): boolean { return value.status === "active" }
export function compareAttachment(left: Attachment, right: Attachment): number { return left.label.localeCompare(right.label) || left.id.localeCompare(right.id) }
export function mergeAttachment(current: Attachment, patch: Partial<Attachment>): Attachment { return normalizeAttachment({ ...current, ...patch, id: current.id, tenantId: current.tenantId }) }
export function indexAttachments(values: readonly Attachment[]): ReadonlyMap<string, Attachment> { return new Map(values.map(value => [value.id, value])) }
export function visibleAttachments(values: readonly Attachment[]): readonly Attachment[] { return values.filter(isAttachmentActive).toSorted(compareAttachment) }
