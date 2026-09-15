export interface Feature7View {
  busy: boolean
  message: string
  items: readonly string[]
  selectedId: string | null
}
export class Feature7Controller {
  private view: Feature7View = { busy: false, message: "", items: [], selectedId: null }
  snapshot(): Feature7View { return this.view }
  begin(): Feature7View { return this.view = { ...this.view, busy: true, message: "loading" } }
  succeed(items: readonly string[]): Feature7View { return this.view = { busy: false, message: items.length ? "ready" : "empty", items: [...items], selectedId: null } }
  fail(message: string): Feature7View { return this.view = { ...this.view, busy: false, message } }
  select(id: string): Feature7View { return this.view = { ...this.view, selectedId: this.view.items.includes(id) ? id : null } }
  reset(): Feature7View { return this.view = { busy: false, message: "", items: [], selectedId: null } }
}
