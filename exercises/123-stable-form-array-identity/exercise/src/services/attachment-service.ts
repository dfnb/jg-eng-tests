import { createAttachment, normalizeAttachment, type Attachment } from "../domain/attachment.ts"

export interface AttachmentTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Attachment[]>
  save(value: Attachment, signal?: AbortSignal): Promise<Attachment>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class AttachmentService {
  constructor(private readonly transport: AttachmentTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Attachment[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeAttachment).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Attachment> {
    return this.transport.save(createAttachment(id, tenantId), signal)
  }
  async update(value: Attachment, signal?: AbortSignal): Promise<Attachment> {
    return this.transport.save(normalizeAttachment(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
