import { createDocument, normalizeDocument, type Document } from "../domain/document.ts"

export interface DocumentTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Document[]>
  save(value: Document, signal?: AbortSignal): Promise<Document>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class DocumentService {
  constructor(private readonly transport: DocumentTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Document[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeDocument).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Document> {
    return this.transport.save(createDocument(id, tenantId), signal)
  }
  async update(value: Document, signal?: AbortSignal): Promise<Document> {
    return this.transport.save(normalizeDocument(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
