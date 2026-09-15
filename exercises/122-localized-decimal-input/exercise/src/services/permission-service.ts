import { createPermission, normalizePermission, type Permission } from "../domain/permission.ts"

export interface PermissionTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Permission[]>
  save(value: Permission, signal?: AbortSignal): Promise<Permission>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class PermissionService {
  constructor(private readonly transport: PermissionTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Permission[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizePermission).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Permission> {
    return this.transport.save(createPermission(id, tenantId), signal)
  }
  async update(value: Permission, signal?: AbortSignal): Promise<Permission> {
    return this.transport.save(normalizePermission(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
