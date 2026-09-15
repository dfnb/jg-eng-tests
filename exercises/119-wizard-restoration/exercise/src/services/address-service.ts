import { createAddress, normalizeAddress, type Address } from "../domain/address.ts"

export interface AddressTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Address[]>
  save(value: Address, signal?: AbortSignal): Promise<Address>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class AddressService {
  constructor(private readonly transport: AddressTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Address[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeAddress).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Address> {
    return this.transport.save(createAddress(id, tenantId), signal)
  }
  async update(value: Address, signal?: AbortSignal): Promise<Address> {
    return this.transport.save(normalizeAddress(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
