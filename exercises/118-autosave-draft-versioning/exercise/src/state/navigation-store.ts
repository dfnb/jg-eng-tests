export type NavigationState = Readonly<{ revision: number; status: string; values: readonly string[] }>
export type NavigationListener = (state: NavigationState) => void

export class NavigationStore {
  private state: NavigationState = { revision: 0, status: "idle", values: [] }
  private readonly listeners = new Set<NavigationListener>()
  snapshot(): NavigationState { return this.state }
  subscribe(listener: NavigationListener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }
  replace(values: readonly string[]): void { this.publish({ ...this.state, revision: this.state.revision + 1, values: [...values] }) }
  setStatus(status: string): void { this.publish({ ...this.state, revision: this.state.revision + 1, status }) }
  clear(): void { this.publish({ revision: this.state.revision + 1, status: "idle", values: [] }) }
  private publish(next: NavigationState): void { this.state = next; for (const listener of this.listeners) listener(next) }
}
export const navigationStoreVersion = 2
