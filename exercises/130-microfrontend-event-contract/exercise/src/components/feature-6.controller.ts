export interface Feature6View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature6Controller {
  private view: Feature6View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature6View { return this.view }
  begin(): Feature6View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature6View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature6View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature6View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature6View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
