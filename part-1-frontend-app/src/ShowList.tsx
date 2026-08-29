import ShowCard from './ShowCard'

import type { Show } from './types'

type ShowListProps = {
  shows: Show[]
}

const byPremiereDate = (a: Show, b: Show) => {
  if (!a.premiered && !b.premiered) return 0
  if (!a.premiered) return 1   // nulls last
  if (!b.premiered) return -1
  return a.premiered.localeCompare(b.premiered)
}

function ShowList(props: ShowListProps) {
  return (
    <ul className="show-list">
      {props.shows?.sort(byPremiereDate).map(({
        id,
        name,
        premiered,
        image,
        _embedded,
      }) => (
        <li key={id}>
          <ShowCard
            id={id}
            name={name}
            premiered={premiered}
            image={image}
            _embedded={_embedded}
          />
        </li>
      ))}
    </ul>
  )
}

export default ShowList