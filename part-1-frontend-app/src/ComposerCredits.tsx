import { useEffect, useState } from "react"
import { fetchCredits } from "./api/tvmaze"

import type { CrewCredit } from "./types"

type ComposerCreditsProps = {
  personId: number
  showId: number
}

const byShowPremiere = (a: CrewCredit, b: CrewCredit) => {
  const aDate = a._embedded.show.premiered ?? ''
  const bDate = b._embedded.show.premiered ?? ''
  return aDate.localeCompare(bDate) // oldest first; negate for newest first
}

function ComposerCredits({ personId, showId }: ComposerCreditsProps) {
  const [credits, setCredits] = useState<CrewCredit[]>([])
  const [loaded, setLoaded] = useState(false)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    fetchCredits(personId).then(setCredits).then(() => setLoaded(true)).catch(setError)
  }, [])

  if (error) return <p>{error.message}</p>

  if (!loaded) return <progress />
  
  const otherCredits = credits
    .filter((credit) => credit._embedded.show.id !== showId)
    .sort(byShowPremiere)

  if (loaded && otherCredits.length === 0) return (<p>No other credits found</p>)

  return (
    <>
      <p>Other credits:</p>
      <ul>
        {otherCredits.map((credit) => (
          <li key={`${credit._embedded.show.name}-${credit.type}`}>
            <i>{credit._embedded.show.name}</i>
            {credit._embedded.show.premiered && ` (${credit._embedded.show.premiered.slice(0, 4)})`}
            {' '}— {credit.type}
          </li>
        ))}
      </ul>
    </>
  )
}

export default ComposerCredits