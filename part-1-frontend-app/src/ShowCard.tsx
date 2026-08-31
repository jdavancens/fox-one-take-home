import { useState } from 'react'
import ComposerCredits from "./ComposerCredits"
import type { CrewMember, Show } from './types'

type CrewMemberDetailsProps = {
  crewMember: CrewMember
  showId: number
}

type ShowCardProps = Pick<Show, 'id' | 'name' | 'premiered' | 'image' | '_embedded'>


function CrewMemberDetails({ crewMember, showId }: CrewMemberDetailsProps) {
  const [open, setOpen] = useState(false)

  return (
    <details name={`crew-${showId}`}  onToggle={(e) => setOpen(e.currentTarget.open)}>
      <summary>
        {crewMember.person.name} — {crewMember.type}
      </summary>
      {open && (
        <ComposerCredits
          personId={crewMember.person.id}
          showId={showId}
        />
      )}
    </details>
  )
}

const musicCrewFilter = (crewMember: CrewMember) => {
  return [
    'Composer',
    'Music',
    'Music Editor',
    'Music Scoring Mixer',
    'Music Supervisor'
  ].includes(crewMember.type)
}

function ShowCard({
  id,
  image,
  name,
  premiered,
  _embedded,
}: ShowCardProps) {
  return (
    <article className="show-card">
      <div className="show-card-poster">
        {image && (
          <img src={image?.medium} alt={`${name}-image`} />
        )}
      </div>

      <div className="show-card-meta">
        <h2>{name}</h2>
        {premiered && (
          <p className="premiere">
            <time dateTime={premiered}> {premiered.slice(0, 4)}</time>
          </p>
        )}
      </div>

      <div className="show-card-crew">
        {_embedded?.crew.filter(musicCrewFilter).map((crewMember) => (
          <CrewMemberDetails
            key={`${crewMember.person.id}-${crewMember.type}`}
            crewMember={crewMember}
            showId={id}
          />
        ))}
      </div>
    </article>
  )
}

export default ShowCard