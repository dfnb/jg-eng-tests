import { createOrder, normalizeOrder, type Order } from "../domain/order.ts"

export interface OrderTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Order[]>
  save(value: Order, signal?: AbortSignal): Promise<Order>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class OrderService {
  constructor(private readonly transport: OrderTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Order[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeOrder).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Order> {
    return this.transport.save(createOrder(id, tenantId), signal)
  }
  async update(value: Order, signal?: AbortSignal): Promise<Order> {
    return this.transport.save(normalizeOrder(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
