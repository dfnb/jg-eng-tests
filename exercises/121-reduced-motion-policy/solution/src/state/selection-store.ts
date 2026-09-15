export type SelectionState = Readonly<{ revision: number; status: string; values: readonly string[] }>
export type SelectionListener = (state: SelectionState) => void

export class SelectionStore {
  private state: SelectionState = { revision: 0, status: "idle", values: [] }
  private readonly listeners = new Set<SelectionListener>()
  snapshot(): SelectionState { return this.state }
  subscribe(listener: SelectionListener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }
  replace(values: readonly string[]): void { this.publish({ ...this.state, revision: this.state.revision + 1, values: [...values] }) }
  setStatus(status: string): void { this.publish({ ...this.state, revision: this.state.revision + 1, status }) }
  clear(): void { this.publish({ revision: this.state.revision + 1, status: "idle", values: [] }) }
  private publish(next: SelectionState): void { this.state = next; for (const listener of this.listeners) listener(next) }
}
export const selectionStoreVersion = 5
