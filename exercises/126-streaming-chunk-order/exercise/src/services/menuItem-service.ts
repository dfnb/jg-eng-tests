import { createMenuItem, normalizeMenuItem, type MenuItem } from "../domain/menuItem.ts"

export interface MenuItemTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly MenuItem[]>
  save(value: MenuItem, signal?: AbortSignal): Promise<MenuItem>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class MenuItemService {
  constructor(private readonly transport: MenuItemTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly MenuItem[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeMenuItem).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<MenuItem> {
    return this.transport.save(createMenuItem(id, tenantId), signal)
  }
  async update(value: MenuItem, signal?: AbortSignal): Promise<MenuItem> {
    return this.transport.save(normalizeMenuItem(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
