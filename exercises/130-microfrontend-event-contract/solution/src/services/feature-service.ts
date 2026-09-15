import { createFeature, normalizeFeature, type Feature } from "../domain/feature.ts"

export interface FeatureTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Feature[]>
  save(value: Feature, signal?: AbortSignal): Promise<Feature>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class FeatureService {
  constructor(private readonly transport: FeatureTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Feature[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeFeature).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Feature> {
    return this.transport.save(createFeature(id, tenantId), signal)
  }
  async update(value: Feature, signal?: AbortSignal): Promise<Feature> {
    return this.transport.save(normalizeFeature(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
