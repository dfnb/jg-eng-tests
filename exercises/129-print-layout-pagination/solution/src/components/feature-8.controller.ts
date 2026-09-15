export interface Feature8View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature8Controller {
  private view: Feature8View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature8View { return this.view }
  begin(): Feature8View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature8View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature8View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature8View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature8View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
