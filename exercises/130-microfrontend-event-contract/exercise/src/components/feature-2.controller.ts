export interface Feature2View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature2Controller {
  private view: Feature2View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature2View { return this.view }
  begin(): Feature2View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature2View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature2View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature2View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature2View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
