export type CrewCredit = {
  type: string
  _embedded: {
    show: {
      id: number
      name: string
      premiered: string | null
    }
  }
}

export type CrewMember = {
  type: string
  person: { id: number; name: string }
}

export type Show = {
  id: number
  name: string
  premiered: string | null
  summary: string | null
  image: { medium: string; original: string } | null
  network: { name: string } | null
  _embedded?: { crew: CrewMember[] }
}

