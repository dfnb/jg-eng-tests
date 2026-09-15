import { createAlert, normalizeAlert, type Alert } from "../domain/alert.ts"

export interface AlertTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Alert[]>
  save(value: Alert, signal?: AbortSignal): Promise<Alert>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class AlertService {
  constructor(private readonly transport: AlertTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Alert[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeAlert).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Alert> {
    return this.transport.save(createAlert(id, tenantId), signal)
  }
  async update(value: Alert, signal?: AbortSignal): Promise<Alert> {
    return this.transport.save(normalizeAlert(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
