export interface Feature4View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature4Controller {
  private view: Feature4View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature4View { return this.view }
  begin(): Feature4View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature4View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature4View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature4View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature4View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
