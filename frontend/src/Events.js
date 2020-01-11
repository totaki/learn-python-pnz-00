import React, { useState, useEffect } from 'react';
import { BASE_API_URL } from "./const";
const EVENTS_ROUTE = 'events';


function Event({ title }) {
  return (
    <div className="card">
      <p>{title}</p>
    </div>
  )
}

function Events() {
  const [events, setEvents] = useState([]);
  const [url, setURL] = useState(`${BASE_API_URL}/events/`);
  const [pagination, setPagination] = useState([null, null]);

  useEffect(() => {
    fetch(url)
      .then(result => result.json())
      .then(json => {
        setEvents(json.results);
        setPagination([json.next, json.previous])
      })
      .catch(e => console.log(e));
  }, [url]);

  const [next, previous] = pagination;

  return (
    <>
      <div>Список мероприятий</div>
      {events.map((e, i) => <Event {...e}/>)}
      <div className="btn-group" role="group" aria-label="paginationGroup">
        {previous ? <button  type="button" className="btn btn-secondary" onClick={() => setURL(previous)}>Previous</button> : null}
        {next ? <button  type="button" className="btn btn-secondary" onClick={() => setURL(next)}>Next</button> : null}
      </div>
    </>
  )
}

export default Events
export {
  EVENTS_ROUTE
}
