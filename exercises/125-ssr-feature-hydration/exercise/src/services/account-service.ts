import { createAccount, normalizeAccount, type Account } from "../domain/account.ts"

export interface AccountTransport {
  list(tenantId: string, signal?: AbortSignal): Promise<readonly Account[]>
  save(value: Account, signal?: AbortSignal): Promise<Account>
  remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void>
}

export class AccountService {
  constructor(private readonly transport: AccountTransport) {}
  async list(tenantId: string, signal?: AbortSignal): Promise<readonly Account[]> {
    const rows = await this.transport.list(tenantId, signal)
    return rows.map(normalizeAccount).toSorted((a, b) => a.id.localeCompare(b.id))
  }
  async create(tenantId: string, id: string, signal?: AbortSignal): Promise<Account> {
    return this.transport.save(createAccount(id, tenantId), signal)
  }
  async update(value: Account, signal?: AbortSignal): Promise<Account> {
    return this.transport.save(normalizeAccount(value), signal)
  }
  async remove(tenantId: string, id: string, signal?: AbortSignal): Promise<void> {
    await this.transport.remove(tenantId, id, signal)
  }
}
