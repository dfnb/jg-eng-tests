export type FilterState = Readonly<{ revision: number; status: string; values: readonly string[] }>
export type FilterListener = (state: FilterState) => void

export class FilterStore {
  private state: FilterState = { revision: 0, status: "idle", values: [] }
  private readonly listeners = new Set<FilterListener>()
  snapshot(): FilterState { return this.state }
  subscribe(listener: FilterListener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }
  replace(values: readonly string[]): void { this.publish({ ...this.state, revision: this.state.revision + 1, values: [...values] }) }
  setStatus(status: string): void { this.publish({ ...this.state, revision: this.state.revision + 1, status }) }
  clear(): void { this.publish({ revision: this.state.revision + 1, status: "idle", values: [] }) }
  private publish(next: FilterState): void { this.state = next; for (const listener of this.listeners) listener(next) }
}
export const filterStoreVersion = 6
