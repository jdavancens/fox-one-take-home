import type { CrewCredit, Show } from '../types'

export const TVMAZE_BASE_URL = 'https://api.tvmaze.com'

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

async function get<T>(path: string, attempt = 0, maxRetries = 3) {
  const res = await fetch(`${TVMAZE_BASE_URL}/${path}`)

  const shouldRetry = (res.status === 429 || res.status >= 500) && attempt < maxRetries

  if (shouldRetry) {
    await sleep(1000 * (attempt + 1))
    return get<T>(path, attempt + 1, maxRetries)
  }

  if (!res.ok) throw new Error(`API Error: ${res.status}`)
  return res.json()
} 

export async function fetchShows(ids: number[]): Promise<Show[]> {
  return Promise.all(ids.map((id) =>  get<Show>(`shows/${id}?embed=crew`)))
}

export async function fetchCredits(id: number) {
  return await get<CrewCredit[]>(`people/${id}/crewcredits?embed=show`)
}