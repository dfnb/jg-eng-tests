export type NotificationState = Readonly<{ revision: number; status: string; values: readonly string[] }>
export type NotificationListener = (state: NotificationState) => void

export class NotificationStore {
  private state: NotificationState = { revision: 0, status: "idle", values: [] }
  private readonly listeners = new Set<NotificationListener>()
  snapshot(): NotificationState { return this.state }
  subscribe(listener: NotificationListener): () => void {
    this.listeners.add(listener)
    listener(this.state)
    return () => this.listeners.delete(listener)
  }
  replace(values: readonly string[]): void { this.publish({ ...this.state, revision: this.state.revision + 1, values: [...values] }) }
  setStatus(status: string): void { this.publish({ ...this.state, revision: this.state.revision + 1, status }) }
  clear(): void { this.publish({ revision: this.state.revision + 1, status: "idle", values: [] }) }
  private publish(next: NotificationState): void { this.state = next; for (const listener of this.listeners) listener(next) }
}
export const notificationStoreVersion = 3
