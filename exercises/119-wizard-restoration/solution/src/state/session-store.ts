export type SessionState = Readonly<{ revision: number; status: string; values: readonly string[] }>
export type SessionListener = (state: SessionState) => void

export class SessionStore {
  private state: SessionState = { revision: 0, status: "idle", values: [] }
  private readonly listeners = new Set<SessionListener>()
  snapshot(): SessionState { return this.state }
  subscribe(listener: SessionListener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }
  replace(values: readonly string[]): void { this.publish({ ...this.state, revision: this.state.revision + 1, values: [...values] }) }
  setStatus(status: string): void { this.publish({ ...this.state, revision: this.state.revision + 1, status }) }
  clear(): void { this.publish({ revision: this.state.revision + 1, status: "idle", values: [] }) }
  private publish(next: SessionState): void { this.state = next; for (const listener of this.listeners) listener(next) }
}
export const sessionStoreVersion = 1
