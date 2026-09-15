import { createInvoice, normalizeInvoice, type Invoice } from "../domain/invoice.ts"

export interface InvoiceTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Invoice[]>
  save(value: Invoice, signal?: AbortSignal): Promise<Invoice>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class InvoiceService {
  constructor(private readonly transport: InvoiceTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Invoice[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeInvoice).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Invoice> {
    return this.transport.save(createInvoice(id, tenantId), signal)
  }
  async update(value: Invoice, signal?: AbortSignal): Promise<Invoice> {
    return this.transport.save(normalizeInvoice(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
