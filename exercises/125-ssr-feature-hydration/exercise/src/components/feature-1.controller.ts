export interface Feature1View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature1Controller {
  private view: Feature1View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature1View { return this.view }
  begin(): Feature1View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature1View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature1View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature1View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature1View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
