import { createCustomer, normalizeCustomer, type Customer } from "../domain/customer.ts"

export interface CustomerTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Customer[]>
  save(value: Customer, signal?: AbortSignal): Promise<Customer>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class CustomerService {
  constructor(private readonly transport: CustomerTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Customer[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeCustomer).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Customer> {
    return this.transport.save(createCustomer(id, tenantId), signal)
  }
  async update(value: Customer, signal?: AbortSignal): Promise<Customer> {
    return this.transport.save(normalizeCustomer(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
