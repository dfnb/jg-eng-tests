export type DraftState = Readonly<{ revision: number; status: string; values: readonly string[] }>
export type DraftListener = (state: DraftState) => void

export class DraftStore {
  private state: DraftState = { revision: 0, status: "idle", values: [] }
  private readonly listeners = new Set<DraftListener>()
  snapshot(): DraftState { return this.state }
  subscribe(listener: DraftListener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }
  replace(values: readonly string[]): void { this.publish({ ...this.state, revision: this.state.revision + 1, values: [...values] }) }
  setStatus(status: string): void { this.publish({ ...this.state, revision: this.state.revision + 1, status }) }
  clear(): void { this.publish({ revision: this.state.revision + 1, status: "idle", values: [] }) }
  private publish(next: DraftState): void { this.state = next; for (const listener of this.listeners) listener(next) }
}
export const draftStoreVersion = 4
