export interface Feature5View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature5Controller {
  private view: Feature5View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature5View { return this.view }
  begin(): Feature5View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature5View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature5View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature5View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature5View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
