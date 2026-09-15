import { createActor, normalizeActor, type Actor } from "../domain/actor.ts"

export interface ActorTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Actor[]>
  save(value: Actor, signal?: AbortSignal): Promise<Actor>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class ActorService {
  constructor(private readonly transport: ActorTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Actor[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeActor).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Actor> {
    return this.transport.save(createActor(id, tenantId), signal)
  }
  async update(value: Actor, signal?: AbortSignal): Promise<Actor> {
    return this.transport.save(normalizeActor(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
