import { useEffect, useState } from 'react'
import { fetchShows } from './api/tvmaze'
import ShowList from './ShowList'

import type { Show } from './types'

const foxShows = [
  83, // the simpsons
  58, // new girl
  65, // bones
  180, // firefly
  430, // the x-files
  499, // married... with children
  541, // prison break
  587, // that 70's show
]

function App() {
  const [shows, setShows] = useState<Show[]>([]);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetchShows(foxShows)
      .then(setShows)
      .catch(setError)
  }, [])

  return (
    <main className="container">
      <header>
        <h1>Iconic Fox TV Music</h1>
        <p>Composers and music supervisors</p>
      </header>
      <section>
        {error ? <p>{error?.message}</p> : shows.length === 0 ? <progress />: <ShowList shows={shows} />}
      </section>
    </main>
  )
}

export default App
