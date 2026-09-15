export interface Feature3View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature3Controller {
  private view: Feature3View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature3View { return this.view }
  begin(): Feature3View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature3View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature3View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature3View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature3View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
