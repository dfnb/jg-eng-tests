export type LayoutState = Readonly<{ revision: number; status: string; values: readonly string[] }>
export type LayoutListener = (state: LayoutState) => void

export class LayoutStore {
  private state: LayoutState = { revision: 0, status: "idle", values: [] }
  private readonly listeners = new Set<LayoutListener>()
  snapshot(): LayoutState { return this.state }
  subscribe(listener: LayoutListener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }
  replace(values: readonly string[]): void { this.publish({ ...this.state, revision: this.state.revision + 1, values: [...values] }) }
  setStatus(status: string): void { this.publish({ ...this.state, revision: this.state.revision + 1, status }) }
  clear(): void { this.publish({ revision: this.state.revision + 1, status: "idle", values: [] }) }
  private publish(next: LayoutState): void { this.state = next; for (const listener of this.listeners) listener(next) }
}
export const layoutStoreVersion = 7
